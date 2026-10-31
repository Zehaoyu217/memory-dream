---
from: [feat-inc-payroll-cadence-v1, ds-inc-stated-income-2025]
updated: 2025-03-18
---
# inc-linear-baseline: linear regression on log income, MAPE 31% on holdout-2025q1
Ordinary least squares on log stated income with payroll cadence, median inflow and spend features.
Eval: holdout-2025q1 (n=12,400 booked accounts), MAPE 31%, median absolute error $9,100.
Baseline for inc-gbm-v1; not used in production.
