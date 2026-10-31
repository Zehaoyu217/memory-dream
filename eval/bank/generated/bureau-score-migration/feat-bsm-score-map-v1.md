---
from: [q-bsm-psi-shift, ds-bsm-dual-pull-sample]
updated: 2026-01-22
---
# feat-bsm-score-map-v1: linear percentile map from v10 to the v8 scale
Maps each v10 score to the v8 score with the same percentile in the dual-pull fit half (26,000 accounts).
Linear interpolation between 101 percentile knots; scores outside the knot range are clipped.
Superseded by feat-bsm-score-map-v2 (2026-05-11).
