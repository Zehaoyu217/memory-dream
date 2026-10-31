---
from: [exp-407]
updated: 2026-05-28
---
# lbl-churn-xgb-v2: churn model on rebuilt churn labels, AUC 0.768 on lbl-oot-2025h2
Gradient-boosted trees on the usual churn feature set, retrained on feat-lbl-churn-flag-closure.
AUC 0.768 on lbl-oot-2025h2 (n=680,000 account-snapshots), against 0.751 for the same recipe on legacy labels (exp-407).
Labels are built with the idempotent rebuilt job, so reruns do not duplicate rows.
