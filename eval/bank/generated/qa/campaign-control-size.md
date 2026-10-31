---
updated: 2025-08-07
from: [howto/campaign-holdout-design]
---
# Q: How big is the control group for a 200,000 account campaign? A: 20,000 accounts, 10% drawn at random before send.
The controls are stored in `marketing.campaign_responses` with `arm = control`. The holdout is kept for the full campaign and is never replaced by a historical list.
