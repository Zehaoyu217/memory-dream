---
from: [exp-306, find-rs-region-proxy, feat-rs-bureau-postco-v1, feat-rs-contact-attempts]
updated: 2025-09-18
supersedes: [rs-xgb-v1]
---
# rs-xgb-v2 is the recovery classifier with post-charge-off bureau and contact features, no region feature; Gini 0.47
Features: feat-rs-balance-at-co, feat-rs-pay-before-co, feat-rs-bureau-postco-v1, feat-rs-contact-attempts.
Gini 0.47 and KS 0.33 on recovery-scoring-holdout-2023h2 (n=6,120), exp-306.
Used for agency placement from October 2025. Superseded by rs-xgb-v3 (2026-02-10).
