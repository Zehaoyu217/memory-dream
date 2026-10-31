---
from: [exp-303, rdm-propensity-lr, feat-rdm-last-activity-v1, feat-rdm-app-installed]
updated: 2025-05-06
---
# rdm-uplift-v1: T-learner targeting model, holdout uplift@20% 2.8pp
- LightGBM T-learner trained on waves 1 and 2 (121,500 sends); features last activity v1, prior response, balance band and app installed.
- Holdout rdm-oot-2025q1: uplift@20% 2.8pp, Qini 0.41.
- Production targeting model until rdm-uplift-v2 in February 2026.
