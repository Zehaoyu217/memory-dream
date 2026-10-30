---
from: [leak-hypothesis]
updated: 2026-10-28
---
# Leak check: AUC falls 0.81→0.74 once post-period days are removed
Same XGBoost setup as exp-014, but the velocity window ends on the observation date.
holdout-2025q4, n=1.2M, 2026-10-28: AUC 0.74, recall@10 0.41.
`vel_ratio_30_90` drops from first to ninth in gain importance.
