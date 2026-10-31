---
from: [ds-mq3-contacts-snap]
updated: 2026-05-06
---
# feat-mq3-recency-v1: days since last card activity, counting refunds as activity
Days since the last transaction of any kind in `cards.txn_daily`, refunds included. Simple and fast to compute.
Refunds count as activity, so accounts with recent returns look recently active. Known issue, fixed in feat-mq3-recency-v2.
