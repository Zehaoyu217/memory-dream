## Q1
The only note of another project built directly on find-cu-sms-cost is find-ch-sms-call-gap in collections-channel-mix, which lists it as a source and says it builds on it. It also replaces find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on the bureau join and the 3-month utilisation feature. Through those it rests on the offer log, which is the other dataset in the chain.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is the only current-looking model that builds directly on a replaced feature. It builds on feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. csb-xgb-v2, the production model, builds on no replaced feature or dataset. Note that csb-lr-base carries no supersession marker, so it counts as current here.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026, directly or through notes built on it: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback. The cutover decision reaches it through bsm-cutoff-logit and exp-305.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
cu-uplift-v3 is in force now, since nothing supersedes it. It is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note of another project builds directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests directly on bsm-app-gbm-v10a, feat-bsm-score-map-v2 and feat-bsm-thin-file-flag. Through those it reaches four dataset notes: the dual-pull sample, the v10 cohorts, the application dev 2024 set and the v8 history.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model that builds directly on a replaced feature: feat-cli-util-v1, now replaced by feat-cli-util-v2. It has no supersession marker, so it counts as current here. cli-xgb-v3, the only other current CLI model, builds on no replaced feature.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md