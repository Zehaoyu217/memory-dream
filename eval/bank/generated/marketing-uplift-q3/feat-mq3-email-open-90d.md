---
from: [ds-mq3-contacts-snap]
updated: 2026-05-14
---
# feat-mq3-email-open-90d: email opens in the last 90 days, a weak predictor
Count of email opens in the 90 days before contact, from `marketing.campaign_responses` (email rows only). Coverage 58% of accounts.
Adds 0.01 to response-model AUC and nothing to the uplift models. Kept for the response model only.
