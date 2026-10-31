---
from: [exp-307, feat-rdm-last-activity-v2, feat-rdm-prior-response, feat-rdm-balance-band, feat-rdm-app-installed, fnd-rdm-sms-uplift-v2]
updated: 2026-02-16
supersedes: [rdm-uplift-v1]
---
# rdm-uplift-v2: X-learner targeting model, holdout uplift@20% 3.6pp
- X-learner on five features: last activity v2, prior response, balance band, app installed and the corrected channel flag.
- Holdout rdm-oot-2025q1 (n=11,260): uplift@20% 3.6pp, Qini 0.47.
- Current reactivation-dormant targeting model.
