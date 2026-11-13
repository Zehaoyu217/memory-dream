## Q1
One note from another project builds directly on find-cu-sms-cost: collections-channel-mix/find-ch-sms-call-gap, which says it builds on exp-504, find-ch-sms-matches-call and collections-uplift/find-cu-sms-cost.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through it. Its other upstream notes are the feature feat-bt-util-3m and the question q-bt-who-accepts.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1. cli-xgb-v1 also uses the ds-cli-holdout-2025q4 dataset, which is not a feature.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current (no supersession marker) and builds directly on feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2 from January 2026.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback. The first is direct; the other two reach it through the models and maps built on the cohort set.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, so cu-uplift-v3 is in force. It is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note from another project builds directly on feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2, which uses it for the utilisation slope in its bands.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026 (both direct or near-direct), plus ds-bsm-v8-history and ds-bsm-app-dev-2024 further back. I inferred ds-bsm-app-dev-2024's kind from its name and description, since its kind line was not in the output.
Notes: bureau-score-migration/bsm-app-gbm-v10b.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-app-dev-2024.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also uses feat-fsm-util-ratio, which is not shared with the spend model.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model that builds directly on a replaced feature: feat-cli-util-v1, which was superseded by feat-cli-util-v2 on 2025-10-14. cli-xgb-v3 is current but does not build directly on any replaced feature or dataset.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md