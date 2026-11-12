## Q1
Four decision notes rest on ds-cu-call-outcomes. Three are in collections-uplift (dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3), and one is in collections-channel-mix (dec-ch-call-escalation), which builds on find-cu-sms-cost and so reaches the label through the cu-uplift chain.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is in force. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note from another project builds directly on rdm-uplift-v1: exp-506 in customer-lifetime-value.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on two randomised-test datasets and one cost dataset: ds-ch-ab-wave1, ds-ch-ab-wave2 and ds-ch-contact-costs.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 (via exp-201 and cc-logreg-v1) and dec-cc-drop-dispute-v1 (via fnd-cc-dispute-link-leak, exp-204 and cc-logreg-v1). dec-cc-auto-threshold reports numbers on holdout-2025q4, but its build chain does not go through ds-cc-holdout, so I excluded it.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is in force. It is built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes from other projects build directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1, both in revenue-forecast-2026.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes (directly, and via feat-cu-contact-hist-v2) and ds-cu-cases-dpd (via feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour).
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Only dec-cli-uplift-targeting rests on ds-cli-holdout-2025q4, through cli-xgb-v3, exp-106 and find-cli-uplift-wins.
Notes: credit-line-increase/dec-cli-uplift-targeting.md