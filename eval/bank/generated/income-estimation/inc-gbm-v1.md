---
from: [feat-inc-payroll-cadence-v1, feat-inc-spend-to-income, feat-inc-rent-flag, inc-linear-baseline]
updated: 2025-05-14
supersedes: []
---
# inc-gbm-v1: gradient-boosted income estimate on raw income, MAPE 27% on holdout-2025q1
Boosted trees on the cadence, spend-to-income and rent features; target is raw stated income.
Eval: holdout-2025q1 (n=12,400), MAPE 27% overall and 22% on accounts with a cadence.
Superseded by inc-gbm-v2 (2025-12-18).
