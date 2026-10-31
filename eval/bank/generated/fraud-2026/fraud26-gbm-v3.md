---
from: [fraud26-gbm-v2, feat-f26-geo-mismatch, feat-f26-amt-zscore, exp-207]
supersedes: [fraud26-gbm-v2]
updated: 2026-08-19
---
# fraud26-gbm-v3 adds geo-mismatch and amount z-score: AUC 0.933 on fraud26-oot-2026h1
Adds feat-f26-geo-mismatch and feat-f26-amt-zscore to the v2 feature set; same 60-day maturity rule.
Eval on fraud26-oot-2026h1: AUC 0.933, KS 0.72, recall@1% 0.61 (exp-207, 2026-07-02).
Current model; alert threshold 0.66 (exp-208, dec-f26-promote-v3).
