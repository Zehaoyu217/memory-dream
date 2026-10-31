---
from: [feat-csb-spend-raw, fnd-csb-seasonal-trap, ds-csb-merchant-mix]
updated: 2026-01-12
supersedes: [feat-csb-spend-raw]
---
# feat-csb-spend-sa-v2: spend divided by the 2024 merchant-category monthly median
- For each account, 3-month spend divided by the 2024 median for the same merchant categories and calendar months, from the merchant-mix build.
- Removes the December lift: the seasonal gap in churn score falls to 0.01 (exp-206).
- Replaces feat-csb-spend-raw in csb-xgb-v2.
