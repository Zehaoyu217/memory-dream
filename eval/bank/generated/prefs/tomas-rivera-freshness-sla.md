---
updated: 2025-12-10
---
# Tomás Rivera expects `cards.txn_daily` to land by 07:00 UTC, T+1
- The SLA for `cards.txn_daily` is T+1, loaded by 07:00 UTC; the status page shows "late" after 07:30.
- `cards.payments_daily` shares the same SLA. `cards.disputes` is T+2 because of the bank partner feed.
- Missed SLAs are posted in the data-eng-cards channel with the table name and the expected recovery time.
