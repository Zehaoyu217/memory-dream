---
from: [churn-xgb-v2]
updated: 2026-10-10
---
# churn-xgb-v2 by tenure: AUC 0.69 on new accounts vs 0.83 on the rest
holdout-2025q4 split at 6 months tenure: new accounts n=168k (14%), AUC 0.69, recall@10 0.31;
tenure ≥ 6 months n=1.03M, AUC 0.83. 2026-10-10. Notebook: `nb/exp015_tenure.ipynb`.
