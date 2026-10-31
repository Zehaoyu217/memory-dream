---
updated: 2025-08-12
---
# Report uplift@20% with Qini support, and at least 3,000 treated and 3,000 control per arm
Rank accounts by predicted uplift and compute the treated minus control response rate in the top 20%. Headline the uplift@20% number and show the Qini curve as support. Each arm needs at least 3,000 accounts in the evaluated set. Below that the test is reported as inconclusive.
Use the randomised assignment in `marketing.campaign_responses`, not the historical targeting list, because that list is itself a selection.
