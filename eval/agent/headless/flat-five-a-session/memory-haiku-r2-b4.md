## Q1
Both models build directly on three feature notes: feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour. cli-xgb-v1 also builds on ds-cli-holdout-2025q4, which is a dataset, not a feature.
Notes: work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q2
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (through exp-303), dec-bsm-cutover-2026q3 (through bsm-cutoff-logit, exp-305 and find-bsm-ks-parity) and dec-bsm-keep-v8-fallback (through exp-307). I checked the other decision notes for mentions of the cohort and found none beyond these.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q3
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, so cu-uplift-v3 is the note in force. It builds on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q4
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history, ds-bsm-app-dev-2024 (through bsm-app-gbm-v8), ds-bsm-dual-pull-sample, and ds-bsm-v10-cohorts-2026. The one note named only in words, feat-bsm-score-map-v2, names the dual-pull sample, which is already in the chain.
Notes: work/ds-bsm-v8-history.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md

## Q5
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md