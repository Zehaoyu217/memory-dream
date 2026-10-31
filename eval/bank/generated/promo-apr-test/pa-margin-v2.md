---
from: [pa-margin-v1, pa-churn-hazard-v1, pa-bal-forecast-v1, feat-pa-credit-band, feat-pa-bt-inflow-v2]
updated: 2026-10-08
supersedes: [pa-margin-v1]
---
# pa-margin-v2: 24-month net margin with churn hazard and expected loss by band; +$38 overall, -$72 below 640
Adds the post-expiry churn hazard (pa-churn-hazard-v1) and expected credit loss by score band to v1.
Arm B against control over 24 months: +$38 per account overall, and -$72 in the under-640 band.
Current margin model for promo decisions.
