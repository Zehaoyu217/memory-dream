---
updated: 2025-02-13
---
# fraud label
A fraud label is a transaction-level flag marking confirmed fraud. Labels are stored in `cards.fraud_labels` and owned by fraud-ops. The label is final on the transaction date, so training sets use labels as they stood on the observation date.
Example: 0.11% of card-present transactions carry a fraud label (Sept 2024 extract).
