## Q1
Both build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour (the full-pay versus minimum-pay feature). cli-logreg-baseline uses all three, and cli-xgb-v1 uses the same three plus the 2025-Q4 holdout set.
Notes: work/cli-logreg-baseline.md, work/cli-xgb-v1.md, work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q2
Three decisions rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (directly via exp-303), dec-bsm-cutover-2026q3 (via bsm-cutoff-logit, feat-bsm-v10-band and exp-306/find-bsm-ks-parity), and dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap).
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md, work/ds-bsm-v10-cohorts-2026.md, work/exp-303-bureau-score-migration.md, work/feat-bsm-v10-band.md, work/bsm-cutoff-logit.md, work/exp-305-bureau-score-migration.md, work/exp-306-bureau-score-migration.md, work/find-bsm-ks-parity.md, work/feat-bsm-score-missing-impute.md, work/bsm-app-gbm-v10a.md, work/exp-304-bureau-score-migration.md, work/feat-bsm-thin-file-flag.md, work/find-bsm-thin-file-gap.md, work/exp-307-bureau-score-migration.md, work/bsm-app-gbm-v10b.md

## Q3
cu-uplift-v3 is in force; it is built on exp-106-collections-uplift, feat-cu-bureau-delta and the calibrated uplift model used for routing (cu-uplift-v2, which it replaces).
Notes: work/cu-uplift-v1.md, work/cu-uplift-v2.md, work/cu-uplift-v3.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q4
bsm-app-gbm-v10b rests on the four dataset notes ds-bsm-v10-cohorts-2026, ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024 and ds-bsm-v8-history, which chain back to ds-bsm-v8-history as the root.
Notes: work/bsm-app-gbm-v10b.md, work/bsm-app-gbm-v10a.md, work/bsm-app-gbm-v8.md, work/feat-bsm-score-map-v2.md, work/feat-bsm-score-map-v1.md, work/exp-301-bureau-score-migration.md, work/feat-bsm-score-missing-impute.md, work/feat-bsm-thin-file-flag.md, work/ds-bsm-v10-cohorts-2026.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md

## Q5
Both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-spend-lgbm-v2.md, work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md

I created a scratch file at <path> during the search, outside the notes folder, and have deleted it. Nothing else was written.