## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, plus dec-ch-call-escalation in collections-channel-mix.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is the model in force (inc-gbm-v1 was replaced by inc-gbm-v2, which was replaced by v3). It is built directly on inc-gbm-v2, find-inc-log-target-gain and ds-inc-verified-2026, and through those on 14 more notes.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/inc-gbm-v2.md, income-estimation/find-inc-log-target-gain.md, income-estimation/ds-inc-verified-2026.md

## Q3
Only one note of another project is built directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which takes its 2.8pp uplift from rdm-uplift-v1.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1 and ds-ch-ab-wave2 (through ch-propensity-v2 and exp-507) and ds-ch-contact-costs (through ch-propensity-v1 and the feature notes).
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1, both through cc-logreg-v1 and the experiments and findings built on it.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is the feature in force (60d was replaced by 90d, which was replaced by closure). It is built directly on feat-lbl-churn-flag-90d and dec-lbl-churn-closure, and through those on 9 more notes, including the 60d flag, ds-lbl-churn-labels and the churn-rate findings.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md, label-pipeline-rebuild/dec-lbl-churn-closure.md

## Q8
Two notes of other projects are built directly on sfc-hier-v3: revenue-forecast-2026/ds-rev26-spend-volume and revenue-forecast-2026/rev26-combined-v1.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase and dec-cld-band-policy-2026 in limit-decrease-policy, both through the CLI models built on that holdout.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md