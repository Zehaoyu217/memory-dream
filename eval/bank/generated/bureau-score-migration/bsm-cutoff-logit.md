---
from: [feat-bsm-v10-band, exp-305]
updated: 2026-07-21
---
# bsm-cutoff-logit: cutoff recalibration on v10 bands, approval rate held at 58% with cutoff 652
Logistic model maps v10 bands to the v8 approval decision so the approval rate stays where it was.
Eval: ds-bsm-v10-cohorts-2026, n=71,300; cutoff 652 on the v10 scale matches a v8 cutoff of 640 for 58% approval.
Used for the cutover decision in dec-bsm-cutover-2026q3.
