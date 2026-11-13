## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation. About 90 other notes in work/ have links the memory could not match, so they may also rest on it; I have not confirmed that.
Notes: work/dec-cu-drop-tod.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
The line runs inc-gbm-v1 → inc-gbm-v2 → inc-gbm-v3, so inc-gbm-v3 is in force. It is built on ds-inc-verified-2026 and find-inc-log-target-gain, and on inc-gbm-v2 (the model it replaced). It also names a cadence-stability income model that the memory could not match to a note.
Notes: work/inc-gbm-v3.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md

## Q3
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 directly through exp-507-collections-channel-mix, and ds-ch-ab-wave1 and ds-ch-contact-costs through the chain ch-propensity-v2 → ch-propensity-v1 and the other features. ds-ch-ab-wave1 and ds-ch-contact-costs each name an input in words that matched no note, so their chains may be incomplete.
Notes: work/ds-ch-ab-wave2.md, work/ds-ch-ab-wave1.md, work/ds-ch-contact-costs.md

## Q4
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. Both come through cc-logreg-v1 and the complaint-classification experiments.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md