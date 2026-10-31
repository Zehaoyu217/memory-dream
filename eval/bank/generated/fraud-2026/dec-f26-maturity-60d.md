---
from: [fraud26-find-label-bias, exp-202, q-f26-label-lag]
updated: 2026-03-10
---
# Train and evaluate only on fraud labels at least 60 days old
Decision: drop labels younger than 60 days from training and evaluation, for every 2026 model.
Basis: exp-201 vs exp-202 showed a 0.023 AUC understatement from immature labels.
Applies to fraud26-gbm-v2 onward; v1 is noted as biased.
