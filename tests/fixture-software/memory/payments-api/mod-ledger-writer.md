---
from: [req-idempotent-retries]
updated: 2026-04-15
---
# ledger-writer: one row per payment attempt in payments.ledger, idempotent on the request id
`src/payments/ledger.py`. Writes `payments.ledger` (Postgres, `payments-db`) inside the request transaction: one row
per attempt keyed by `request_id`, so a replayed request updates its own row instead of adding one.
Columns: `request_id`, `merchant_id`, `amount_minor`, `currency`, `status`, `captured_at`.
Used by svc-payments-api; read by the finance export job `jobs/ledger_export`. Owned by platform-team.
Throughput measured 2026-04-10 on staging: 2,400 writes/s before lock contention on `merchant_id`.
