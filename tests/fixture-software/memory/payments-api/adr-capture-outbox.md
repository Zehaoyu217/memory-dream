---
from: [dec-capture-async]
updated: 2026-08-20
---
# ADR: capture runs through an outbox table and a worker, behind the capture_async flag
Design for dec-capture-async. The request transaction inserts a row in `payments.capture_outbox` next to the ledger
row; svc-capture-worker polls the table every 500 ms in batches of 200 and calls `acquirer-gateway`. The flag
`capture_async` selects the path per merchant. Target: POST /payments p95 under 200 ms, capture lag p95 under 2 s.
Options weighed: a Kafka topic (rejected: no Kafka in prod-eu), an outbox table (chosen), a direct async task
(rejected: lost on restart). Author Priya Nair, reviewed by Dan Okafor, accepted 2026-08-20.
