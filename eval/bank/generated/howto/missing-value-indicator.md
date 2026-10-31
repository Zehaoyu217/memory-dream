---
updated: 2025-06-27
---
# Add an _isnull flag for any numeric feature with over 2% nulls, and impute on train only
For each numeric feature with more than 2% nulls add `<feature>_isnull`. Impute the median computed on the training split only, then apply it unchanged to validation and OOT. Missingness often carries signal: in the 2025 retention model `bur_income_band_isnull` ranked fifth.
