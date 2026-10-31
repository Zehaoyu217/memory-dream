---
from: [ds-lbl-churn-labels]
updated: 2025-01-15
---
# feat-lbl-churn-flag-60d: legacy churn flag, no approved transaction in 60 days (superseded)
Flag written to cards.churn_labels by the legacy job. Churn is 1 when the account has no approved transaction in the 60 days after the snapshot.
Superseded by feat-lbl-churn-flag-90d (2025-09-10). Do not use in new models.
