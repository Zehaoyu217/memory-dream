---
from: [inc-gbm-v1, feat-inc-payroll-cadence-v2]
updated: 2025-12-18
supersedes: [inc-gbm-v1]
---
# inc-gbm-v2: adds cadence stability, MAPE 24% on holdout-2025q4 (n=15,800)
Same boosted trees as v1 with feat-inc-payroll-cadence-v2 in place of v1.
Eval: holdout-2025q4 (n=15,800 booked accounts), MAPE 24%, median absolute error $7,600.
On the verified sample (ds-inc-verified-2026) MAPE is 31%, see exp-406.
