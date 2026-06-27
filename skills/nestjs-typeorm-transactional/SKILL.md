---
name: nestjs-typeorm-transactional
description: Implement, transplant, audit, or debug a custom NestJS + TypeORM transaction boundary built from TxRunner, AsyncLocalStorage, OrmHelper, a Transactional metadata decorator, and a Nest interceptor. Use when moving this transaction pattern to another project, making repositories participate in the active EntityManager, choosing isolation levels, verifying commit/rollback behavior, or diagnosing Transactional decorators that do not start transactions.
---

# NestJS TypeORM Transactional

Build transaction boundaries that propagate TypeORM's transactional `EntityManager` through asynchronous calls without passing it through every service and repository method.

## Required workflow

1. Inspect the target project's NestJS, TypeORM, RxJS, TypeScript, module, bootstrap, repository, test, and multi-data-source setup.
2. Read [architecture-and-audit.md](references/architecture-and-audit.md) to identify required components and known failure modes.
3. Decide the transaction entry point:
   - Use interceptor mode only for controller handler or controller class boundaries.
   - Use `TxRunner.run()` for service-to-service calls, jobs, consumers, schedulers, CLI flows, and other non-controller entry points.
   - Do not claim that a metadata-only service method decorator is active through a Nest controller interceptor.
4. Read [implementation-example.md](references/implementation-example.md) and adapt paths, module ownership, logging, isolation defaults, and data-source selection to the target project.
5. Replace transaction-sensitive repository access with `OrmHelper` lookups performed at method call time.
6. Keep the transaction scope around database work only. Move slow filesystem, network, subprocess, and streaming work outside it unless atomic coupling is explicitly required and supported.
7. Read [testing-example.md](references/testing-example.md), add proportional tests, and verify commit, rollback, context cleanup, nesting, and non-transactional fallback.
8. Report changed files, selected boundary mode, participating repositories, unsupported paths, tests run, and remaining risks.

## Required invariants

- Resolve repositories from the current transactional manager when one exists.
- Fall back to the normal `DataSource.manager` outside a transaction.
- Never cache a transaction-sensitive `Repository` or `EntityManager` in a constructor.
- Re-throw errors so TypeORM can roll back.
- Release context after both success and failure.
- Treat nested `run()` calls as join-existing semantics unless savepoints or independent transactions are deliberately implemented.
- State that an inner isolation request cannot replace an already-open outer transaction's isolation.
- Keep one transaction context per data source when a project uses multiple data sources.
- Avoid transactions around SSE or non-completing Observables because `lastValueFrom()` cannot finish them.

## Audit existing decorators

For every `@Transactional()` occurrence, classify it as:

- effective controller handler;
- effective controller class;
- ineffective service/provider method under interceptor-only wiring;
- unsupported non-request entry point;
- transaction containing avoidable external I/O.

Move ineffective boundaries to a controller entry point or replace them with explicit `TxRunner.run()`. Do not silently leave decorative metadata that has no runtime effect.

## Completion criteria

- Required providers are registered once and injectable.
- Every database call expected to join the transaction resolves through the active manager.
- At least one success test proves commit behavior.
- At least one failure test proves rollback across multiple writes.
- A post-failure test proves no `EntityManager` leaks into later work.
- The handoff identifies controller-only decorator semantics and any multi-data-source or streaming limitation.
