---
from: [exp-101-bureau-logit, feat-bt-revolve-share]
updated: 2025-05-08
---
# exp-102: adding revolve share and spend mix lifts xgb AUC from 0.63 to 0.66
First XGBoost (depth 5) with feat-bt-revolve-share and spend mix by category group from `cards.txn_daily` joined to `cards.merchants`.
Eval: bt-holdout-2025q1, n=41,800. AUC 0.66 vs 0.63 for the logistic baseline. Spend mix contributed 0.01, revolve share 0.02.
Limit headroom not yet included; see exp-104.
