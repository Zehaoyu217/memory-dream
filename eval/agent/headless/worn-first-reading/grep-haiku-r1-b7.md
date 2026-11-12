## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix, which reaches it through find-ch-sms-call-gap and find-cu-sms-cost.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is the one in force. It builds on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2, the cadence-stability model.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note in another project builds directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which uses its 2.8pp uplift.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1 and ds-ch-ab-wave2 (the two randomised channel tests) and ds-ch-contact-costs, through ch-propensity-v2, exp-506, exp-507 and feat-ch-prefer-channel-v1.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1, via exp-201 and cc-logreg-v1, and dec-cc-drop-dispute-v1, via fnd-cc-dispute-link-leak, exp-204, exp-202 and cc-logreg-v1.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is the one in force. It builds on dec-lbl-churn-closure and feat-lbl-churn-flag-90d, which replaced feat-lbl-churn-flag-60d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in revenue-forecast-2026 build directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase, via cli-xgb-v1 and exp-102, and dec-cld-band-policy-2026 in limit-decrease-policy, via feat-cld-risk-band-v2, feat-cli-util-v2 and exp-103.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md