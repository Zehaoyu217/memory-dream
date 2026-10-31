---
from: [feat-ae-depth-v1, exp-504]
updated: 2026-02-04
supersedes: [feat-ae-depth-v1]
---
# Depth v2: screens and features per active day, divided by a tenure-based baseline so new accounts are not inflated
The baseline is the median depth of accounts at the same tenure month, from the prior quarter. Accounts with under 90 days get the baseline from their own cohort.
Mean score for accounts under 90 days drops from 62 under v1 to 48 under v2 (exp-504).
