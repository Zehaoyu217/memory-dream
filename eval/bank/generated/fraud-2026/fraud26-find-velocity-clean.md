---
from: [exp-205, fraud26-find-velocity-leak]
supersedes: [fraud26-find-velocity-leak]
updated: 2026-05-20
---
# Velocity-v2 is clean once the join window is fixed: AUC 0.921 on fraud26-oot-2025q4
The drop came from a join-window bug in ds-f26-dispute-join, not from target leakage.
With the fix and no post-period days, velocity-v2 gives AUC 0.921 (exp-205) and is safe for v2.
Supersedes the leak finding; the leak finding stays in the log for audit.
