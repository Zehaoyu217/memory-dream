---
from: [feat-txc-descriptor-tokens-v1, feat-txc-mcc-prior]
updated: 2025-07-22
---
# txc-logreg-v1 is the baseline: macro-F1 0.71 on holdout-2025q2
Multinomial logistic regression on char n-gram TF-IDF. Scores 0.71 with the MCC prior off (exp-101) and 0.74 with it on (exp-102).
Trained on the 2025-01 to 2025-04 labelled split; scored on holdout-2025q2 (n=2,000).
It is the reference every later run beats.
Superseded by txc-gbm-v2 in August 2025.
