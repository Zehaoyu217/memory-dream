---
from: [bt-xgb-v2, q-bt-margin-threshold]
updated: 2026-02-19
---
# exp-107: margin-weighted label puts 61% of 12-month margin in the top 30%, up from 48%
Retrained the bt-xgb-v2 features with target = 12-month net margin per exposed account (promo fee and expected loss deducted), from `bt.offer_log` joined to `cards.accounts_monthly`.
Eval bt-holdout-2025q1 (n=41,800): top 30% of scores capture 61% of 12-month margin, versus 48% for the acceptance label.
AUC against acceptance rises slightly, from 0.68 to 0.69. Result model is bt-xgb-v3.
