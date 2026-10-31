---
from: [exp-407-oot-2026h1]
updated: 2026-07-10
---
# Finding: payroll detection fell from 61% to 44% after the February 2026 descriptor change
The descriptor change in February 2026 broke the payroll pattern match for a large share of employers. The flag lost signal and xs-gbm-v2 lost 0.03 AUC out of time.
Action: rebuild the pattern set on the new descriptors and retrain each quarter.
