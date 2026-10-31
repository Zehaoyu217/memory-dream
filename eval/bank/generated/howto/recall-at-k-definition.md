---
updated: 2025-06-16
---
# recall@k is positives in the top k divided by all positives in the scored population
Sort accounts by score descending, with ties broken by `account_id`. recall@k = positives in the top k divided by all positives in the scored population. Accounts with no bureau pull are not scored, so they are left out of the denominator too.
Precision@k uses k as its denominator, so unscored accounts do not change it. Report both, with the population size in the footnote.
