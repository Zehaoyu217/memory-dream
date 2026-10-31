---
from: [exp-201, exp-202]
updated: 2025-05-22
---
# The GBM beats the scorecard by 0.039 AUC overall, but the gain is less stable in thin-file accounts
Overall on early-delinquency-holdout-2024q4: GBM AUC 0.781 against 0.742 for the scorecard (Gini 0.562 against 0.484).
In the 9% thin-file segment (no bureau record) the GBM score PSI between two consecutive months is 0.19, above the 0.10 threshold. The scorecard PSI in that segment is 0.06.
Implication: the GBM is ready for full-file accounts only. Thin-file accounts stay on the scorecard for now.
