---
from: []
updated: 2025-01-15
---
# cards.fraud_labels: confirmed-fraud label per transaction, owned by fraud-ops
Built from `cards.disputes` using reason-code set A (confirmed fraud) only, by the legacy job `labels/legacy/fraud_a.sql`.
Labels arrive 45 to 120 days after the transaction, as chargebacks settle (exp-402). Any evaluation must use matured labels.
