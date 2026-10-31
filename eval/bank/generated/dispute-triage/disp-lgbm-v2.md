---
from: [disp-lgbm-v1, feat-disp-amount-band, feat-disp-txn-match, feat-disp-merchant-cb-rate, exp-303]
supersedes: [disp-lgbm-v1]
updated: 2026-04-21
---
# disp-lgbm-v2 adds amount band, txn match and merchant chargeback rate; 93.4% at 0.90
LightGBM on four feature groups: reason text, amount band, transaction match, merchant 90-day dispute ratio.
Out-of-time on disp-oot-2026h1: precision 93.4% and coverage 31% at p>=0.90 (exp-304).
Superseded by disp-lgbm-v3 on 2026-09-14; auto-resolve was paused on v2 (dec-disp-autoresolve-095).
