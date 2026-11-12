## Q1
One decision rests on ds-cu-call-outcomes: dec-cu-drop-tod. It is reached through feat-cu-call-tod-v1, which was built directly on the dataset.
Notes: collections-uplift/dec-cu-drop-tod.md

## Q2
The line runs inc-gbm-v1 → inc-gbm-v2 → inc-gbm-v3, so inc-gbm-v3 is the one in force now. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2, which it replaces.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note from another project was built directly on rdm-uplift-v1: exp-506 in customer-lifetime-value.
Notes: customer-lifetime-value/exp-506.md

## Q4
Following ch-bandit-v1 all the way back, it rests on three datasets: ds-ch-ab-wave1, ds-ch-ab-wave2 and ds-ch-contact-costs.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both models build directly on the same two features: feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decisions rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. Both are reached through cc-logreg-v1 and the notes built on it.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
The line runs feat-lbl-churn-flag-60d → feat-lbl-churn-flag-90d → feat-lbl-churn-flag-closure, so feat-lbl-churn-flag-closure is the one in force now. It is built on dec-lbl-churn-closure and on feat-lbl-churn-flag-90d, which it replaces.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in revenue-forecast-2026 were built directly on sfc-hier-v3: the dataset ds-rev26-spend-volume and the model rev26-combined-v1.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on one dataset, ds-cu-cases-dpd. It is reached through its three features: feat-cu-contact-hist-v2, feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decisions rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase and dec-cld-band-policy-2026 in limit-decrease-policy.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md