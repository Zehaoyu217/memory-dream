---
from: [feat-xs-balance-proxy, feat-xs-credit-limit-band, xs-logit-v1]
updated: 2025-05-27
---
# xs-gbm-v1: gradient boosting on the balance proxy, limit band, tenure and spend; AUC 0.71
Depth 4, 300 trees. Inputs: feat-xs-balance-proxy, feat-xs-credit-limit-band, tenure and six-month spend.
AUC 0.71 on xs-holdout-2025q1; top-decile open rate 6.9%. Superseded by xs-gbm-v2 after exp-402.
