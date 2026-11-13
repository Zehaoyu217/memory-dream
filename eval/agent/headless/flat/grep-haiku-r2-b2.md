## Q1
app-gbm-v2 builds on app-gbm-v1 and find-app-reject-inference-gain, which chains back through app-scorecard-v3, feat-app-thin-file, feat-app-velocity-apps, exp-501-application-scorecard and q-app-reject-inference. Its dataset notes are ds-app-applications-2024 and ds-app-reject-sample.
Notes: work/app-gbm-v2.md, work/app-gbm-v1.md, work/app-scorecard-v3.md, work/feat-app-thin-file.md, work/feat-app-velocity-apps.md, work/find-app-reject-inference-gain.md, work/exp-501-application-scorecard.md, work/q-app-reject-inference.md, work/ds-app-reject-sample.md, work/ds-app-applications-2024.md

## Q2
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: work/csb-lr-base.md, work/csb-xgb-v1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Three decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features (via find-bt-limit-leak and exp-104-limit-headroom-full), dec-bt-margin-label (via exp-107-margin-label, which reads bt.offer_log), and dec-bt-cut-mailer-top30 (via bt-xgb-v3 and dec-bt-margin-label).
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/find-bt-limit-leak.md, work/exp-104-limit-headroom-full.md, work/exp-107-margin-label.md, work/find-bt-margin-top30.md, work/bt-xgb-v3.md, work/ds-bt-offer-log.md

## Q4
The current in-force note is dec-cb-threshold-2500, which replaces dec-cb-adopt-banded-tiers and so ends the chain from dec-cb-extend-flat-pilot. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md

## Q5
bt-logit-baseline's full ancestry is ds-bt-bureau-join, feat-bt-util-3m, ds-bt-offer-log and q-bt-who-accepts. Its dataset notes are ds-bt-bureau-join and ds-bt-offer-log.
Notes: work/bt-logit-baseline.md, work/ds-bt-bureau-join.md, work/feat-bt-util-3m.md, work/ds-bt-offer-log.md, work/q-bt-who-accepts.md

## Q6
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-pay-behaviour (full-pay versus minimum-pay), feat-cli-spend-velocity and feat-cli-util-v1.
Notes: work/cli-logreg-baseline.md, work/cli-xgb-v1.md, work/feat-cli-pay-behaviour.md, work/feat-cli-spend-velocity.md, work/feat-cli-util-v1.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-cutover-2026q3 (via exp-305) and dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap).
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md, work/ds-bsm-v10-cohorts-2026.md

## Q8
The current in-force note is cu-uplift-v3, which replaces cu-uplift-v2 and is not replaced. It builds on cu-uplift-v2 (the T-learner and isotonic calibration), exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/cu-uplift-v1.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b's ancestry is bsm-app-gbm-v10a, bsm-app-gbm-v8, feat-bsm-score-map-v1, feat-bsm-score-map-v2, exp-301-bureau-score-migration, feat-bsm-thin-file-flag, feat-bsm-score-missing-impute and q-bsm-psi-shift. Its dataset notes are ds-bsm-app-dev-2024, ds-bsm-v8-history, ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026.
Notes: work/bsm-app-gbm-v10b.md, work/bsm-app-gbm-v10a.md, work/bsm-app-gbm-v8.md, work/feat-bsm-score-map-v1.md, work/feat-bsm-score-map-v2.md, work/exp-301-bureau-score-migration.md, work/feat-bsm-thin-file-flag.md, work/feat-bsm-score-missing-impute.md, work/q-bsm-psi-shift.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md

## Q10
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-spend-lgbm-v2.md, work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md