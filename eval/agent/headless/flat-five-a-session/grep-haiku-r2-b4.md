## Q1
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour (the full-pay versus minimum-pay feature).
Notes: work/cli-logreg-baseline.md, work/cli-xgb-v1.md, work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q2
dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback rest on ds-bsm-v10-cohorts-2026, the first two through exp-303 and bsm-cutoff-logit/find-bsm-ks-parity, and the third through find-bsm-thin-file-gap and bsm-app-gbm-v10b. dec-bsm-linear-map does not, because it predates the cohort and rests only on the dual-pull sample and exp-301.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md, work/ds-bsm-v10-cohorts-2026.md

## Q3
cu-uplift-v3 is the one in force: cu-uplift-v1 was replaced by cu-uplift-v2, which was replaced by cu-uplift-v3, and no later version appears in the notes. cu-uplift-v3 is built on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v1.md, work/cu-uplift-v2.md, work/cu-uplift-v3.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q4
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history, ds-bsm-app-dev-2024, ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026.
Notes: work/bsm-app-gbm-v10b.md, work/bsm-app-gbm-v10a.md, work/bsm-app-gbm-v8.md, work/feat-bsm-score-map-v1.md, work/feat-bsm-score-map-v2.md, work/feat-bsm-thin-file-flag.md, work/feat-bsm-score-missing-impute.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v8-history.md, work/ds-bsm-v10-cohorts-2026.md

## Q5
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-spend-lgbm-v2.md, work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md