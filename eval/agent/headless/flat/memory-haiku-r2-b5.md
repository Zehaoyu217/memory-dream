## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation. The first two and the last come through other notes built on the dataset, and dec-cu-promote-v3 comes through cu-uplift-v3 and its findings.
Notes: work/dec-cu-drop-tod.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
The note in force at the end of the inc-gbm-v1 line is inc-gbm-v3, which is built on ds-inc-verified-2026 (dataset), find-inc-log-target-gain (finding) and inc-gbm-v2 (model). Its note also names a "cadence-stability income model" that no note was placed for, so that link is unresolved.
Notes: work/inc-gbm-v3.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md, work/inc-gbm-v2.md

## Q3
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 directly, and ds-ch-ab-wave1 and ds-ch-contact-costs through ch-propensity-v2 and the experiments. Two of these name inputs that no note was placed for (q-ch-sms-vs-call and the `callcenter.calls` cost fields), so the chain is not complete.
Notes: work/ds-ch-ab-wave2.md, work/ds-ch-ab-wave1.md, work/ds-ch-contact-costs.md

## Q4
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1, both through the cc-logreg-v1 and cc-ft-v2 chain.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md

## Q6
The note in force at the end of the feat-lbl-churn-flag-60d line is feat-lbl-churn-flag-closure, which is built on dec-lbl-churn-closure (decision) and feat-lbl-churn-flag-90d (the superseded 90-day flag).
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md

## Q7
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd both directly and through feat-cu-dpd-roll-v1 and related features.
Notes: work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md

## Q8
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting, through cli-xgb-v3 and its findings, and dec-cld-band-policy-2026, through cld-gbm-v3 and related notes.
Notes: work/dec-cli-uplift-targeting.md, work/dec-cld-band-policy-2026.md

## Q9
The note in force at the end of the cld-gbm-v1 line is cld-gbm-v3, which is built on cld-gbm-v2 (model) and feat-cld-payment-shock (feature).
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/feat-cld-payment-shock.md

## Q10
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through them and through feat-cc-embed-v1.
Notes: work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/ds-cc-tickets-raw.md