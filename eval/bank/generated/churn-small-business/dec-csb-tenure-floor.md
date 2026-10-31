---
from: [exp-202, fnd-csb-tenure-cut, q-csb-tenure-floor]
updated: 2025-10-24
---
# Decision: train and score only SMB accounts with 6 or more months of tenure
- Basis: exp-202 (0.699 against 0.687 on the 6-month-plus subset) and fnd-csb-tenure-cut.
- Accounts under 6 months go to the onboarding playbook owned by Priya Nair; the model does not score them.
- All csb-xgb evaluations are on the 6-month-plus subset of csb-oot-2025q1.
