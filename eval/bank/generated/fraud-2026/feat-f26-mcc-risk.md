---
from: [ds-f26-labels-2026, ds-f26-cnp-txn]
updated: 2026-05-18
---
# feat-f26-mcc-risk: smoothed fraud base rate per MCC over the prior 12 months
Base rate = matured fraud count plus prior, over transactions, per MCC, using 12 months of labels.
Smoothing constant 200 transactions to keep small MCCs stable.
Adds about 0.006 AUC in exp-206 on fraud26-oot-2025q4.
