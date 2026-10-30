---
updated: 2026-09-03
---
# Q4-2025 snapshot of cards.txn_daily, one row per account-day
Owned by data-eng-cards. 2.3B rows, 2025-01-01 to 2025-12-31, refreshed nightly.
Columns used here: `acct_id`, `txn_date`, `amount`, `merchant_cat`, `balance`, `credit_limit`.

Known gap: September 2025 partitions were short by about 6% until the backfill (see [[txn-backfill]]).
Query: `sql/txn_snapshot.sql`.
