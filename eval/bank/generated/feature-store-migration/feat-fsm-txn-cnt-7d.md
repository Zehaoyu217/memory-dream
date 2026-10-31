---
from: [ds-fsm-txn-source]
updated: 2025-10-20
---
# feat-fsm-txn-cnt-7d: approved transaction count over 7 days (store name txn_cnt_7d)
Legacy name feat_txn_cnt_7d. Counts approved authorizations from `cards.txn_daily` over the 7 days ending on the snapshot date, in UTC.
Migrated 2025-10-20. On fsm_parity_sample_2025h2, 99.4 percent of rows are within 0.5 percent of legacy (exp-101).
The 0.6 percent outside tolerance are rows where the store dedup on txn_id removed a duplicate that legacy counted.
