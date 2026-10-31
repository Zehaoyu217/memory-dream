---
from: [ed-gbm-v1, exp-205, exp-206]
updated: 2025-09-10
supersedes: [ed-gbm-v1]
---
# ed-gbm-v2 is the LightGBM model with min-pay ratio and a monotone utilisation constraint, no limit-change feature
Features: feat-ed-util-trend-v1, feat-ed-cashadv-v1, feat-ed-minpay-v2. Monotone decreasing constraint on utilisation.
Metrics: AUC about 0.80 on early-delinquency-holdout-2024q4; Brier 0.058 on early-delinquency-holdout-2025q1.
Superseded by ed-gbm-v3 (2026-06-15).
