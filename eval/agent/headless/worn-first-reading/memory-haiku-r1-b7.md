## Q1
One decision note rests on ds-cu-call-outcomes: dec-cu-drop-tod, which reaches it through feat-cu-call-tod-v1 and find-cu-tod-leak.
Notes: collections-uplift/dec-cu-drop-tod.md

## Q2
inc-gbm-v3 is the note in force at the end of that line. It is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note from another project was built directly on rdm-uplift-v1: customer-lifetime-value/exp-506.md.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 (directly), and ds-ch-ab-wave1 and ds-ch-contact-costs (through it).
Notes: collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1, both reached through cc-logreg-v1 and other notes built on it.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is the note in force at the end of that line. It is built directly on dec-lbl-churn-closure and feat-lbl-churn-flag-90d (the superseded 90-day flag).
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes from another project were built directly on sfc-hier-v3: revenue-forecast-2026/ds-rev26-spend-volume.md and revenue-forecast-2026/rev26-combined-v1.md.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on one dataset note, ds-cu-cases-dpd, which feeds its features directly or through feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase, and dec-cld-band-policy-2026 in limit-decrease-policy, which reaches it through other notes.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md