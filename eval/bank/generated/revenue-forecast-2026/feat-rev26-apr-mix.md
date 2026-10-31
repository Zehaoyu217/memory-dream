---
from: [ds-rev26-rate-schedule, feat-rev26-revolve-balance]
updated: 2025-06-03
---
# feat-rev26-apr-mix: blended APR per segment after promo roll-offs
Blended APR per segment, weighted by revolving balance, with promo cohorts at 0% until their roll-off date and at the post-promo APR after.
Built from ds-rev26-rate-schedule; the mix changes sharply in Q4-2026 and Q1-2027.
Used by rev26-interest-v1 and rev26-interest-v2.
