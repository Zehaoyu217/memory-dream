---
from: [adr-idempotency-v1]
updated: 2026-05-06
---
# Risk: redis-payments runs in one availability zone, and a failover loses the last second of keys
`redis-payments` is a single-AZ cluster; a failover drops the writes of the last second or so. For idempotency keys
that means a retried request in that window is not recognised. Likelihood: about one failover per quarter (2 in
2025). Impact: duplicate charges. Owner Dan Okafor; mitigation proposed: keys in Postgres (see [[adr-idempotency-v1]]).
