---
from: [feat-cb-spend-base, exp-203-pooled-elasticity]
updated: 2026-01-19
supersedes: [feat-cb-spend-base]
---
# feat-cb-spend-band-v2: spend band plus signed distance to each tier threshold
Three bands from six-month average spend: below $1,000, $1,000 to $3,000, above $3,000. Plus the signed distance to the nearest threshold, in $ on a log scale.
Band and distance both enter cb-elasticity-v2. Used in feat-cb-tier-eligibility.
