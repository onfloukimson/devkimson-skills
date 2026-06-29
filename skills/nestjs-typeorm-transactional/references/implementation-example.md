# Implementation example

Adapt import aliases and filenames to the target project. These examples assume one TypeORM `DataSource`.

## 1. Isolation type and metadata key

```ts
// transaction.constants.ts
export const TRANSACTION_METADATA = Symbol('TRANSACTION_METADATA');

export type TransactionIsolation =
  | 'READ UNCOMMITTED'
  | 'READ COMMITTED'
  | 'REPEATABLE READ'
  | 'SERIALIZABLE';
```

Using a local union avoids depending on TypeORM's internal driver type path.

## 2. Transaction context

```ts
// tx.context.ts
import { Injectable } from '@nestjs/common';
import { AsyncLocalStorage } from 'node:async_hooks';
import type { EntityManager } from 'typeorm';

@Injectable()
export class TxContext {
  private readonly storage = new AsyncLocalStorage<EntityManager>();

  runWithManager<T>(
    manager: EntityManager,
    work: () => Promise<T>,
  ): Promise<T> {
    return this.storage.run(manager, work);
  }

  get currentManager(): EntityManager | undefined {
    return this.storage.getStore();
  }
}
```

## 3. Transaction runner

```ts
// tx.runner.ts
import { Injectable } from '@nestjs/common';
import { DataSource } from 'typeorm';
import type { TransactionIsolation } from './transaction.constants';
import { TxContext } from './tx.context';

@Injectable()
export class TxRunner {
  constructor(
    private readonly dataSource: DataSource,
    private readonly context: TxContext,
  ) {}

  run<T>(
    work: () => Promise<T>,
    isolation: TransactionIsolation = 'READ COMMITTED',
  ): Promise<T> {
    if (this.context.currentManager) {
      return work();
    }

    return this.dataSource.transaction(isolation, manager =>
      this.context.runWithManager(manager, work),
    );
  }
}
```

Remove join-existing behavior only when the project deliberately implements savepoints or independent transactions.

## 4. Transaction-aware ORM helper

```ts
// orm.helper.ts
import { Injectable } from '@nestjs/common';
import {
  DataSource,
  type EntityManager,
  type EntityTarget,
  type ObjectLiteral,
  type Repository,
} from 'typeorm';
import { TxContext } from './tx.context';

@Injectable()
export class OrmHelper {
  constructor(
    private readonly dataSource: DataSource,
    private readonly context: TxContext,
  ) {}

  getManager(): EntityManager {
    return this.context.currentManager ?? this.dataSource.manager;
  }

  getRepo<E extends ObjectLiteral>(
    entity: EntityTarget<E>,
  ): Repository<E> {
    return this.getManager().getRepository(entity);
  }
}
```

## 5. Metadata decorator

```ts
// transactional.decorator.ts
import { SetMetadata } from '@nestjs/common';
import {
  TRANSACTION_METADATA,
  type TransactionIsolation,
} from './transaction.constants';

export function Transactional(
  isolation: TransactionIsolation = 'READ COMMITTED',
): MethodDecorator & ClassDecorator {
  return SetMetadata(TRANSACTION_METADATA, isolation);
}
```

This decorator stores metadata. It does not wrap a service method by itself.

## 6. Controller interceptor

```ts
// transactional.interceptor.ts
import {
  CallHandler,
  ExecutionContext,
  Injectable,
  NestInterceptor,
} from '@nestjs/common';
import { Reflector } from '@nestjs/core';
import { from, lastValueFrom, type Observable } from 'rxjs';
import {
  TRANSACTION_METADATA,
  type TransactionIsolation,
} from './transaction.constants';
import { TxRunner } from './tx.runner';

@Injectable()
export class TransactionalInterceptor implements NestInterceptor {
  constructor(
    private readonly runner: TxRunner,
    private readonly reflector: Reflector,
  ) {}

  intercept(context: ExecutionContext, next: CallHandler): Observable<unknown> {
    const isolation = this.reflector.getAllAndOverride<TransactionIsolation>(
      TRANSACTION_METADATA,
      [context.getHandler(), context.getClass()],
    );

    if (!isolation) {
      return next.handle();
    }

    return from(
      this.runner.run(
        () => lastValueFrom(next.handle()),
        isolation,
      ),
    );
  }
}
```

Do not apply this to SSE or another non-completing Observable.

## 7. Module registration

If the target project already registers TypeORM, add only the transaction providers:

```ts
// transaction.module.ts
import { Global, Module } from '@nestjs/common';
import { APP_INTERCEPTOR } from '@nestjs/core';
import { OrmHelper } from './orm.helper';
import { TransactionalInterceptor } from './transactional.interceptor';
import { TxContext } from './tx.context';
import { TxRunner } from './tx.runner';

@Global()
@Module({
  providers: [
    TxContext,
    TxRunner,
    OrmHelper,
    {
      provide: APP_INTERCEPTOR,
      useClass: TransactionalInterceptor,
    },
  ],
  exports: [TxContext, TxRunner, OrmHelper],
})
export class TransactionModule {}
```

Import `TransactionModule` once from the root application module. Do not add a second `TypeOrmModule.forRoot*()` registration.

If interceptor order is already managed manually, preserve that order and register one instance:

```ts
app.useGlobalInterceptors(
  app.get(TransactionalInterceptor),
);
```

Register the interceptor as a provider before resolving it from the application.

## 8. Repository example

```ts
// accounts.repository.ts
import { Injectable } from '@nestjs/common';
import { OrmHelper } from '../transaction/orm.helper';
import { Account } from './account.entity';

@Injectable()
export class AccountsRepository {
  constructor(private readonly orm: OrmHelper) {}

  findById(id: number) {
    return this.orm.getRepo(Account).findOneBy({ id });
  }

  save(account: Account) {
    return this.orm.getRepo(Account).save(account);
  }

  delete(id: number) {
    return this.orm.getRepo(Account).delete(id);
  }
}
```

## 9. Controller-bound transaction

```ts
@Post('transfer')
@Transactional('SERIALIZABLE')
transfer(@Body() command: TransferCommand) {
  return this.transferService.transfer(command);
}
```

All participating repositories must resolve through `OrmHelper`.

## 10. Service or job boundary

```ts
@Injectable()
export class SettlementJob {
  constructor(
    private readonly txRunner: TxRunner,
    private readonly settlements: SettlementsRepository,
    private readonly ledger: LedgerRepository,
  ) {}

  execute(command: SettlementCommand) {
    return this.txRunner.run(async () => {
      const settlement = await this.settlements.create(command);
      await this.ledger.record(settlement);
      return settlement;
    });
  }
}
```

Use this form for cron, queues, commands, event consumers, and direct service calls.

## 11. Keep external work outside the transaction

```ts
async synchronize(command: SyncCommand) {
  const remote = await this.remoteClient.fetch(command.remoteId);

  return this.txRunner.run(() =>
    this.persistRemoteState(remote),
  );
}
```

If the database write and external side effect must be coordinated, use an outbox, idempotency key, retry policy, or compensating action rather than assuming a database transaction can roll back the external system.
