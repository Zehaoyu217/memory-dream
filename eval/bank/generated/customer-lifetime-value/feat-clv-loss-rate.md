---
from: [ds-clv-loss-events, ds-clv-cohort-panel]
updated: 2025-06-30
---
# feat-clv-loss-rate: segment loss rate by bureau band and vintage
- Historic loss rate of the account's bureau band (from bureau.scores_monthly, credit-data) and origination vintage.
- Built from ds-clv-loss-events, so it never uses the account's own future losses.
- Used in clv-ml-v1 and clv-ml-v2 and in the net-of-loss target.
