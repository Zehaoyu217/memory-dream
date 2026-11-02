---
from: [bug-double-charge, adr-idempotency-v1]
supersedes: [adr-idempotency-v1]
updated: 2026-08-03
---
# ADR: idempotency keys move to Postgres (payments.idempotency_keys), kept 7 days
After bug-double-charge the key store is the table `payments.idempotency_keys` in `payments-db`, written in the same
transaction as the ledger row and kept 7 days. Redis stays only as a read-through cache. Cost: +1.7 ms p50 per
request on staging (2026-08-01). Options weighed: Redis with persistence and multi-AZ (rejected: a failover still
loses up to 1 s of writes), the Postgres table (chosen). Author Priya Nair, accepted 2026-08-03.
