---
updated: 2026-04-06
---
# The weekly deck does not publish if `cards.txn_daily` row count is more than 5% off its trailing 7-day mean
- The gate compares the week's daily row count in `cards.txn_daily` with the trailing 7-day mean.
- A gap above 5% stops publication and posts to data-eng-cards; Tomás Rivera's team clears it.
- The gate result is shown as slide 8 of the weekly deck.
