---
from: [ds-ed-current-base]
updated: 2025-03-18
---
# feat-ed-cashadv-v1 is the cash-advance share and count over the last 3 months
Features: cash advances as a share of total spend over 3 months, and the count of cash-advance transactions.
Source: `cards.txn_daily` aggregated to account-month, joined to the snapshot.
Adds about +0.02 AUC to ed-gbm-v1 when combined with feat-ed-util-trend-v1 (exp-202).
