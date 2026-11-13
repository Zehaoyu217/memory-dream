## Q1
Four decisions rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix. They reach it through cu-resp-v1, feat-cu-call-tod-v1 and the uplift models built on them.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is in force; it replaced inc-gbm-v2, which had replaced inc-gbm-v1. inc-gbm-v3 is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/inc-gbm-v1.md, income-estimation/inc-gbm-v2.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md

## Q3
Only one note in another project is built directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which takes its 2.8pp uplift as an input.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: the wave-1 and wave-2 channel tests and the per-contact cost table. The chain runs through ch-propensity-v2, ch-propensity-v1 and exp-507.
Notes: collections-channel-mix/ch-bandit-v1.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/txc-gbm-v2.md, txn-categorization/txc-logreg-v1.md, txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decisions rest on ds-cc-holdout: dec-cc-ft-v1, via cc-ft-v1 and the fine-tuning experiments, and dec-cc-drop-dispute-v1, via the dispute-link experiments. cc-ft-v2 has an unresolved link to "the 30-day prior dispute count" that no note matches, so it may add to this list.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is in force; it replaced feat-lbl-churn-flag-90d, which had replaced feat-lbl-churn-flag-60d. It is built on dec-lbl-churn-closure and the superseded 90-day flag.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md, label-pipeline-rebuild/feat-lbl-churn-flag-60d.md, label-pipeline-rebuild/dec-lbl-churn-closure.md

## Q8
Two notes in another project are built directly on sfc-hier-v3: revenue-forecast-2026/ds-rev26-spend-volume and revenue-forecast-2026/rev26-combined-v1. revenue-forecast-2026/exp-305 also uses it as a backtest volume source, but its note does not name it as a build.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes directly, and ds-cu-cases-dpd through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decisions rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase, via cli-xgb-v2/v3 and the uplift experiments, and dec-cld-band-policy-2026 in limit-decrease-policy, via cld-gbm-v2/v3.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md