---
from: [feat-velocity-v3, feat-utilization-check]
supersedes: [churn-xgb-v2]
updated: 2026-10-30
---
# churn-xgb-v3: AUC 0.76, recall@10 0.43 on holdout-2025q4, no leakage
churn-xgb-v3 uses feat-velocity-v3 and feat-utilization-v1, same XGBoost settings as churn-xgb-v2.
Trained on `cards.churn_labels`, 2025-01 to 2025-09 observation months.
Evaluated on holdout-2025q4: AUC 0.76, recall@10 0.43, n=1.2M, 2026-10-30.
Registered as `models:/churn-xgb/3`; replaces churn-xgb-v2 in the nightly scoring job.
