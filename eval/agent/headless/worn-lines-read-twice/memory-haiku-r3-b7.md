## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, plus dec-ch-call-escalation in collections-channel-mix.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v1 was replaced by inc-gbm-v2, which was replaced by inc-gbm-v3, so inc-gbm-v3 is in force. It is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note of another project is built directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which builds on clv-ml-v2 and rdm-uplift-v1.
Notes: customer-lifetime-value/exp-506.md

## Q4
The chain behind ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave1, ds-ch-ab-wave2 and ds-ch-contact-costs. Two unplaced notes, exp-508 and feat-ch-email-open-v1, may also be built on ch-bandit-v1, but no link confirms it.
Notes: collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 are built directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. Both reach it through other notes in the chain.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is in force, after feat-lbl-churn-flag-60d was replaced by feat-lbl-churn-flag-90d and that by the closure version. It is built directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes of other projects are built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1, both in revenue-forecast-2026.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
The chain behind cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes (direct) and ds-cu-cases-dpd (through feat-cu-dpd-roll-v1).
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase and dec-cld-band-policy-2026 in limit-decrease-policy.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md