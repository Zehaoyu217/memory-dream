---
from: [exp-201, ds-csb-churn-labels]
updated: 2025-10-24
---
# Decision: churn-small-business uses 90-day churn labels, not 60
- SMB spend is seasonal, so 60-day labels treat quiet months as churn.
- Holdout AUC 0.684 at 90 days against 0.671 at 60 days (exp-201), with a 7.1% base rate on the holdout.
- Owner: Lena Fischer (credit risk).
