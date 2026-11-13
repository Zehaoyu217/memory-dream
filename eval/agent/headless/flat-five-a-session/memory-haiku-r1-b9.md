## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation. About 90 other work notes name a source that no note was placed for, so they may also rest on it but cannot be confirmed from the links.
Notes: work/dec-cu-drop-tod.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
The line runs inc-gbm-v1, then inc-gbm-v2, then inc-gbm-v3, and inc-gbm-v3 is the one in force. It builds on ds-inc-verified-2026 and find-inc-log-target-gain, and on the cadence-stability income model, which is named only in words. That model is most likely inc-gbm-v2 (the note that adds cadence stability), but the links do not confirm it.
Notes: work/inc-gbm-v3.md, work/inc-gbm-v2.md, work/inc-gbm-v1.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md

## Q3
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 (directly through exp-507 and ch-propensity-v2), ds-ch-ab-wave1 (through ch-propensity-v1 and the feature notes), and ds-ch-contact-costs (through the feature notes). The chain is not complete: ds-ch-ab-wave1 and ds-ch-contact-costs also cite sources (q-ch-sms-vs-call and the callcenter.calls cost fields) that have no note.
Notes: work/ds-ch-ab-wave2.md, work/ds-ch-ab-wave1.md, work/ds-ch-contact-costs.md

## Q4
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1, both through cc-logreg-v1. The other notes that rest on it are experiments, findings and features, and the ~90 unlinked notes could also include decisions.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md