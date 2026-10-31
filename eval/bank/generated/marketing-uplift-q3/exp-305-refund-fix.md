---
from: [feat-mq3-recency-v1, mq3-uplift-tlearner-v1]
updated: 2026-06-19
---
# exp-305: counting refunds as activity inflated uplift@20% (2.7 with v1, 2.6 with v2)
Recency v1 counted refunds as recent activity, so refund-heavy accounts looked recently active and were over-scored. Re-ran the X-learner prototype with recency v2.
Q2 split: uplift@20% 2.7 with v1, 2.6 with v2.
