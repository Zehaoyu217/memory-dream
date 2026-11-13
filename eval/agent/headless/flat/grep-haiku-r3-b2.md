## Q1
app-gbm-v2 rests on two dataset notes. ds-app-applications-2024 is the root, and ds-app-reject-sample sits on it and feeds the reject-inference chain.
Notes: memory/work/ds-app-applications-2024.md, memory/work/ds-app-reject-sample.md

## Q2
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band (the five tenure bands feature).
Notes: memory/work/feat-csb-spend-raw.md, memory/work/feat-csb-tenure-band.md

## Q3
Three decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features (via find-bt-limit-leak), dec-bt-margin-label (via exp-107-margin-label and find-bt-margin-top30, both on bt-xgb-v2), and dec-bt-cut-mailer-top30 (via bt-xgb-v3, which is trained on the depth-5 model bt-xgb-v2). The helper closure missed the margin and bt-xgb-v3 branches, so I checked those by reading the lines.
Notes: memory/work/dec-bt-drop-post-offer-features.md, memory/work/dec-bt-margin-label.md, memory/work/dec-bt-cut-mailer-top30.md, memory/work/bt-xgb-v3.md, memory/work/exp-107-margin-label.md, memory/work/find-bt-margin-top30.md

## Q4
The in-force note is dec-cb-threshold-2500. It replaced dec-cb-adopt-banded-tiers, which had replaced dec-cb-extend-flat-pilot, and nothing replaces it. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: memory/work/dec-cb-extend-flat-pilot.md, memory/work/dec-cb-adopt-banded-tiers.md, memory/work/dec-cb-threshold-2500.md, memory/work/exp-206-breakeven-sim.md, memory/work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join, which builds on the bt offer log, and ds-bt-offer-log itself, which is reached directly through feat-bt-util-3m.
Notes: memory/work/ds-bt-bureau-join.md, memory/work/ds-bt-offer-log.md

## Q6
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-pay-behaviour (the full-pay versus minimum-pay feature), feat-cli-spend-velocity and feat-cli-util-v1.
Notes: memory/work/feat-cli-pay-behaviour.md, memory/work/feat-cli-spend-velocity.md, memory/work/feat-cli-util-v1.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-cutover-2026q3 (via bsm-cutoff-logit, exp-305 and find-bsm-ks-parity), and dec-bsm-keep-v8-fallback (via exp-307). dec-bsm-linear-map does not qualify, because its experiment exp-301 does not build on the v10 cohorts.
Notes: memory/work/dec-bsm-isotonic-map.md, memory/work/dec-bsm-cutover-2026q3.md, memory/work/dec-bsm-keep-v8-fallback.md, memory/work/ds-bsm-v10-cohorts-2026.md, memory/work/exp-303-bureau-score-migration.md, memory/work/exp-307-bureau-score-migration.md

## Q8
The in-force note is cu-uplift-v3. It replaced cu-uplift-v2, which had replaced cu-uplift-v1, and nothing replaces it. It builds on cu-uplift-v2 (the calibrated uplift model used for routing), exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: memory/work/cu-uplift-v1.md, memory/work/cu-uplift-v2.md, memory/work/cu-uplift-v3.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history, ds-bsm-app-dev-2024, ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026.
Notes: memory/work/ds-bsm-v8-history.md, memory/work/ds-bsm-app-dev-2024.md, memory/work/ds-bsm-dual-pull-sample.md, memory/work/ds-bsm-v10-cohorts-2026.md

## Q10
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: memory/work/feat-fsm-payment-lag-v2.md, memory/work/feat-fsm-spend-cv-30d.md