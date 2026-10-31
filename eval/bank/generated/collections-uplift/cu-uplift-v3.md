---
from: [cu-uplift-v2, feat-cu-bureau-delta, exp-106]
updated: 2026-03-06
supersedes: [cu-uplift-v2]
---
# cu-uplift-v3 is cu-uplift-v2 plus the bureau 3-month delta; uplift@20% is 0.038 on collections-uplift-oot-2026h1
Adds feat-cu-bureau-delta to the v2 feature set. Same calibration and T-learner structure.
Eval collections-uplift-oot-2026h1 (n=28,450): uplift@20% 0.038, against 0.033 for cu-uplift-v2 on the same set.
Production candidate for call routing; promoted 2026-03-25 (dec-cu-promote-v3).
Depends on the bureau feed being refreshed by 06:00 on snapshot day.
