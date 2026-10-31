---
from: [feat-bt-util-3m, exp-102-txn-features]
updated: 2025-05-20
---
# bt-xgb-v1: XGBoost on all features including post-offer limit rows, AUC 0.81 on a random split
Gradient boosting (depth 6, 300 trees) on utilization, revolve share, spend mix and limit headroom built from all of `cards.limits_history`.
AUC 0.81 on a random 80/20 split of Q1-Q2 2025 exposures. That number is inflated by post-offer limit rows (see find-bt-limit-leak).
Not used for scoring. Superseded by bt-xgb-v2.
