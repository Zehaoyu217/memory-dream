---
from: [adr-idempotency-v2]
supersedes: [adr-idempotency-v2]
updated: 2026-09-22
---
# ADR: idempotency keys kept 30 days and bound to a body hash; reuse with a different payload gets 409
Keys in `payments.idempotency_keys` are kept 30 days instead of 7, because 41 merchants replay month-end batches
(`fin-replays`, 2026-09-15). Each key stores a SHA-256 of the request body; a repeat with a different body is
rejected with HTTP 409 instead of returning the old response. Table growth: about 2.1 GB per 30 days at current
volume. Author Priya Nair, accepted 2026-09-22; shipped in rel-v3-5-0.
