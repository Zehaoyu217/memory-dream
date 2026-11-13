## Q1
The notes for app-gbm-v2 rest on two dataset roots: ds-app-applications-2024 (214,600 applications, Jan–Dec 2024) through the scorecard lineage, and ds-app-reject-sample (8,400 manually approved rejects) through exp-501-application-scorecard and find-app-reject-inference-gain.
Notes: work/app-gbm-v2.md, work/app-gbm-v1.md, work/app-scorecard-v3.md, work/find-app-reject-inference-gain.md, work/exp-501-application-scorecard.md, work/ds-app-reject-sample.md, work/ds-app-applications-2024.md

## Q2
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: work/csb-lr-base.md, work/csb-xgb-v1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Four decision notes rest on ds-bt-offer-log. dec-bt-drop-post-offer-features and dec-bt-margin-label rest on it through bt-xgb-v1/v2 and exp-104/105/107, and dec-bt-cut-mailer-top30 rests on it through bt-xgb-v3. dec-pa-6m-default rests on it through find-pa-margin-corrected, pa-margin-v2, pa-bal-forecast-v1 and bt-xgb-v3.
Notes: work/ds-bt-offer-log.md, work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/dec-pa-6m-default.md, work/find-pa-margin-corrected.md, work/pa-margin-v2.md, work/pa-bal-forecast-v1.md, work/bt-xgb-v3.md

## Q4
The note in force at the end of the line is dec-cb-threshold-2500, which replaced dec-cb-adopt-banded-tiers. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-extend-flat-pilot.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset roots: ds-bt-offer-log, directly and via feat-bt-util-3m, and ds-bt-bureau-join, which builds on the offer log.
Notes: work/bt-logit-baseline.md, work/feat-bt-util-3m.md, work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md

## Q6
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1.
Notes: work/cli-logreg-baseline.md, work/cli-xgb-v1.md, work/feat-cli-pay-behaviour.md, work/feat-cli-spend-velocity.md, work/feat-cli-util-v1.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-cutover-2026q3 (via exp-305, bsm-cutoff-logit and feat-bsm-v10-band), and dec-bsm-keep-v8-fallback (via exp-304 and exp-307, which trace back to the cohorts through bsm-app-gbm-v10a/v10b). dec-bsm-linear-map does not, since it rests on exp-301 and the dual-pull sample.
Notes: work/ds-bsm-v10-cohorts-2026.md, work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md, work/exp-303-bureau-score-migration.md, work/exp-305-bureau-score-migration.md, work/exp-304-bureau-score-migration.md, work/exp-307-bureau-score-migration.md

## Q8
The note in force at the end of the cu-uplift-v1 line is cu-uplift-v3, which replaced cu-uplift-v2 (itself a replacement of cu-uplift-v1). cu-uplift-v3 builds on cu-uplift-v2 and exp-106-collections-uplift.
Notes: work/cu-uplift-v1.md, work/cu-uplift-v2.md, work/cu-uplift-v3.md, work/exp-106-collections-uplift.md

## Q9
bsm-app-gbm-v10b rests on four dataset roots: ds-bsm-v8-history (the root), ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024 (via bsm-app-gbm-v8) and ds-bsm-v10-cohorts-2026.
Notes: work/bsm-app-gbm-v10b.md, work/bsm-app-gbm-v10a.md, work/bsm-app-gbm-v8.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md, work/feat-bsm-score-map-v2.md, work/feat-bsm-thin-file-flag.md, work/feat-bsm-score-missing-impute.md

## Q10
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-spend-lgbm-v2.md, work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md