## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3 and dec-ch-call-escalation. This counts "Builds on" and "Features" edges as dependencies and does not count "Replaces" or "Superseded" edges. If only "Builds on" edges count, dec-ch-call-escalation and dec-cu-promote-v3 drop out.
Notes: memory/work/dec-cu-drop-tod.md, memory/work/dec-cu-uplift-for-calls.md, memory/work/dec-cu-promote-v3.md, memory/work/dec-ch-call-escalation.md, memory/work/ds-cu-call-outcomes.md

## Q2
inc-gbm-v3 is in force. It is built on ds-inc-verified-2026 (9,850 verified-income accounts), find-inc-log-target-gain, and the cadence-stability income model (feat-inc-payroll-cadence-v2, via inc-gbm-v2).
Notes: memory/work/inc-gbm-v3.md, memory/work/ds-inc-verified-2026.md, memory/work/find-inc-log-target-gain.md, memory/work/feat-inc-payroll-cadence-v2.md

## Q3
ch-bandit-v1 rests on two randomised channel-test datasets and the per-contact cost table: ds-ch-ab-wave1, ds-ch-ab-wave2 and ds-ch-contact-costs.
Notes: memory/work/ds-ch-ab-wave1.md, memory/work/ds-ch-ab-wave2.md, memory/work/ds-ch-contact-costs.md

## Q4
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: memory/work/txc-gbm-v2.md, memory/work/txc-logreg-v1.md, memory/work/feat-txc-descriptor-tokens-v1.md, memory/work/feat-txc-mcc-prior.md

## Q5
Two decision notes rest on ds-cc-holdout. dec-cc-ft-v1 gets there through exp-201 and cc-logreg-v1. dec-cc-drop-dispute-v1 gets there through feat-cc-dispute-link-v2, fnd-cc-dispute-link-leak, exp-204, fnd-cc-dispute-link-helps, exp-202 and cc-logreg-v1. dec-cc-auto-threshold evaluates on holdout-2025q4 only in its text, not through a builds-on edge, so I left it out.
Notes: memory/work/dec-cc-ft-v1.md, memory/work/dec-cc-drop-dispute-v1.md, memory/work/ds-cc-holdout.md, memory/work/cc-logreg-v1.md

## Q6
feat-lbl-churn-flag-closure is in force. It is built on dec-lbl-churn-closure, and through the superseded 90-day flag on dec-lbl-churn-90d and ds-lbl-churn-labels.
Notes: memory/work/feat-lbl-churn-flag-60d.md, memory/work/feat-lbl-churn-flag-90d.md, memory/work/feat-lbl-churn-flag-closure.md, memory/work/dec-lbl-churn-closure.md, memory/work/dec-lbl-churn-90d.md, memory/work/ds-lbl-churn-labels.md

## Q7
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes (promise-to-pay labels) and ds-cu-cases-dpd (collections cases, 1–29 DPD).
Notes: memory/work/ds-cu-call-outcomes.md, memory/work/ds-cu-cases-dpd.md

## Q8
Only dec-cli-uplift-targeting rests on ds-cli-holdout-2025q4. It goes through cli-xgb-v3, then find-cli-uplift-wins and exp-102 to cli-xgb-v1, which builds on the holdout. It also goes through exp-106 to ds-cli-oot-2026h1, which builds on the holdout.
Notes: memory/work/dec-cli-uplift-targeting.md, memory/work/cli-xgb-v3.md, memory/work/find-cli-uplift-wins.md, memory/work/exp-102-credit-line-increase.md, memory/work/cli-xgb-v1.md, memory/work/exp-106-credit-line-increase.md, memory/work/ds-cli-oot-2026h1.md, memory/work/ds-cli-holdout-2025q4.md

## Q9
cld-gbm-v3 is in force. It is built on cld-gbm-v2 and the payment-shock feature (feat-cld-payment-shock), and cld-gbm-v2 is in turn built on cld-gbm-v1, which rests on ds-cld-decrease-cohort.
Notes: memory/work/cld-gbm-v3.md, memory/work/cld-gbm-v2.md, memory/work/cld-gbm-v1.md, memory/work/ds-cld-decrease-cohort.md

## Q10
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels (adjudicated complaint labels), ds-cc-taxonomy-v3 (the 18-code taxonomy) and ds-cc-tickets-raw (the raw ticket table, which also feeds feat-cc-embed-v1).
Notes: memory/work/ds-cc-qa-labels.md, memory/work/ds-cc-taxonomy-v3.md, memory/work/ds-cc-tickets-raw.md