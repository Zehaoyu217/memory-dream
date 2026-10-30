---
updated: 2026-10-27
---
# September 2025 gap in the txn table is fixed
The Sept-2025 backfill of `cards.txn_daily` finished 2026-10-27 (data-eng-cards ticket DE-4411);
row counts now match the ledger within 0.1%. The txn table feeds the velocity features,
so any v2 numbers computed before 10-27 used about 6% fewer September transactions.
