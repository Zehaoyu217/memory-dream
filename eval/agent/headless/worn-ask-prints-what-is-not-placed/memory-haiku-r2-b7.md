## Q1
Four decision notes rest on ds-cu-call-outcomes: three in collections-uplift (dec-cu-drop-tod, dec-cu-uplift-for-calls, dec-cu-promote-v3) and one in collections-channel-mix (dec-ch-call-escalation). The last reaches it through find-ch-sms-call-gap.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is in force at the end of the inc-gbm-v1 → inc-gbm-v2 → inc-gbm-v3 line. It is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note in another project builds directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which uses its 2.8pp uplift.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 and ds-ch-ab-wave1 (the two channel tests) and ds-ch-contact-costs (per-contact cost by channel). The chain runs back through ch-propensity-v2 and exp-507 to these.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 (via exp-201 and cc-logreg-v1) and dec-cc-drop-dispute-v1 (via feat-cc-dispute-link-v2).
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is in force at the end of the 60d → 90d → closure line. It is built on dec-lbl-churn-closure and on the superseded feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in revenue-forecast-2026 build directly on sfc-hier-v3: ds-rev26-spend-volume (the volume series) and rev26-combined-v1 (the combined revenue model).
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase, and dec-cld-band-policy-2026 in limit-decrease-policy, both through the cli-xgb models.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md