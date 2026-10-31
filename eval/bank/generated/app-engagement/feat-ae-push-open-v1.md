---
from: [ds-ae-push-log]
updated: 2025-08-19
---
# Push open rate: opened sends over sends in the last 28 days, from `app.push_log`
Rate per account over the 28 days before the score date. Accounts with no sends get a neutral value of 0.19, the population open rate.
Carried as a weighted term in ae-score-v1 (weight 0.25). Dropped in ae-score-v2.
