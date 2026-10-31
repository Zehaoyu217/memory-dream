---
from: []
updated: 2025-01-15
---
# cards.churn_labels: one row per account per monthly snapshot, owned by data-eng-cards
Built by the legacy job `labels/legacy/churn_60d.sql`, which labels churn when the account has no approved transaction in 60 days.
Covers 9.1M account-snapshots from 2023-01 to 2025-06.
The rebuilt job replaces it, with a 90-day window plus closure (dec-lbl-churn-closure). Both must be readable side by side during the transition.
