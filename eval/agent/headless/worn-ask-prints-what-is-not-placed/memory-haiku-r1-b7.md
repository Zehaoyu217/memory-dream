## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod, dec-cu-uplift-for-calls and dec-cu-promote-v3 in collections-uplift, and dec-ch-call-escalation in collections-channel-mix. The memory lists 23 notes in that chain, and the decisions are the ones named here.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
The note in force at the end of the inc-gbm-v1 line is inc-gbm-v3, which is built directly on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2. Those trace back through inc-gbm-v2 to inc-gbm-v1's own inputs, but ds-inc-verified-2026 names a recurring ACH inflow dataset that no note records, so that link is unresolved.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/ds-inc-verified-2026.md, income-estimation/find-inc-log-target-gain.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note in another project is built directly on rdm-uplift-v1: exp-506 in customer-lifetime-value, which uses its 2.8pp uplift. The grep of the memory folder confirmed no other project note names it.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 and ds-ch-ab-wave1 (the two channel tests) and ds-ch-contact-costs (per-contact costs). Those are reached through ch-propensity-v2, exp-507 and the other notes in its 14-note chain.
Notes: collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
txc-gbm-v2 and txc-logreg-v1 both build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. They reach it through cc-logreg-v1, the fine-tuned and dispute-link experiments, and the other notes in its 12-note chain.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
The note in force is feat-lbl-churn-flag-closure, which is built directly on dec-lbl-churn-closure and the superseded feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/dec-lbl-churn-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes in revenue-forecast-2026 are built directly on sfc-hier-v3: ds-rev26-spend-volume, which uses its forecasts, and rev26-combined-v1, which uses it for volume error. The grep also found exp-305 mentioning it, but exp-305 builds only on ds-rev26-spend-volume and rev26-interchange-v1.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes, used directly, and ds-cu-cases-dpd, used through feat-cu-dpd-roll-v1 and feat-cu-pay-behaviour.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting in credit-line-increase and dec-cld-band-policy-2026 in limit-decrease-policy. They reach the holdout through cli-xgb-v1, cli-xgb-v2 and the other notes in its 23-note chain.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md