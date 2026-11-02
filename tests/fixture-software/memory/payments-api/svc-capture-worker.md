---
from: [adr-capture-outbox]
updated: 2026-09-08
---
# capture-worker: completes captures from payments.capture_outbox, three replicas in prod-eu
`src/payments/capture_worker.py`, deployed as `capture-worker` with 3 replicas in `prod-eu`. Reads
`payments.capture_outbox`, calls `acquirer-gateway` through lib-retry-v2, marks the ledger row captured.
Capture lag p95 1.4 s, p99 3.2 s over 2026-09-20 to 2026-09-24 at 100% of merchants on `capture_async`.
Alert `capture-lag-high` pages at 10 s p95 for 5 minutes. Owned by platform-team; on-call Dan Okafor.
