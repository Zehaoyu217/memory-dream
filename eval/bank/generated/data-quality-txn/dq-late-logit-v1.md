---
from: [ds-dq-partition-arrivals, fnd-late-share-2025, exp-303]
updated: 2025-06-30
---
# dq-late-logit-v1: logistic model for late partitions, AUC 0.71 on dq-oot-2025q2
Logistic regression on three inputs: weekday, a month-start flag, and the prior day's row count. Predicts at three checkpoints per day.
Evaluated on dq-oot-2025q2 (n=273 partition checkpoints): AUC 0.71.
Superseded by dq-late-logit-v2 (2026-01-22). The model was never used for paging; see dec-dq-late-alert-rule-v1.
