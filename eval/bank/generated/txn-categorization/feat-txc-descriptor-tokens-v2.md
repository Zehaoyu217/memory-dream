---
from: [feat-txc-descriptor-tokens-v1, feat-txc-normalise-v2]
supersedes: [feat-txc-descriptor-tokens-v1]
updated: 2026-02-02
---
# feat-txc-descriptor-tokens-v2: char 2-5 grams and word tokens on normalised descriptors
Char 2- to 5-grams plus word tokens, computed after feat-txc-normalise-v2, capped at 240k features.
Replaces the raw-string v1 tokens in every current training run.
Fit on the 2025-H2 training split only, so the time-split evaluation stays clean.
Input to txc-gbm-v3.
