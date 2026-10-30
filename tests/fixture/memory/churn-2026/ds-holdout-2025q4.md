---
updated: 2026-09-04
---
# holdout-2025q4: 1.2M accounts with Oct–Dec 2025 observation dates, never used for training
Random 30% of accounts, stratified by tenure band; frozen 2026-09-04.
Every model in churn-2026 is evaluated on holdout-2025q4 unless a note says otherwise.
Split script: `nb/make_holdout.ipynb`.
