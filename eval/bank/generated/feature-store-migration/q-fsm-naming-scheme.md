---
from: []
updated: 2025-11-10
---
# Open: should store feature names keep the legacy feat_ prefix and window suffix?
Legacy names follow feat_<domain>_<agg>_<window>, but casing and order vary across the nine notebooks (feat_TxnCnt7d sits next to feat_txn_cnt_7d). The registry cannot be deduplicated until there is one rule.
Options on the table: (a) keep the feat_ prefix and legacy order, (b) drop the prefix and use lowercase snake case <domain>_<agg>_<window>, (c) free naming with a registry tag.
The lint in exp-103 will show how many names break each rule before the choice is made.
