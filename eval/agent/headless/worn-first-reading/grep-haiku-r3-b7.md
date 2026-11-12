## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix. The last one reaches it through find-ch-sms-call-gap, find-cu-sms-cost, cu-uplift-v3 and back to cu-resp-v1.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is in force. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2 (the note the team calls the cadence-stability income model).
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only customer-lifetime-value exp-506 builds directly on rdm-uplift-v1.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-contact-costs, ds-ch-ab-wave1 and ds-ch-ab-wave2. It reaches them through ch-propensity-v2, ch-propensity-v1, exp-507, exp-506, feat-ch-prefer-channel-v1, find-ch-sms-matches-call, exp-501 and exp-502.
Notes: collections-channel-mix/ds-ch-contact-costs.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout. dec-cc-ft-v1 gets there through exp-201 and cc-logreg-v1. dec-cc-drop-dispute-v1 gets there through feat-cc-dispute-link-v2 and fnd-cc-dispute-link-leak, back through exp-204, fnd-cc-dispute-link-helps and exp-202 to cc-logreg-v1.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
The line ends at feat-lbl-churn-flag-closure, which is built on dec-lbl-churn-closure and the superseded 90-day flag feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two revenue-forecast-2026 notes build directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes, ds-cu-call-outcomes and ds-cu-cases-dpd. It gets there directly or through feat-cu-contact-hist-v2, feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/cu-resp-v1.md, collections-uplift/feat-cu-contact-hist-v2.md, collections-uplift/feat-cu-dpd-roll-v1.md, collections-uplift/feat-cu-pay-behaviour.md, collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Only dec-cli-uplift-targeting rests on ds-cli-holdout-2025q4, through cli-xgb-v3 and exp-106 back to cli-xgb-v1 and cli-xgb-v2, and through find-cli-uplift-wins and exp-102.
Notes: credit-line-increase/dec-cli-uplift-targeting.md