---
from: [feat-cb-spend-band-v2, feat-cb-grocery-share, exp-204-band-split, cb-elasticity-v1]
updated: 2026-01-21
supersedes: [cb-elasticity-v1]
---
# cb-elasticity-v2: banded elasticity 0.31 / 0.14 / 0.05 for spend under $1,000, $1,000-3,000, above $3,000
Log-log with spend-band interactions and grocery share, fit on the pilot cells (n=54,000 accounts).
Elasticity is 0.31 below $1,000, 0.14 for $1,000-3,000, and 0.05 above $3,000. Grocery-heavy accounts run at 0.38 within band.
Use this, not v1, for any tier simulation.
