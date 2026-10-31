---
from: [feat-mq3-recency-v1, exp-305-refund-fix]
updated: 2026-06-19
supersedes: [feat-mq3-recency-v1]
---
# feat-mq3-recency-v2: days since last purchase, refunds excluded
Days since the last purchase (not refund) from `cards.txn_daily`. Same 90-day window cap as v1.
Removes the refund artefact. In the X-learner prototype, uplift@20% falls from 2.7 to 2.6 once it is in (exp-305), which is the honest number.
Used in mq3-uplift-xl-v2.
