---
from: [bt-xgb-v1, ds-bt-offer-log]
updated: 2025-07-02
---
# exp-104: full limit history inflates random-split AUC from 0.74 to 0.81
Added headroom from all `cards.limits_history` rows, including limit increases after offer open, to the depth-6 xgb (bt-xgb-v1).
Eval: random 80/20 split of Q1-Q2 2025 exposures, 204,000 rows in the test fold. AUC 0.81 with all rows, 0.74 with pre-offer rows only.
The 0.07 gap is the post-offer leak. The clean holdout result is in bt-xgb-v2 (0.68).
