## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, plus dec-ch-call-escalation in collections-channel-mix. The first three reach it through cu-resp-v1 and the cu-uplift models, and the last through the collections-uplift findings.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is the note in force, after inc-gbm-v1 was replaced by inc-gbm-v2 and inc-gbm-v2 by inc-gbm-v3. It is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only customer-lifetime-value/exp-506 is built directly on rdm-uplift-v1 from another project. It also builds on clv-ml-v2.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1 and ds-ch-ab-wave2, which are randomised channel tests, and ds-ch-contact-costs, which gives per-contact costs by channel.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on the feature notes feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md, txn-categorization/txc-gbm-v2.md, txn-categorization/txc-logreg-v1.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 through cc-logreg-v1 and cc-ft-v2, and dec-cc-drop-dispute-v1 through feat-cc-dispute-link-v2 and the dispute-link findings. dec-cc-taxonomy-split does not rest on it.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is the note in force, after feat-lbl-churn-flag-60d was replaced by feat-lbl-churn-flag-90d and that by feat-lbl-churn-flag-closure. It is built directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in revenue-forecast-2026 are built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1. No other project's notes build on it directly.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through the feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour features.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase, and dec-cld-band-policy-2026 in limit-decrease-policy, which reaches it through the cli-xgb models and the uplift findings.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md