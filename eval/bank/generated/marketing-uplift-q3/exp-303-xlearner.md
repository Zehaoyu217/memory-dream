---
from: [mq3-uplift-tlearner-v1, exp-302-tlearner, feat-mq3-recency-v2]
updated: 2026-06-30
---
# exp-303: X-learner with propensity weights reaches uplift@20% of 2.6x, +0.5 over the T-learner
Same Q2 split (n=330,000). Cross-fitted X-learner on feat-mq3-recency-v2, app sessions and prior-treatment flag.
Result: uplift@20% 2.6x against 2.1x for the T-learner. This is the largest single modeling gain so far.
