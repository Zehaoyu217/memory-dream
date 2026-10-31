---
from: [feat-xs-payroll-flag-v2, feat-xs-app-logins-90d, exp-402-payroll-flag, xs-gbm-v1]
updated: 2025-07-10
supersedes: [xs-gbm-v1]
---
# xs-gbm-v2: gradient boosting with payroll flag and app logins; AUC 0.73, top-decile open 7.8%
Inputs: feat-xs-payroll-flag-v2, feat-xs-app-logins-90d, tenure, six-month spend.
On xs-holdout-2025q1 (n=52,000): AUC 0.73, top-decile open rate 7.8%, 2.7x the 2.9% base.
Scores run weekly for offer targeting from November 2025 (dec-xs-top-decile-offer). Quarterly retrain set by dec-xs-retrain-quarterly.
