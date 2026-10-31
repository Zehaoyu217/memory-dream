---
from: [feat-mrisk-cb-ratio-90d, feat-mrisk-txn-concentration, feat-mrisk-new-merchant, ds-mrisk-merchant-month]
updated: 2026-04-22
---
# mrisk-gbm-v1: gradient-boosted merchant risk, three features, AUC 0.85
Gradient-boosted trees on the merchant-month panel with chargeback ratio, card concentration and new-merchant flag.
Labels from ds-mrisk-chargebacks (3 confirmed-fraud disputes in 90 days).
AUC 0.85 and precision@100 0.41 on mrisk-oot-2025h2 (exp-502). Superseded by mrisk-gbm-v2 on 2026-06-09.
