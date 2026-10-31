---
updated: 2025-02-11
---
# Random 70/30 account split was the team default until June 2025
Until 2025-06 every training table was split 70/30 at random by `account_id` in `ds_split_utils.random_split`. Lena Fischer showed that this let the model train on accounts whose later months sat in the holdout, so holdout AUC ran about 0.03 above live AUC on the 2024 cards.
This split is retired. Use `howto/oot-split-by-observation-date`. Old deck numbers built on it are kept only so they can be traced.
