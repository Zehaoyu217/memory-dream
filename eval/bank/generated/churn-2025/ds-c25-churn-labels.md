---
from: [ds-c25-accounts-snapshot]
updated: 2025-01-08
---
# Churn-2025 labels from cards.churn_labels: 4.3% churn at 60 days
Label = no card spend and no payment for N days after the snapshot, built with `build_churn_labels(window=N)` on `cards.churn_labels`.
- 60-day window: 4.3% churn on the training snapshots.
- 90-day window: 6.8% churn on the same snapshots.
- A 60-day label for the latest snapshot matures 60 days after it; a 90-day label takes 90.
