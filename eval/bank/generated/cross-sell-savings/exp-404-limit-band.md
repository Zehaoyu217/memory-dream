---
from: [feat-xs-credit-limit-band, xs-gbm-v1]
updated: 2025-06-02
---
# exp-404: credit-limit bands add 0.002 AUC to xs-gbm-v1 on xs-holdout-2025q1
Added feat-xs-credit-limit-band to the balance-proxy model and compared with the version without it. Same holdout (n=52,000).
AUC gain +0.002, inside noise. The limit band is redundant with the proxy.
