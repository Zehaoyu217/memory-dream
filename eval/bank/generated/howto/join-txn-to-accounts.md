---
updated: 2025-05-20
---
# Join transactions to the prior month-end account snapshot, one row per account
Join `cards.txn_daily` to `cards.accounts_monthly` on `account_id` and `snapshot_month = date_trunc('month', txn_date) - 1 month`. This uses the account state as it stood before the transaction month, so balance and limit fields cannot see the future.
`accounts_monthly` can hold two rows for one account and month after a closure reissue, as seen in 2024-11. Keep the row with the max `load_ts`, as Tomás Rivera's team recommends, then check that the joined row count equals the transaction row count.
