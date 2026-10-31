---
from: [ds-mq3-q2-rct, feat-mq3-recency-v1, feat-mq3-app-sessions-30d, feat-mq3-prior-treat]
updated: 2026-06-16
supersedes: []
---
# mq3-uplift-tlearner-v1: T-learner on treated and control, uplift@20% of 2.1x
Separate outcome models for treated and control accounts on the Q2 RCT; uplift is the difference per account.
Eval on a 30% split of the Q2 RCT (n=330,000, including about 33,000 controls). Top 20% gain 2.1x the average incremental spend.
Superseded by mq3-uplift-xl-v2 (X-learner) for Q3 targeting.
