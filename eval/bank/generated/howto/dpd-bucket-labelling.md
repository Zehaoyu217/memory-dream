---
updated: 2025-04-11
---
# DPD buckets are 0 current, 1 to 29, 30 to 59, 60 to 89 and 90 plus; 30+ means DPD at least 30
Days past due are read from `cards.payments_daily` at the label date. Buckets are 0 current, 1 to 29 early, 30 to 59, 60 to 89 and 90 plus. The label 30+ means DPD greater than or equal to 30, so an account at exactly 30 days is counted.
Using strictly greater than 30 undercounted roll rates in the 2024 vintages by about 4% of the 30-day bucket.
