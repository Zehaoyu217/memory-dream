---
from: [feat-bt-util-trend-v2, feat-bt-revolve-share, feat-bt-bureau-delta, feat-bt-limit-headroom, dec-bt-drop-post-offer-features, bt-xgb-v1]
updated: 2025-08-25
supersedes: [bt-xgb-v1]
---
# bt-xgb-v2: XGBoost, depth 5, 400 trees, AUC 0.68 on bt-holdout-2025q1
Inputs: feat-bt-util-trend-v2, feat-bt-revolve-share, feat-bt-bureau-delta, feat-bt-limit-headroom (pre-offer rows only).
On bt-holdout-2025q1 (n=41,800, label = acceptance): AUC 0.68, KS 0.27, top-30% lift 1.9x.
Trained on 2025 waves excluding holdout accounts. Scored weekly in production from Sept 2025 until bt-xgb-v3 replaced it.
