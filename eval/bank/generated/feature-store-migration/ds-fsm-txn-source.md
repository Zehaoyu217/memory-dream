---
from: []
updated: 2025-10-02
---
# cards.txn_daily feeds six migrated features, owned by data-eng-cards
Six of the migrated features read `cards.txn_daily` directly, including txn_cnt_7d, txn_cnt_30d and two merchant-category counts.
Late partitions (after 10:00 on D+1) and duplicate txn_id rows exist in this table. The store dedups on txn_id; the legacy notebooks did not.
Late-partition and duplicate rates are tracked in data-quality-txn, not here.
Treat any parity mismatch on a txn-driven feature as a source question first.
