## Q1
app-gbm-v2 rests on two dataset notes, ds-app-applications-2024 and ds-app-reject-sample, the first through app-scorecard-v3 and exp-501, the second directly through exp-501 and find-app-reject-inference-gain.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label through the BT model and finding chain, and dec-pa-6m-default and dec-pa-no-12m-subprime through the PA chain.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-cut-mailer-top30.md, work/dec-bt-margin-label.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The line runs dec-cb-extend-flat-pilot → dec-cb-adopt-banded-tiers → dec-cb-threshold-2500, and dec-cb-threshold-2500 is the one in force. It is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through feat-bt-util-3m and q-bt-who-accepts.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md

## Q6
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map directly through the BSM chain, and dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback through bsm-app-gbm-v10b.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q8
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, and cu-uplift-v3 is the one in force. It is built on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-app-dev-2024 and ds-bsm-v8-history. The first two are reached through the direct parents and the last two through bsm-app-gbm-v8 and the score-map chain.
Notes: work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md

## Q10
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md