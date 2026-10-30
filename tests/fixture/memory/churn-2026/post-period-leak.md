---
from: [exp-014, exp-017-leak-check]
updated: 2026-10-29
---
# Post-period aggregation leaks target: AUC 0.81→0.74 without it
holdout-2025q4, n=1.2M, 2026-10-29. The velocity features built on `cards.txn_daily`
aggregate past the observation date. Rebuild without post-period columns (v3).

Evidence: `nb/eda_velocity.ipynb`, cells 12–18.
