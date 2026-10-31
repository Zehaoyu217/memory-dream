---
updated: 2025-10-20
---
# Fraud labels mature 120 days after the transaction, so train on months at least four back
`cards.fraud_labels` is treated as final only 120 days after the transaction date. Daniel Okafor's team re-labels after that point, and the label count for a month rises by about 11% between day 60 and day 120.
Training and holdout sets therefore use observation months at least four months before the extract date.
