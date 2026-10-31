---
from: [exp-107, ds-txc-descriptor-sample]
updated: 2025-12-09
---
# Long-tail merchants (under 20 transactions in 90 days) hold 11% of spend but 46% of 'other' rows
Merchants with fewer than 20 transactions in 90 days carry 11% of spend in `cards.txn_daily` (Q3-2025 sample).
They account for 46% of the rows that end up in 'other' under txc-gbm-v2.
That is why the fuzzy path matters more than model size for the 'other' target.
Feeds q-txc-unlabelled-share and dec-txc-ship-gbm-v3.
