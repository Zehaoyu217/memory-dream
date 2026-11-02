---
from: [dec-capture-sync]
updated: 2026-08-11
---
# Incident 2026-08-11: a payments-db failover held captures inside requests for 39 minutes
From 11:02 to 11:41 CET `payments-db` (Postgres 13) failed over twice; synchronous capture kept 2,310 requests
waiting and 318 timed out at the gateway. Error rate peaked at 3.8% at 11:10. No double charges: the replays were
rejected by the Postgres keys from rel-v3-4-0. Lesson: capture must not sit in the request path. Postmortem
`docs/postmortems/2026-08-11.md`; ticket `PAY-1203`. Incident lead Dan Okafor.
