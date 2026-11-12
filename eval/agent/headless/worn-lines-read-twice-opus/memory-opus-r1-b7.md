## Q1
Four decision notes rest on ds-cu-call-outcomes. Three are in collections-uplift: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3. The fourth is in collections-channel-mix: dec-ch-call-escalation.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
The line runs inc-gbm-v1 → inc-gbm-v2 → inc-gbm-v3, so inc-gbm-v3 is in force now. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note from another project builds directly on rdm-uplift-v1: exp-506 in customer-lifetime-value, which builds on clv-ml-v2 and rdm-uplift-v1.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2, ds-ch-ab-wave1 and ds-ch-contact-costs. It reaches them through exp-507, ch-propensity-v2, ch-propensity-v1 and the ch feature notes.
Notes: collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both models build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. Both reach it through cc-logreg-v1 and the experiments built on that model.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
The line runs feat-lbl-churn-flag-60d → feat-lbl-churn-flag-90d → feat-lbl-churn-flag-closure, so feat-lbl-churn-flag-closure is in force now. It is built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in revenue-forecast-2026 are built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1. exp-305 and rev26-interchange-v1 mention sfc-hier-v3 in their text, but neither lists it as something it builds on.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes. It uses ds-cu-call-outcomes directly, and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4. One is dec-cli-uplift-targeting in credit-line-increase. The other is dec-cld-band-policy-2026 in limit-decrease-policy.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md