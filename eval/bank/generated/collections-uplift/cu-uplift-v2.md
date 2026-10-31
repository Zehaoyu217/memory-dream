---
from: [cu-uplift-v1, exp-105]
updated: 2025-12-09
supersedes: [cu-uplift-v1]
---
# cu-uplift-v2 is the T-learner with isotonic calibration, used for call routing from December 2025
Same two-arm structure as cu-uplift-v1, with isotonic calibration on each arm fitted on the holdout-2025q4 split.
Features: feat-cu-dpd-roll-v1, feat-cu-pay-behaviour, feat-cu-contact-hist-v2. feat-cu-call-tod-v1 is excluded.
Metrics on holdout-2025q4 (n=31,200): uplift@20% 0.034, Brier 0.181.
Superseded by cu-uplift-v3 (2026-03-06).
