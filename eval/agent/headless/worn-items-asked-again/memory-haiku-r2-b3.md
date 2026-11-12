## Q1
Only one note in another project is built directly on find-cu-sms-cost: collections-channel-mix/find-ch-sms-call-gap, which lists it among its direct sources.
Notes: collections-uplift/find-cu-sms-cost.md, collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on the dataset ds-bt-bureau-join. Through feat-bt-util-3m it also rests on ds-bt-offer-log, so those are the two dataset notes.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-spend-velocity and feat-cli-util-v1. The logistic model also uses feat-cli-pay-behaviour, and the XGBoost model also uses the holdout dataset ds-cli-holdout-2025q4.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is the only current model in churn-small-business that builds directly on a replaced note. It uses feat-csb-spend-raw, which has been replaced by feat-csb-spend-sa-v2.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback. The last two come through intermediate notes such as bsm-cutoff-logit, exp-305 and exp-307.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The note in force at the end of the cu-uplift-v1 line is cu-uplift-v3. It is built directly on cu-uplift-v2 (replaced), exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note in another project is built directly on feat-cli-util-v2: limit-decrease-policy/feat-cld-risk-band-v2, which uses the utilisation slope from it.
Notes: credit-line-increase/feat-cli-util-v2.md, limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on five dataset notes: ds-app-applications-2024 (application-scorecard), ds-bsm-app-dev-2024, ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026 and ds-bsm-v8-history. Four of them are reached through intermediate notes such as bsm-app-gbm-v8, feat-bsm-score-map-v1 and bsm-app-gbm-v10a.
Notes: application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/bsm-app-gbm-v10b.md

## Q9
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. The churn model also uses feat-fsm-util-ratio.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md, feature-store-migration/feat-fsm-util-ratio.md

## Q10
cli-logreg-baseline is the only current model in credit-line-increase that builds directly on a replaced note. It uses feat-cli-util-v1, which was replaced by feat-cli-util-v2.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md