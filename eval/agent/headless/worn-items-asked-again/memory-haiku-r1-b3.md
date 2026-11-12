## Q1
Only one note in another project is built directly on find-cu-sms-cost: collections-channel-mix/find-ch-sms-call-gap, which also rests on exp-504 and find-ch-sms-matches-call.
Notes: collections-uplift/find-cu-sms-cost.md, collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through feat-bt-util-3m and ds-bt-bureau-join.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current and builds directly on feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2 from January 2026.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v1 was replaced by cu-uplift-v2, which was replaced by cu-uplift-v3, the note in force now. cu-uplift-v3 is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v1.md, collections-uplift/cu-uplift-v2.md, collections-uplift/cu-uplift-v3.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only limit-decrease-policy/feat-cld-risk-band-v2 is built directly on feat-cli-util-v2 from another project.
Notes: credit-line-increase/feat-cli-util-v2.md, limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on five dataset notes: ds-app-applications-2024, ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024, ds-bsm-v10-cohorts-2026 and ds-bsm-v8-history.
Notes: application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model that builds directly on a replaced feature: feat-cli-util-v1, now superseded by feat-cli-util-v2.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md