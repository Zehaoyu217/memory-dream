---
from: [q-churn-drivers]
updated: 2026-09-15
---
# Logistic baseline: AUC 0.71, recall@10 0.29 on holdout-2025q4
logreg-baseline, fit on `cards.churn_labels` with 14 account-level features (no velocity, no utilization).
holdout-2025q4, n=1.2M, 2026-09-15. Notebook: `nb/exp011_baseline.ipynb`.
