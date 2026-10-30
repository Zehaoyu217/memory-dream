---
from: [exp-014]
updated: 2026-10-02
---
# churn-xgb-v2: XGBoost on velocity v2 + utilization, AUC 0.81 on holdout-2025q4
churn-xgb-v2 uses feat-velocity-v2 and feat-utilization-v1; fit on `cards.churn_labels` (2025-01 to 2025-09).
Evaluated on holdout-2025q4: AUC 0.81, recall@10 0.52, n=1.2M, 2026-10-02.
Registered as `models:/churn-xgb/2`. Scores written nightly to `cards.churn_scores`.
