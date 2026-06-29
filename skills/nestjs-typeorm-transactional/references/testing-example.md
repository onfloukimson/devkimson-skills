# Testing example

Test behavior, not only metadata presence.

## Unit-test `TxRunner`

```ts
import type { DataSource, EntityManager } from 'typeorm';
import { TxContext } from './tx.context';
import { TxRunner } from './tx.runner';

describe('TxRunner', () => {
  const manager = {} as EntityManager;
  let context: TxContext;
  let transaction: jest.Mock;
  let runner: TxRunner;

  beforeEach(() => {
    context = new TxContext();
    transaction = jest.fn(
      async (_isolation, callback: (em: EntityManager) => Promise<unknown>) =>
        callback(manager),
    );
    runner = new TxRunner({ transaction } as unknown as DataSource, context);
  });

  it('binds the transaction manager while work runs', async () => {
    await runner.run(async () => {
      expect(context.currentManager).toBe(manager);
      return 'ok';
    });

    expect(transaction).toHaveBeenCalledTimes(1);
    expect(context.currentManager).toBeUndefined();
  });

  it('clears context after an error', async () => {
    await expect(
      runner.run(async () => {
        throw new Error('rollback');
      }),
    ).rejects.toThrow('rollback');

    expect(context.currentManager).toBeUndefined();
  });

  it('joins an existing transaction', async () => {
    await runner.run(async () => {
      await runner.run(async () => {
        expect(context.currentManager).toBe(manager);
      }, 'SERIALIZABLE');
    });

    expect(transaction).toHaveBeenCalledTimes(1);
  });
});
```

## Unit-test `OrmHelper`

Verify both manager sources:

```ts
it('uses the transaction manager when present', async () => {
  await context.runWithManager(transactionManager, async () => {
    expect(helper.getManager()).toBe(transactionManager);
    expect(helper.getRepo(User)).toBe(transactionRepository);
  });
});

it('uses the default manager outside a transaction', () => {
  expect(helper.getManager()).toBe(dataSource.manager);
});
```

## Integration rollback test

Use the target project's actual test database and two transaction-aware repositories:

```ts
it('rolls back all writes when the second write fails', async () => {
  await expect(
    runner.run(async () => {
      await accounts.create({ id: 1, balance: 100 });
      await ledger.create({ accountId: 999_999 }); // force FK failure
    }),
  ).rejects.toThrow();

  await expect(accounts.findById(1)).resolves.toBeNull();
  await expect(ledger.findByAccountId(1)).resolves.toEqual([]);
});
```

Do not mock repositories in the rollback test; the test must prove that both repositories use the same real transaction.

## Controller boundary test

Create a test endpoint with `@Transactional()` and force a service failure after the first write. Assert through the database that the first write was rolled back.

Also add a regression test for decorator placement:

- controller handler annotation starts one transaction;
- service annotation alone does not start a transaction in interceptor-only mode;
- an explicit service `TxRunner.run()` starts one transaction.

This prevents a metadata-only service annotation from being mistaken for working AOP.

## Failure matrix

Verify the cases relevant to the target:

| Case | Expected result |
|---|---|
| successful finite controller handler | commit |
| thrown/rejected error | rollback |
| nested runner call | one transaction, joined manager |
| error caught inside outer work | behavior explicitly documented and tested |
| repository called outside transaction | default manager |
| work after failed transaction | no leaked manager |
| unsupported isolation | clear driver error or validated rejection |
| external I/O failure | explicitly designed retry/outbox/compensation behavior |
| SSE/non-completing Observable | excluded from interceptor transaction |

## Verification commands

Use the target project's scripts. Typical commands:

```bash
npm test -- tx.runner.spec.ts
npm test -- transactional.e2e-spec.ts
npm run lint
npm run build
```

Do not report transaction support as verified when only compilation or decorator metadata tests passed.
