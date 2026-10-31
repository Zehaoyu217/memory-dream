---
from: [ds-txc-descriptor-sample, ds-txc-labelled-merchants]
updated: 2025-07-01
---
# feat-txc-descriptor-tokens-v1: char 3-5 gram TF-IDF on raw descriptors
Character 3- to 5-gram TF-IDF on the raw descriptor string, capped at 180k features.
The input is the descriptor as the bank stores it, so store numbers and city suffixes add noise.
Baseline for txc-logreg-v1 and the first txc-gbm-v2 runs (exp-101, exp-103).
Superseded by feat-txc-descriptor-tokens-v2 once normalisation was added.
