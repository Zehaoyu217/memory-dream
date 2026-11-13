## Q1
Four decision notes rest on ds-cu-call-outcomes, all indirectly: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation. They reach it through cu-resp-v1, the two collections features (call time-of-day and contact history) and the cu-uplift models.
Notes: work/dec-cu-drop-tod.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
The line runs inc-gbm-v1 → inc-gbm-v2 → inc-gbm-v3, and inc-gbm-v3 is the one in force now. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2 (the "cadence-stability income model" its text names).
Notes: work/inc-gbm-v3.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md, work/inc-gbm-v2.md

## Q3
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2, ds-ch-ab-wave1 and ds-ch-contact-costs. At the start of the chain, ds-ch-contact-costs takes its call costs from the raw `callcenter.calls` cost fields, which the note names as a table and does not link to a note.
Notes: work/ds-ch-ab-wave2.md, work/ds-ch-ab-wave1.md, work/ds-ch-contact-costs.md

## Q4
Both models build directly on the same two feature notes: feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout, both indirectly through cc-logreg-v1 and its experiments and findings: dec-cc-ft-v1 and dec-cc-drop-dispute-v1.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md

## Q6
The line runs feat-lbl-churn-flag-60d → feat-lbl-churn-flag-90d → feat-lbl-churn-flag-closure, and feat-lbl-churn-flag-closure is in force now. It is built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md

## Q7
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes, which it uses directly, and ds-cu-cases-dpd, which it reaches through its features.
Notes: work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md

## Q8
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting, through cli-xgb-v1 → v2 → v3, and dec-cld-band-policy-2026, through the CLI work that leads into feat-cld-risk-band-v2 and cld-gbm-v3.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md

## Q9
The line runs cld-gbm-v1 → cld-gbm-v2 → cld-gbm-v3, and cld-gbm-v3 is in force now. It is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/feat-cld-payment-shock.md

## Q10
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3, which it uses directly, and ds-cc-tickets-raw, which it reaches through those and feat-cc-embed-v1.
Notes: work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/ds-cc-tickets-raw.md