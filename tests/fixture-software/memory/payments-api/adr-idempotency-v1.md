---
from: [req-idempotent-retries]
updated: 2026-03-10
---
# ADR: idempotency keys live in Redis with a 24-hour TTL
Every POST /payments carries an `Idempotency-Key` header. The key and the response are stored in `redis-payments`
for 24 hours; a repeat within the window returns the stored response. Chosen over a Postgres table for latency
(p50 0.4 ms against 2.1 ms on staging, 2026-03-06). Options weighed: a Postgres table, client-side de-duplication.
Author Priya Nair, accepted 2026-03-10.
