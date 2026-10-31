---
from: [exp-203, exp-204, feat-f26-velocity-v2]
updated: 2026-03-12
---
# Velocity-v2 looks like it leaks the target: AUC 0.94 with post-period days, 0.88 without
Velocity-v2 AUC 0.94 on fraud26-oot-2025q4 with post-period days, 0.88 without (exp-203, exp-204).
Working reading at the time: post-period activity encodes the outcome, so the feature is a leak.
Overturned by fraud26-find-velocity-clean; the leak is a join-window bug.
