## Q1
The only decision note resting on ds-cu-call-outcomes is dec-cu-drop-tod. It gets there through feat-cu-call-tod-v1, which is built directly on the dataset, and through find-cu-tod-leak.
Notes: collections-uplift/dec-cu-drop-tod.md

## Q2
inc-gbm-v1 was superseded by inc-gbm-v2, which was superseded by inc-gbm-v3, the note in force now. inc-gbm-v3 is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only customer-lifetime-value/exp-506 is built directly on rdm-uplift-v1 from outside reactivation-dormant.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 and ds-ch-ab-wave1, the two channel tests, and ds-ch-contact-costs, the per-contact cost table.
Notes: collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. dec-cc-taxonomy-split is not among them, because it rests on ds-cc-taxonomy-v3 instead.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-60d was superseded by feat-lbl-churn-flag-90d, which was superseded by feat-lbl-churn-flag-closure, the note in force now. feat-lbl-churn-flag-closure is built directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes of other projects are built directly on sfc-hier-v3: revenue-forecast-2026/ds-rev26-spend-volume and revenue-forecast-2026/rev26-combined-v1.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on one dataset note, ds-cu-cases-dpd, which feeds its features feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase, and dec-cld-band-policy-2026 in limit-decrease-policy.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md