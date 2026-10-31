---
from: [exp-104-limit-headroom-full, find-bt-headroom-top]
updated: 2025-07-08
supersedes: [find-bt-headroom-top]
---
# Finding: post-offer limit increases leak the target; random-split AUC falls from 0.81 to 0.74
Limit increases dated after the BT offer open are often caused by the offer itself (the customer accepts and gets a bump). Including them inflates AUC.
exp-104: random split 0.81 with all rows, 0.74 with pre-offer rows only. The clean model's holdout AUC is 0.68 (bt-xgb-v2).
Action: dec-bt-drop-post-offer-features.
