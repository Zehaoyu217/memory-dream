---
from: [find-bt-limit-leak, exp-104-limit-headroom-full]
updated: 2025-07-10
---
# feat-bt-limit-headroom: credit limit minus balance, using only limit rows dated before offer open
Headroom = credit limit minus statement balance, read from `cards.limits_history` for rows dated before the offer open date only.
Rows after offer open are excluded because limit increases often come from the BT offer itself (see find-bt-limit-leak and dec-bt-drop-post-offer-features).
Top feature by gain in bt-xgb-v2. Removing it drops holdout AUC by 0.03.
