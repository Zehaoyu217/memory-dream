## Q1
Four decisions rest on ds-cu-call-outcomes: dec-cu-uplift-for-calls (through cu-resp-v1, exp-101, find-cu-response-misranks and exp-105), dec-cu-drop-tod (through feat-cu-call-tod-v1 and find-cu-tod-leak), dec-cu-promote-v3 (through the cu-uplift chain v1→v2→v3 and find-cu-sms-cost), and dec-ch-call-escalation (through find-cu-sms-cost and find-ch-sms-call-gap). I left out dec-ch-sms-first, because I read its "30-day prior contact count" as feat-ch-prior-contact-v1, which is built on ds-ch-contact-costs.
Notes: work/dec-cu-uplift-for-calls.md, work/dec-cu-drop-tod.md, work/dec-cu-promote-v3.md, work/dec-ch-call-escalation.md

## Q2
The line runs inc-gbm-v1 → inc-gbm-v2 → inc-gbm-v3, and inc-gbm-v3 is in force now. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2 (the cadence-stability income model).
Notes: work/inc-gbm-v3.md, work/ds-inc-verified-2026.md, work/find-inc-log-target-gain.md, work/inc-gbm-v2.md

## Q3
ch-bandit-v1 rests on three datasets: ds-ch-ab-wave1, ds-ch-ab-wave2 and ds-ch-contact-costs. It reaches them through ch-propensity-v1/v2, the channel features, exp-507 and find-ch-sms-matches-call.
Notes: work/ds-ch-ab-wave1.md, work/ds-ch-ab-wave2.md, work/ds-ch-contact-costs.md

## Q4
Both models build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: work/feat-txc-descriptor-tokens-v1.md, work/feat-txc-mcc-prior.md

## Q5
Two decisions rest on ds-cc-holdout, both through cc-logreg-v1. dec-cc-ft-v1 comes through exp-201-complaint-classification. dec-cc-drop-dispute-v1 comes through exp-202, fnd-cc-dispute-link-helps, exp-204, fnd-cc-dispute-link-leak and feat-cc-dispute-link-v2.
Notes: work/dec-cc-ft-v1.md, work/dec-cc-drop-dispute-v1.md

## Q6
The line runs feat-lbl-churn-flag-60d → feat-lbl-churn-flag-90d → feat-lbl-churn-flag-closure, and feat-lbl-churn-flag-closure is in force now. It is built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: work/feat-lbl-churn-flag-closure.md, work/dec-lbl-churn-closure.md, work/feat-lbl-churn-flag-90d.md

## Q7
cu-resp-v1 rests on two datasets. ds-cu-call-outcomes comes directly and through feat-cu-contact-hist-v2. ds-cu-cases-dpd comes through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: work/ds-cu-call-outcomes.md, work/ds-cu-cases-dpd.md

## Q8
Only dec-cli-uplift-targeting rests on it. The path goes through cli-xgb-v1 (and exp-103), then cli-xgb-v2 and exp-106, plus exp-102 and find-cli-uplift-wins, and on into cli-xgb-v3.
Notes: work/dec-cli-uplift-targeting.md

## Q9
The line runs cld-gbm-v1 → cld-gbm-v2 → cld-gbm-v3, and cld-gbm-v3 is in force now. It is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: work/cld-gbm-v3.md, work/cld-gbm-v2.md, work/feat-cld-payment-shock.md

## Q10
cc-ft-v1 rests on three datasets. ds-cc-qa-labels and ds-cc-taxonomy-v3 come directly. ds-cc-tickets-raw comes through ds-cc-qa-labels and feat-cc-embed-v1.
Notes: work/ds-cc-qa-labels.md, work/ds-cc-taxonomy-v3.md, work/ds-cc-tickets-raw.md