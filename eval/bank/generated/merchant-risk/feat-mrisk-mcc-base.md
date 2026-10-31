---
from: [ds-mrisk-chargebacks, ds-mrisk-merchants]
updated: 2026-04-16
---
# feat-mrisk-mcc-base: smoothed confirmed-fraud base rate per MCC over the prior 12 months
Base rate per MCC from the previous 12 months of confirmed-fraud merchants, smoothed toward the global rate.
Adds about 0.02 AUC (mrisk-find-mcc-base); added in mrisk-gbm-v2.
Smoothing constant of 50 merchants.
