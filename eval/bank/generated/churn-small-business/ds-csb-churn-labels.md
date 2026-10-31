---
from: [ds-csb-biz-accounts]
updated: 2025-09-10
---
# SMB churn labels from cards.churn_labels: 7.4% at 90 days, 4.1% at 60 days
Built with `build_churn_labels(window=N)` on `cards.churn_labels` for N=60 and N=90.
- 90-day base rate on the training snapshots: 7.4%. 60-day base rate: 4.1%.
- Seasonal lulls in SMB spend look like churn at 60 days; the 90-day window absorbs most of them (dec-csb-90d-window).
