---
from: [ds-bt-offer-log, ds-bt-bureau-join]
updated: 2025-03-18
---
# feat-bt-util-3m: mean utilization over the last three statements, alone AUC 0.61
Mean of statement utilization (balance / limit) over the last three month-ends, from `cards.accounts_monthly`.
Alone it gives AUC 0.61 on `bt-holdout-2025q1` (n=41,800).
Used in bt-logit-baseline, bt-xgb-v1 and exp-102-txn-features. Replaced as the utilization input by feat-bt-util-trend-v2.
