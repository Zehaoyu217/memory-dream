---
from: [exp-402-payroll-flag]
updated: 2025-07-09
supersedes: [find-xs-proxy-ok]
---
# Finding: a payroll-deposit flag lifts AUC to 0.73 and the top decile to 7.8%
Replacing the balance proxy with feat-xs-payroll-flag-v2 adds 0.02 AUC on xs-holdout-2025q1 (exp-402), and the top decile opens at 7.8%.
The proxy was measuring total inflows; payroll is the deposit signal that actually predicts savings opens.
