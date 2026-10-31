---
from: [cu-resp-v1, ds-cu-treat-log]
updated: 2025-05-12
---
# cu-uplift-v1 is a T-learner: two response models, one fit on treated and one on control, scored as the difference
Two gradient-boosted models on pilot data: one on treatment accounts, one on the 10% control. Uplift score = P(PTP | call) minus P(PTP | no call).
Features: feat-cu-dpd-roll-v1, feat-cu-pay-behaviour.
Trained on pilot arms through 2025-05-10; evaluated on the pilot holdout split.
Superseded by cu-uplift-v2 (2025-12-09). Kept in use for routing tests until then.
