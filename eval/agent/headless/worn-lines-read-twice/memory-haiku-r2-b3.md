## Q1
find-cu-sms-cost is built on directly by one note in another project: collections-channel-mix/find-ch-sms-call-gap, which says it "builds on exp-504, find-ch-sms-matches-call and collections-uplift/find-cu-sms-cost." No other folder's notes use it.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes. ds-bt-bureau-join is direct, and ds-bt-offer-log comes through feat-bt-util-3m, which is itself built on ds-bt-offer-log. The chain ends at the question q-bt-who-accepts.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1. cli-xgb-v1 also uses ds-cli-holdout-2025q4, which is a dataset, not a feature.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is the only current model that builds directly on a replaced feature. It uses feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. csb-xgb-v2, the other current model, uses only feature and dataset notes that are still in force.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap) and dec-bsm-cutover-2026q3 (via bsm-cutoff-logit and exp-305). I checked each link against the project's dependency list.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md, bureau-score-migration/dec-bsm-cutover-2026q3.md

## Q6
The note in force at the end of the line is cu-uplift-v3. It is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note in another project builds directly on feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2, which uses the utilisation slope from that feature.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes. ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026 are the direct inputs, and ds-bsm-v8-history and ds-bsm-app-dev-2024 come through the earlier v8 and v10a chain.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-app-dev-2024.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. Each also builds on its own v1 model and an experiment, but those are not features.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model that builds directly on a replaced feature: feat-cli-util-v1, which feat-cli-util-v2 replaced. cli-xgb-v3, the other current model, uses only notes that are still in force.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md