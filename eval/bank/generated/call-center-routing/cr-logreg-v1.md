---
from: [feat-cr-transcript-tfidf-v1, feat-cr-ivr-path-v1]
updated: 2026-01-12
---
# Multinomial logistic regression baseline gives macro F1 0.61 on holdout-2025q4
Inputs: TF-IDF SVD features plus one-hot IVR path tokens. 14 classes, class weights balanced.
Macro F1 0.61 and top-1 accuracy 0.66 on holdout-2025q4 (n = 380,000 calls).
Kept only as the floor for comparisons; it is the reference point in dec-cr-lgbm.
