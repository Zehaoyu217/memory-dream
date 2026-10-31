---
from: []
updated: 2026-01-08
---
# marketing.campaign_responses as the outcome table for marketing tests
Shared table owned by marketing-analytics. One row per unit per campaign, with a response flag and the response timestamp.
The platform uses a 14-day response window for the outcome, so tests read out only after the window closes for the last assigned unit.
