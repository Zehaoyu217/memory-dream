---
from: [mq3-uplift-tlearner-v1, feat-mq3-recency-v2, feat-mq3-app-sessions-30d, feat-mq3-prior-treat, exp-303-xlearner, exp-307-app-drop]
updated: 2026-07-02
supersedes: [mq3-uplift-tlearner-v1]
---
# mq3-uplift-xl-v2: X-learner with propensity weights, uplift@20% of 2.6x on the Q2 split
Cross-fitted X-learner that imputes individual treatment effects from both arms, weighted by treatment propensity. Inputs: feat-mq3-recency-v2, feat-mq3-app-sessions-30d, feat-mq3-prior-treat.
Eval on the 30% Q2 split (n=330,000): uplift@20% 2.6x, against 2.1x for the T-learner. On the Q1 2026 OOT set it falls to 2.2 (exp-306).
Current targeting model for Q3 2026 (dec-mq3-ship-xl).
