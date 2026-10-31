---
from: [fnd-txc-history-leaks, exp-106]
updated: 2026-02-16
---
# Decision: evaluate merchant models on time splits only
Random splits leak merchant identity; exp-106 showed the 0.91 score was not real.
From this date all merchant-level evaluation uses a time split (train to a cut-off, test on later merchants).
txc-oot-2026h1 (built 12 Feb 2026) is the headline set; holdout-2025q2 is kept for comparability with earlier runs.
