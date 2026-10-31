---
from: [feat-cc-tfidf-v1, feat-cc-channel-v1, ds-cc-holdout]
updated: 2025-12-16
---
# Multinomial logistic regression on text and channel gives macro F1 0.74 on holdout-2025q4 without dispute link
18 classes, class weights balanced, C tuned on the training split. No dispute features in this version.
Macro F1 0.74 on holdout-2025q4 (n = 1,800 tickets). Used as the baseline in exp-201 to exp-205.
