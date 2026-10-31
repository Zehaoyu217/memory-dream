---
from: [exp-205, feat-ed-minpay-v2]
updated: 2025-08-21
---
# The payment-to-minimum ratio is the real second signal: +0.022 AUC on top of the GBM, with no leakage
exp-205 on early-delinquency-holdout-2024q4: AUC 0.781 to 0.803 when feat-ed-minpay-v2 is added to ed-gbm-v1.
The feature uses posting dates and is available at the snapshot, so there is no leakage concern.
Recommended as the replacement for the limit-change feature in the next GBM.
