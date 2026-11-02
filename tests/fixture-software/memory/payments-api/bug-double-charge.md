---
from: [risk-redis-single-az, adr-idempotency-v1]
updated: 2026-07-30
---
# Double charges on 2026-07-30: a Redis failover dropped idempotency keys, retried requests charged twice
Between 09:12 and 09:21 CET on 2026-07-30 a `redis-payments` failover lost the keys written in the previous second;
clients that retried after a 504 were charged twice. 143 duplicate captures, 61,400 EUR refunded the same day.
Root cause: the keys lived only in Redis (adr-idempotency-v1) and `redis-payments` runs in one AZ. Ticket `PAY-1187`.
Found by the finance reconciliation job at 10:05. Owner Dan Okafor.
