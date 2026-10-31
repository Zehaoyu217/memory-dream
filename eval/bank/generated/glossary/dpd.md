---
updated: 2025-01-08
---
# DPD (days past due)
DPD is the number of days an account has been past due, counted from the statement close date (the day the statement was cut). Buckets used in every report: 0, 1-29, 30-59, 60-89, 90-119, 120-179, 180+.
Computed nightly from `cards.payments_daily`.
Example: statement closed 3 Aug 2024 and nothing paid; on 17 Sept 2024 that balance is 45 DPD.
