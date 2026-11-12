## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix. They do so directly or through the uplift models, experiments and findings built on it.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is the model in force now, since inc-gbm-v2 was replaced by it. It is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note of another project is built directly on rdm-uplift-v1: exp-506 in customer-lifetime-value, which rests on clv-ml-v2 and rdm-uplift-v1.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1 and ds-ch-ab-wave2, which both feed the chain, and ds-ch-contact-costs. It reaches them through ch-propensity-v1/v2, exp-506, exp-507 and the feature notes.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1, through exp-201 and cc-logreg-v1, and dec-cc-drop-dispute-v1, through feat-cc-dispute-link-v2 and fnd-cc-dispute-link-leak. cc-ft-v2 may also depend on ds-cc-holdout, but its recorded links do not show that, so I have left it out.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is the feature in force now, since feat-lbl-churn-flag-90d was replaced by it. It is built directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes of another project are built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1, both in revenue-forecast-2026.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase, and dec-cld-band-policy-2026 in limit-decrease-policy. They reach it through cli-xgb-v1/v3, exp-103, exp-106 and the limit-decrease models.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md