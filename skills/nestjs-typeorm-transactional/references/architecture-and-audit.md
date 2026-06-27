# Architecture and audit

## Component map

| Component | Responsibility | Required dependency |
|---|---|---|
| `TxContext` | Store the active `EntityManager` per asynchronous execution chain | Node `AsyncLocalStorage` |
| `TxRunner` | Open, commit, or roll back a TypeORM transaction and bind its manager | `DataSource`, `TxContext` |
| `OrmHelper` | Resolve a repository or manager from the active context, with normal-manager fallback | `DataSource`, `TxContext` |
| `Transactional` | Attach the requested isolation level as Nest metadata | `SetMetadata` |
| `TransactionalInterceptor` | Read controller metadata and execute the handler through `TxRunner` | `Reflector`, RxJS |
| `TransactionModule` | Register and export the transaction infrastructure | Nest module system |
| Repository adapters | Resolve transaction-aware repositories at call time | `OrmHelper` |

Runtime flow:

```text
controller handler with @Transactional()
  -> TransactionalInterceptor
  -> TxRunner.run()
  -> DataSource.transaction()
  -> TxContext.runWithManager()
  -> service
  -> repository
  -> OrmHelper.getRepo()
  -> transactional EntityManager
```

Outside a transaction, `OrmHelper` returns `DataSource.manager`, so the same repository code supports both paths.

## Source pattern traced from Office Manager

The source project uses:

- NestJS 11;
- TypeORM 0.3;
- RxJS 7;
- TypeScript legacy decorators with `experimentalDecorators` and `emitDecoratorMetadata`;
- `TxContext`, `TxRunner`, and `OrmHelper` exported by a global database module;
- a global `TransactionalInterceptor`;
- `READ COMMITTED` as the default isolation level;
- repositories that call `OrmHelper.getRepo()` or `getManager()` when executing a query.

Observed annotation locations include controllers and services. Under the current interceptor implementation, controller annotations are effective. Service annotations are not visible to `ExecutionContext.getHandler()` and therefore do not start a transaction. This distinction must be preserved in audits and migrations.

Concrete source locations:

| Source file | Current role or finding |
|---|---|
| `src/database/tx.context.ts` | Holds the `AsyncLocalStorage<EntityManager>` context |
| `src/database/tx.runner.ts` | Calls `DataSource.transaction()` and binds its manager |
| `src/util/orm.helper.ts` | Selects the context manager or default manager |
| `src/common/decorator/transactional.decorator.ts` | Stores isolation metadata under `TX_META_KEY` |
| `src/common/interceptor/transactional.interceptor.ts` | Reads controller execution-context metadata |
| `src/database/database.module.ts` | Registers and globally exports the infrastructure |
| `src/main.ts` | Manually registers the global interceptor |
| `src/hosts/hosts.controller.ts` | Effective controller-handler annotation |
| `src/profiles/profiles.controller.ts` | Effective controller-handler annotations |
| `src/documents/documents.service.ts` | Ineffective service annotation in interceptor-only mode |
| `src/github/github.service.ts` | Ineffective service annotation and long subprocess work inside the intended boundary |
| `src/github/repositories/repositories.service.ts` | Ineffective service annotation and subprocess work |
| `src/terminals/terminals.service.ts` | Ineffective service annotation |
| `src/todo-types/todo-types.service.ts` | Ineffective service annotation despite multiple related writes |

The source runner always opens a new `DataSource.transaction()` and logs with `console.log`. The portable example adds join-existing behavior and omits hard-coded logging. Preserve the source behavior only when independent nesting is intentional and verified.

## Target-project discovery

Before copying code, inspect:

```bash
rg -n '"@nestjs/(common|core)"|"typeorm"|"rxjs"' package.json
rg -n 'experimentalDecorators|emitDecoratorMetadata' tsconfig*.json
rg -n 'TypeOrmModule\.forRoot|DataSource|@InjectRepository|EntityManager' src
rg -n '@Transactional|APP_INTERCEPTOR|useGlobalInterceptors' src
rg -n 'Cron|Processor|SubscribeMessage|Command|Consumer|Sse' src
```

Determine:

- where the primary `DataSource` is registered;
- whether a global infrastructure module already exists;
- whether repositories use `@InjectRepository`, cached repositories, raw managers, or custom base repositories;
- whether transactions begin at HTTP controllers, services, jobs, queues, GraphQL resolvers, or commands;
- whether there are multiple named data sources;
- whether request handlers return finite Observables;
- which database supports each requested isolation level.

## Boundary decision

### Controller interceptor

Use for finite Nest controller or resolver execution when the framework execution context exposes the annotated handler.

Benefits:

- concise boundary declaration;
- centralized isolation metadata;
- automatic rollback when handler completion rejects.

Constraints:

- a controller interceptor does not intercept arbitrary service method calls;
- `lastValueFrom()` requires the handler Observable to complete;
- a transaction can stay open while downstream external I/O runs.

### Explicit service runner

Use for application-service boundaries and non-HTTP entry points:

```ts
return this.txRunner.run(
  () => this.performDatabaseWork(command),
  'READ COMMITTED',
);
```

This is the reliable default for cron, queue, event, CLI, and service-to-service flows.

## Repository participation audit

A transaction only covers queries issued through its `EntityManager`. Flag these patterns:

```ts
// Wrong when this repository is expected to join the AsyncLocalStorage transaction.
constructor(
  @InjectRepository(User)
  private readonly users: Repository<User>,
) {}

// Wrong: cached before a transaction starts.
private readonly users = this.orm.getRepo(User);
```

Prefer:

```ts
constructor(private readonly orm: OrmHelper) {}

findById(id: number) {
  return this.orm.getRepo(User).findOneBy({ id });
}
```

Also audit raw `DataSource.manager`, `dataSource.getRepository()`, query builders created from a non-context manager, and base repositories that cache a repository.

## Nesting semantics

The reference `TxRunner` joins an existing context:

```text
outer run opens transaction
  -> inner run detects current manager
  -> inner work uses outer transaction
```

Consequences:

- inner failure rolls back the outer transaction when propagated;
- inner isolation arguments are ignored because isolation is fixed when the outer transaction begins;
- catching an inner error may allow the outer work to commit;
- this is not `REQUIRES_NEW`;
- savepoints require explicit `QueryRunner` design and tests.

## Multiple data sources

A single unkeyed `TxContext` and `OrmHelper` support one data source. For multiple sources, create a keyed context such as `Map<dataSourceName, EntityManager>` and require the runner/helper to select a key. Do not let one data source's manager serve another source's entities.

## Operational risks

- Long transactions increase lock time and pool pressure.
- External API, filesystem, or subprocess work cannot be rolled back with the database.
- Database isolation support varies by driver.
- Swallowed exceptions can commit partial work.
- A repository bypassing `OrmHelper` silently executes outside the transaction.
- Request-scoped providers are unnecessary for this pattern; `AsyncLocalStorage` supplies asynchronous context propagation.
