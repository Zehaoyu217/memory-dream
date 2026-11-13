## Q1
Both `cli-logreg-baseline` and `cli-xgb-v1` build directly on `feat-cli-util-v1`, `feat-cli-spend-velocity` and `feat-cli-pay-behaviour`.
Notes: work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md, work/cli-logreg-baseline.md, work/cli-xgb-v1.md

## Q2
Three decision notes rest on `ds-bsm-v10-cohorts-2026`: `dec-bsm-isotonic-map` (through `exp-303-bureau-score-migration`), `dec-bsm-cutover-2026q3` and `dec-bsm-keep-v8-fallback` (both through `bsm-cutoff-logit` and `bsm-app-gbm-v10b`).
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q3
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, so `cu-uplift-v3` is the one in force. It is built on `cu-uplift-v2`, `exp-106-collections-uplift` and `feat-cu-bureau-delta`.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q4
`bsm-app-gbm-v10b` rests on four dataset notes: `ds-bsm-v8-history` and `ds-bsm-app-dev-2024` at the start, then `ds-bsm-dual-pull-sample` and `ds-bsm-v10-cohorts-2026`.
Notes: work/ds-bsm-v8-history.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md

## Q5
`fsm-churn-xgb-v2` and `fsm-spend-lgbm-v2` both build directly on `feat-fsm-payment-lag-v2` and `feat-fsm-spend-cv-30d`.
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md