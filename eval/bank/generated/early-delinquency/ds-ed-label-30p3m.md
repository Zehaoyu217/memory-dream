---
from: [ds-ed-current-base]
updated: 2025-02-07
---
# Label is 1 if the account reaches 30+ DPD within 3 months of the snapshot, from cards.payments_daily
Label: 1 if DPD reaches 30 or more at any month-end within three months after the snapshot, else 0. Built from `cards.payments_daily`.
Accounts that close inside the window with no 30+ event are counted as 0. This is a small bias, about 0.2 points of base rate.
Base rate on early-delinquency-holdout-2024q4: 3.4% (n=402,000 current accounts).
