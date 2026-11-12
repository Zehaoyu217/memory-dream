## Q1
Only one note in another project builds directly on find-cu-sms-cost: find-ch-sms-call-gap in collections-channel-mix, which lists it alongside exp-504 and find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through both ds-bt-bureau-join and feat-bt-util-3m. The chain ends at q-bt-who-accepts, which is a question note, not a dataset.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-pay-behaviour (the full-pay versus minimum-pay feature), feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is the only current model that builds directly on a replaced feature. It uses feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2 from January 2026, and it remains on as the monitoring challenger.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026. dec-bsm-isotonic-map builds on exp-303, and dec-bsm-cutover-2026q3 builds on exp-305 through bsm-cutoff-logit and feat-bsm-v10-band. dec-bsm-keep-v8-fallback builds on exp-307, which rests on the v10b model, and on find-bsm-thin-file-gap. dec-bsm-linear-map does not reach the cohorts; it rests only on the dual-pull experiment.
Notes: bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line is cu-uplift-v1, replaced by cu-uplift-v2, which was replaced by cu-uplift-v3. cu-uplift-v3 is in force and builds on the calibrated uplift model used for routing (cu-uplift-v2), exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only feat-cld-risk-band-v2 in limit-decrease-policy builds directly on feat-cli-util-v2 of credit-line-increase.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history, ds-bsm-app-dev-2024, ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026. They are reached through bsm-app-gbm-v10a, bsm-app-gbm-v8, feat-bsm-score-map-v1/v2, feat-bsm-score-missing-impute, exp-301 and feat-bsm-thin-file-flag.
Notes: bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md

## Q9
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model that builds directly on a replaced feature: feat-cli-util-v1, which feat-cli-util-v2 replaced. Its note has no superseded line, though dec-cli-cutoff-2025 that it was used with has been superseded.
Notes: credit-line-increase/cli-logreg-baseline.md