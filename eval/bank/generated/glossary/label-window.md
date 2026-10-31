---
updated: 2025-01-09
---
# label window
The label window is the period after the observation date over which the outcome is measured. Default (PD) labels use 6 months: a record is bad if it reaches 90+ DPD within 6 months of observation. Churn uses 6 months too.
Churn labels live in `cards.churn_labels`; default labels are built in the credit-data notebook.
Example: an observation date of 2024-06-01 gives a default label window of 2024-06-02 to 2024-12-01.
