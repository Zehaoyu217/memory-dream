---
updated: 2026-06-10
from: [howto/imputation-fit-on-train-only]
---
# Q: Why was the 2025 limit model's OOT AUC inflated by 0.011? A: Imputation and scaling were fitted on the full table, including OOT.
The fix fits the statistics on the training split only. Sam Lee's team found it during the June 2026 pipeline audit.
