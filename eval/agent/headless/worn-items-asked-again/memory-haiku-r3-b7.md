## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix (through find-ch-sms-call-gap).
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is the version in force. It was built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2, so it also rests on the earlier income chain through inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only customer-lifetime-value/exp-506 was built directly on rdm-uplift-v1 from another project.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1 and ds-ch-ab-wave2 (the two channel tests) and ds-ch-contact-costs (per-contact costs).
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1, reached through cc-logreg-v1 and the fine-tuned model chain. dec-cc-taxonomy-split does not rest on it in the memory graph.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is the version in force. It was built directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d, so it also rests on the 90-day rule and the legacy 60-day flag.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes of other projects were built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1, both in revenue-forecast-2026. exp-305 and rev26-interchange-v1 also use it as a volume input, but their "builds on" lines do not name it.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through the DPD roll and payment-behaviour features.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase and dec-cld-band-policy-2026 in limit-decrease-policy, both through the xgb and uplift model chains.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md