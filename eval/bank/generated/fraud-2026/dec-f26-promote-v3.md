---
from: [fraud26-gbm-v3, exp-208, fraud26-find-geo-drift, dec-f26-promote-v2]
supersedes: [dec-f26-promote-v2]
updated: 2026-08-26
---
# Promote fraud26-gbm-v3 with alert threshold 0.66 and no travel uplift
Decision: fraud26-gbm-v3 replaces v2 from 2026-08-26; alert threshold 0.66; no travel-specific uplift.
Basis: exp-207 (AUC 0.933, KS 0.72 on fraud26-oot-2026h1) and exp-208 (21.5% precision at 0.6% alert rate).
The geo-mismatch drift is logged for Q4 monitoring; no travel rule was added (q-f26-travel-rule).
