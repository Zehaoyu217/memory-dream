## Q1
Three decision notes rest on ds-cu-call-outcomes: dec-cu-promote-v3 (via cu-uplift-v3, v2, and feat-cu-contact-hist-v2), dec-cu-uplift-for-calls (via exp-105 and find-cu-response-misranks, which use cu-uplift-v2 and cu-resp-v1), and dec-cu-drop-tod (via find-cu-tod-leak and feat-cu-call-tod-v1).
Notes: work/dec-cu-promote-v3.md, work/dec-cu-uplift-for-calls.md, work/dec-cu-drop-tod.md, work/ds-cu-call-outcomes.md

## Q2
inc-gbm-v3 is the note in force; it replaced inc-gbm-v2, which had replaced inc-gbm-v1. It is built on ds-inc-verified-2026, find-inc-log-target-gain, and the cadence-stability income model.
Notes: work/inc-gbm-v3.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md

## Q3
ch-bandit-v1 traces back to three dataset roots: ds-ch-ab-wave1 (the first randomised channel test), ds-ch-ab-wave2 (the second test), and ds-ch-contact-costs (per-contact costs). The chain runs through ch-propensity-v2, exp-507, and ch-propensity-v1.
Notes: work/ds-ch-ab-wave1.md, work/ds-ch-ab-wave2.md, work/ds-ch-contact-costs.md, work/ch-bandit-v1.md

## Q4
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout. dec-cc-ft-v1 gets there through exp-201, which builds on cc-logreg-v1, and dec-cc-drop-dispute-v1 gets there through feat-cc-dispute-link-v2, fnd-cc-dispute-link-leak, exp-204, and exp-202, which builds on cc-logreg-v1. dec-cc-auto-threshold does not build on ds-cc-holdout; it uses cc-ft-v1 and its numbers are evaluated on holdout-2025q4, but that is not a build dependency.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md, work/ds-cc-holdout.md

## Q6
feat-lbl-churn-flag-closure is in force, and it replaced feat-lbl-churn-flag-90d. It is built on dec-lbl-churn-closure and the superseded 90-day churn flag, feat-lbl-churn-flag-90d.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md

## Q7
cu-resp-v1 traces back to two dataset roots: ds-cu-call-outcomes (through feat-cu-contact-hist-v2 and directly) and ds-cu-cases-dpd (through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour). Neither dataset note builds on anything else.
Notes: work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md, work/cu-resp-v1.md

## Q8
Only dec-cli-uplift-targeting rests on ds-cli-holdout-2025q4. The chain runs ds-cli-holdout-2025q4 → cli-xgb-v1 → cli-xgb-v2 → exp-106 (and ds-cli-oot-2026h1) → cli-xgb-v3 → dec-cli-uplift-targeting.
Notes: work/dec-cli-uplift-targeting.md, work/ds-cli-holdout-2025q4.md

## Q9
cld-gbm-v3 is in force; it replaced cld-gbm-v2, which had replaced cld-gbm-v1. It is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: work/cld-gbm-v3.md, work/feat-cld-payment-shock.md

## Q10
cc-ft-v1 traces back to three dataset roots: ds-cc-qa-labels, which builds on ds-cc-tickets-raw, ds-cc-taxonomy-v3, and ds-cc-tickets-raw, which is also reached through feat-cc-embed-v1.
Notes: work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/ds-cc-tickets-raw.md, work/cc-ft-v1.md