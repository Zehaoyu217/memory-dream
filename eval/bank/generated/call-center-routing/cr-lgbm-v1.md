---
from: [feat-cr-transcript-tfidf-v1, feat-cr-ivr-path-v1, feat-cr-caller-history-v1, feat-cr-tenure-v1, exp-101]
updated: 2026-01-30
---
# LightGBM multiclass v1 gives macro F1 0.79 on holdout-2025q4 with caller history v1
Inputs: TF-IDF SVD (200), IVR path tokens, caller history v1, tenure and product count. 14 classes, 600 trees, learning rate 0.05.
Macro F1 0.79 and top-1 accuracy 0.84 on holdout-2025q4 (n = 380,000 calls), scored 2026-01-30.
Superseded by cr-lgbm-v2 after the July 2026 out-of-time read (exp-104).
