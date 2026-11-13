## Q1
Only one note in another project builds directly on collections-uplift's find-cu-sms-cost: collections-channel-mix/find-ch-sms-call-gap, which cites it alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on the dataset ds-bt-bureau-join and the feature feat-bt-util-3m. Through those it also rests on the dataset ds-bt-offer-log, which is the only other dataset in its chain.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is the only current churn-small-business model that builds directly on a replaced input: it uses feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. csb-xgb-v2 is also current but builds on the replacement, not the replaced note.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback, reached directly or through models, features and experiments built on the cohort set.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The note in force is cu-uplift-v3 (cu-uplift-v1 was superseded by cu-uplift-v2, which was superseded by cu-uplift-v3). cu-uplift-v3 is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note in another project builds directly on feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2, which uses its 6-month utilisation slope.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four datasets: ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026 directly or through its parents, and ds-bsm-app-dev-2024 and ds-bsm-v8-history further back through bsm-app-gbm-v8 and the v8 history.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also uses feat-fsm-util-ratio, which fsm-spend-lgbm-v2 does not.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current credit-line-increase model that builds directly on a replaced input: it uses feat-cli-util-v1, which feat-cli-util-v2 replaced. cli-xgb-v3 is also current, but it builds on experiments and a finding, not on a replaced feature or dataset.
Notes: credit-line-increase/cli-logreg-baseline.md