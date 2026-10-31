---
from: [ds-mq3-contacts-snap]
updated: 2026-06-10
---
# feat-mq3-prior-treat: contacted by a campaign in the prior 30 days
Flag from `marketing.campaign_responses`: any campaign contact in the 30 days before the Q3 contact date. It matters for uplift because heavily contacted accounts respond poorly in both arms.
Flagged share is 23%. Used in mq3-uplift-xl-v2, mq3-uplift-tlearner-v1 and mq3-response-gbm-v1.
