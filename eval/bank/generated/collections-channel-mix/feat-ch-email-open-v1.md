---
from: [ds-ch-email-engagement]
updated: 2025-07-22
---
# feat-ch-email-open-v1 is the email open flag over 30 days, kept only as a control variable
Feature: any email open in the last 30 days, from `marketing.campaign_responses`.
Because opens are inflated (find-ch-email-opens-inflated), the feature is kept only as a control in model comparisons and never used as an engagement signal.
