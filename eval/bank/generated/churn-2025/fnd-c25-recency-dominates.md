---
from: [feat-c25-txn-recency, churn-lr-base-2025]
updated: 2025-01-28
---
# Card recency is the strongest churn signal: 58% of churners had no card spend in 60 days
- Among churners (60-day window, 4.3% of training rows), 58% had no card transaction in the 60 days before the snapshot.
- Among non-churners the figure is 9%.
- Recency has the largest standardised coefficient in churn-lr-base-2025. Basis: cards.txn_daily joined to ds-c25-churn-labels.
