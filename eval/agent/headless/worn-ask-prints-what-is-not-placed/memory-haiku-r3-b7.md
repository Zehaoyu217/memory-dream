## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix, which reaches it through the call-outcome chain.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is in force (it replaces inc-gbm-v2, which replaced inc-gbm-v1). It rests directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2, and through them on 14 more notes back to the stated-income, payroll-proxy and transaction-category datasets. Two inputs named only in words, a "recurring ACH inflow dataset" in ds-inc-verified-2026 and exp-403, have no note.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md, income-estimation/ds-inc-stated-income-2025.md, income-estimation/ds-inc-payroll-proxy.md, income-estimation/ds-inc-txn-categories.md, income-estimation/q-inc-coverage.md, income-estimation/exp-406.md, income-estimation/exp-402.md, income-estimation/exp-403.md, income-estimation/find-inc-mape-initial.md, income-estimation/feat-inc-payroll-cadence-v2.md, income-estimation/feat-inc-payroll-cadence-v1.md, income-estimation/feat-inc-rent-flag.md, income-estimation/feat-inc-spend-to-income.md, income-estimation/inc-gbm-v1.md, income-estimation/inc-linear-baseline.md

## Q3
Only customer-lifetime-value/exp-506 is built directly on rdm-uplift-v1 from another project.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: the wave-2 and wave-1 channel tests and the per-contact cost dataset.
Notes: collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is in force (it replaces feat-lbl-churn-flag-90d, which replaced the 60-day flag). It rests directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d, and through them on dec-lbl-churn-90d, feat-lbl-churn-flag-60d, ds-lbl-churn-labels, fnd-churn-rate-legacy, exp-401 and q-lbl-churn-window.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md, label-pipeline-rebuild/dec-lbl-churn-90d.md, label-pipeline-rebuild/feat-lbl-churn-flag-60d.md, label-pipeline-rebuild/ds-lbl-churn-labels.md, label-pipeline-rebuild/fnd-churn-rate-legacy.md, label-pipeline-rebuild/exp-401.md, label-pipeline-rebuild/q-lbl-churn-window.md

## Q8
Two notes of revenue-forecast-2026 are built directly on sfc-hier-v3: the spend-volume dataset and the combined revenue model.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through the feature notes.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase and dec-cld-band-policy-2026 in limit-decrease-policy.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md