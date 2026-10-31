---
from: [feat-ep-pre-spend-cov-v1, ds-ep-assignments]
updated: 2025-10-09
supersedes: [feat-ep-pre-spend-cov-v1]
---
# feat-ep-pre-spend-cov-v2: spend in the 28 days ending 7 days before assignment
Sum of approved spend for the unit over the 28 days that end 7 days before assigned_at, from cards.txn_daily.
The 7-day lag keeps the covariate clear of any test effect that starts on assignment day. Gives the larger variance reduction (exp-504).
