## Q1
cli-logreg-baseline and cli-xgb-v1 both build directly on three feature notes: feat-cli-pay-behaviour (the full-pay versus minimum-pay feature), feat-cli-spend-velocity, and feat-cli-util-v1.
Notes: work/cli-logreg-baseline.md, work/cli-xgb-v1.md, work/feat-cli-pay-behaviour.md, work/feat-cli-spend-velocity.md, work/feat-cli-util-v1.md

## Q2
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-cutover-2026q3 (via bsm-cutoff-logit and exp-305), dec-bsm-isotonic-map (via exp-303), and dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap/exp-304). dec-bsm-linear-map does not, because it rests only on exp-301 and the dual-pull sample.
Notes: work/dec-bsm-cutover-2026q3.md, work/dec-bsm-isotonic-map.md, work/dec-bsm-keep-v8-fallback.md, work/bsm-cutoff-logit.md, work/exp-305-bureau-score-migration.md, work/exp-303-bureau-score-migration.md, work/exp-307-bureau-score-migration.md, work/find-bsm-thin-file-gap.md, work/exp-304-bureau-score-migration.md, work/bsm-app-gbm-v10b.md, work/bsm-app-gbm-v10a.md, work/feat-bsm-score-missing-impute.md, work/feat-bsm-thin-file-flag.md, work/ds-bsm-v10-cohorts-2026.md

## Q3
The line runs cu-uplift-v1, then cu-uplift-v2 (replaced 2026-03-06), then cu-uplift-v3, which is in force because no later cu-uplift note exists. cu-uplift-v3 builds on cu-uplift-v2 (the calibrated uplift model used for routing), exp-106-collections-uplift, and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/cu-uplift-v1.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q4
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history (via ds-bsm-app-dev-2024 and the dual-pull sample), ds-bsm-app-dev-2024 (via bsm-app-gbm-v8), ds-bsm-dual-pull-sample (via feat-bsm-score-map-v1/v2 and exp-301), and ds-bsm-v10-cohorts-2026 (via feat-bsm-score-missing-impute and feat-bsm-thin-file-flag).
Notes: work/bsm-app-gbm-v10b.md, work/bsm-app-gbm-v10a.md, work/bsm-app-gbm-v8.md, work/feat-bsm-score-map-v2.md, work/feat-bsm-score-map-v1.md, work/feat-bsm-thin-file-flag.md, work/feat-bsm-score-missing-impute.md, work/exp-301-bureau-score-migration.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md

## Q5
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-spend-lgbm-v2.md, work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md