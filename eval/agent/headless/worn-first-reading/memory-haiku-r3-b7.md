## Q1
Only one decision note rests on ds-cu-call-outcomes: dec-cu-drop-tod, reached through feat-cu-call-tod-v1 and find-cu-tod-leak. The other notes in that chain (exp-103, find-cu-tod-gain) are not decisions.
Notes: collections-uplift/dec-cu-drop-tod.md

## Q2
inc-gbm-v3 is in force at the end of the line, since nothing supersedes it. It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note in another project is built directly on rdm-uplift-v1: exp-506 in customer-lifetime-value. The other dependents are in reactivation-dormant itself.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: the wave-1 and wave-2 channel tests and the per-contact cost table.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both models build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/txc-gbm-v2.md, txn-categorization/txc-logreg-v1.md, txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 (through cc-logreg-v1 and the fine-tuning experiments) and dec-cc-drop-dispute-v1 (through the dispute-link findings).
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is in force at the end of the line. It is built on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in other projects are built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1, both in revenue-forecast-2026. exp-305 and rev26-interchange-v1 mention it but do not build on it.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on one dataset note, ds-cu-cases-dpd, reached through its three feature notes.
Notes: collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting and limit-decrease-policy/dec-cld-band-policy-2026.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md