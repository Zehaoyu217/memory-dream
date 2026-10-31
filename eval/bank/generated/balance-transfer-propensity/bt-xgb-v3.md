---
from: [bt-xgb-v2, exp-107-margin-label, dec-bt-margin-label]
updated: 2026-02-19
supersedes: [bt-xgb-v2]
---
# bt-xgb-v3: same features as v2, trained on 12-month margin per account; AUC 0.69 on acceptance
Target changed from accept/no-accept to 12-month net margin per exposed account, after promo fee and expected loss. Same inputs as bt-xgb-v2.
On bt-holdout-2025q1: AUC 0.69 against acceptance (n=41,800). The top 30% of scores capture 61% of 12-month margin, versus 48% for bt-xgb-v2.
Current production model from 2026-03-01.
