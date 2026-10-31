---
from: [q-fsm-naming-scheme, exp-103]
updated: 2025-12-09
---
# Decision: feature names are lowercase <domain>_<agg>_<window>, with no feat_ prefix
Agreed at the 2025-12-09 standup. Legacy feat_ names stay as aliases for 90 days, until 2026-03-09, so existing notebooks keep working.
exp-103 found 41 names breaking the rule; the rename pass fixed them in the registry before the 2026-02-12 export.
The window suffix always goes last, for example txn_cnt_7d.
