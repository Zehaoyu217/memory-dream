## Q1
Four decision notes rest on ds-cu-call-outcomes: dec-cu-drop-tod and dec-cu-uplift-for-calls, dec-cu-promote-v3, and collections-channel-mix/dec-ch-call-escalation. They reach it through cu-resp-v1, feat-cu-call-tod-v1, the uplift models, and their experiments and findings.
Notes: collections-uplift/dec-cu-drop-tod.md, collections-uplift/dec-cu-uplift-for-calls.md, collections-uplift/dec-cu-promote-v3.md, collections-channel-mix/dec-ch-call-escalation.md

## Q2
inc-gbm-v3 is in force at the end of the line (inc-gbm-v1 was replaced by inc-gbm-v2, which was replaced by inc-gbm-v3). It is built on ds-inc-verified-2026, find-inc-log-target-gain and inc-gbm-v2.
Notes: income-estimation/inc-gbm-v3.md, income-estimation/inc-gbm-v2.md

## Q3
Only one note from another project was built directly on rdm-uplift-v1: customer-lifetime-value/exp-506, which measures the value of reactivation targeting.
Notes: customer-lifetime-value/exp-506.md

## Q4
ch-bandit-v1 rests on three dataset notes: ds-ch-ab-wave2 and ds-ch-ab-wave1 (the two channel tests) and ds-ch-contact-costs (per-contact costs). It reaches them through ch-propensity-v2, ch-propensity-v1, exp-507 and the feature notes.
Notes: collections-channel-mix/ds-ch-ab-wave2.md, collections-channel-mix/ds-ch-ab-wave1.md, collections-channel-mix/ds-ch-contact-costs.md

## Q5
Both txc-gbm-v2 and txc-logreg-v1 build directly on feat-txc-descriptor-tokens-v1 and feat-txc-mcc-prior.
Notes: txn-categorization/feat-txc-descriptor-tokens-v1.md, txn-categorization/feat-txc-mcc-prior.md

## Q6
Two decision notes rest on ds-cc-holdout: dec-cc-ft-v1 and dec-cc-drop-dispute-v1. They reach it through cc-logreg-v1 and the experiments and findings built on it. The one unplaced note that may build on it, cc-ft-v2, is a model, not a decision.
Notes: complaint-classification/dec-cc-ft-v1.md, complaint-classification/dec-cc-drop-dispute-v1.md

## Q7
feat-lbl-churn-flag-closure is in force at the end of the line (feat-lbl-churn-flag-60d was replaced by feat-lbl-churn-flag-90d, which was replaced by closure). It is built on dec-lbl-churn-closure and the superseded feat-lbl-churn-flag-90d.
Notes: label-pipeline-rebuild/feat-lbl-churn-flag-closure.md, label-pipeline-rebuild/feat-lbl-churn-flag-90d.md

## Q8
Two notes from revenue-forecast-2026 were built directly on sfc-hier-v3: ds-rev26-spend-volume and rev26-combined-v1.
Notes: revenue-forecast-2026/ds-rev26-spend-volume.md, revenue-forecast-2026/rev26-combined-v1.md

## Q9
cu-resp-v1 rests on two dataset notes: ds-cu-call-outcomes (directly) and ds-cu-cases-dpd (through feat-cu-pay-behaviour and the other features). The other direct input, glossary/promise-to-pay, is a term note.
Notes: collections-uplift/ds-cu-call-outcomes.md, collections-uplift/ds-cu-cases-dpd.md

## Q10
Two decision notes rest on ds-cli-holdout-2025q4: dec-cli-uplift-targeting, which goes through cli-xgb-v3, and dec-cld-band-policy-2026 in limit-decrease-policy, which goes through cld-gbm-v2 and the limit-decrease notes.
Notes: credit-line-increase/dec-cli-uplift-targeting.md, limit-decrease-policy/dec-cld-band-policy-2026.md