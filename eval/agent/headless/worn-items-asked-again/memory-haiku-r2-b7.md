## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix. All 23 notes that rest on it were checked against the full dependency list.
Notes: memory/collections-uplift/dec-cu-drop-tod.md, memory/collections-uplift/dec-cu-uplift-for-calls.md, memory/collections-uplift/dec-cu-promote-v3.md, memory/collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v1 was replaced by inc-gbm-v2, which was replaced by inc-gbm-v3, the note in force now. inc-gbm-v3 is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: memory/income-estimation/inc-gbm-v3.md, memory/income-estimation/ds-inc-verified-2026.md, memory/income-estimation/find-inc-log-target-gain.md, memory/income-estimation/inc-gbm-v2.md

## Q3
Only one note from another project is built directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which combines it with clv-ml-v2. I checked the full dependency list for this.
Notes: memory/customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-contact-costs, ds-ch-ab-wave1 and ds-ch-ab-wave2. These are the only datasets among the 14 notes in its chain.
Notes: memory/collections-channel-mix/ds-ch-contact-costs.md, memory/collections-channel-mix/ds-ch-ab-wave1.md, memory/collections-channel-mix/ds-ch-ab-wave2.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: memory/txn-categorization/feat-txc-descriptor-tokens-v1.md, memory/txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. Both are reached through cc-logreg-v1 or the fine-tuned model chain.
Notes: memory/complaint-classification/dec-cc-ft-v1.md, memory/complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-60d was replaced by feat-lbl-churn-flag-90d, which was replaced by feat-lbl-churn-flag-closure, the note in force now. feat-lbl-churn-flag-closure is built on dec-lbl-churn-closure and the superseded feat-lbl-churn-flag-90d.
Notes: memory/label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, memory/label-pipeline-rebuild/dec-lbl-churn-closure.md, memory/label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes from other projects are built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1, both in revenue-forecast-2026.
Notes: memory/revenue-forecast-2026/ds-rev26-spend-volume.md, memory/revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes, ds-cu-call-outcomes directly and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: memory/collections-uplift/ds-cu-call-outcomes.md, memory/collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase and dec-cld-band-policy-2026 in limit-decrease-policy. Both are reached through the CLI model chain.
Notes: memory/credit-line-increase/dec-cli-uplift-targeting.md, memory/limit-decrease-policy/dec-cld-band-policy-2026.md