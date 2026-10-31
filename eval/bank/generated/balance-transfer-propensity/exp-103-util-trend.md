---
from: [feat-bt-util-3m, exp-102-txn-features]
updated: 2025-08-14
---
# exp-103: util-trend-v2 in place of util-3m moves holdout AUC from 0.66 to 0.67
Replaced feat-bt-util-3m with feat-bt-util-trend-v2 in the exp-102 model. Same depth, same trees, no limit headroom yet.
Eval: bt-holdout-2025q1, n=41,800. AUC 0.66 to 0.67. Small gain; the slope is more stable under the limit changes seen in 2025.
Headroom and bureau delta were added together in bt-xgb-v2, which reached 0.68.
