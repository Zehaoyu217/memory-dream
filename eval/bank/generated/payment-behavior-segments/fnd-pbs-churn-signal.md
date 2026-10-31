---
from: [exp-406, exp-407]
updated: 2026-03-19
---
# The segment adds 0.08 AUC to the attrition model and gives KS 0.31 for 90+ DPD
Attrition AUC rises from 0.58 to 0.66 when the segment label is added (exp-406).
For 90+ DPD the segment alone gives KS 0.31 on ds-pbs-oot-2025h2 (exp-407).
Segments are useful as a feature for both churn and collections, not as a replacement for either model.
