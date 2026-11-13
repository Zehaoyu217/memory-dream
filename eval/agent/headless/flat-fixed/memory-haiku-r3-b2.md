## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. It reaches them through app-scorecard-v3, exp-501-application-scorecard, and q-app-reject-inference.
Notes: work/app-gbm-v2.md, work/ds-app-applications-2024.md, work/ds-app-reject-sample.md, work/app-gbm-v1.md, work/find-app-reject-inference-gain.md, work/exp-501-application-scorecard.md, work/app-scorecard-v3.md

## Q2
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: work/csb-lr-base.md, work/csb-xgb-v1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-margin-label, dec-bt-cut-mailer-top30, dec-pa-6m-default and dec-pa-no-12m-subprime. None rests on it directly; each reaches it through a chain of other notes.
Notes: work/ds-bt-offer-log.md, work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The line ends at dec-cb-threshold-2500, the decision in force (dec-cb-extend-flat-pilot → dec-cb-adopt-banded-tiers → dec-cb-threshold-2500). It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-extend-flat-pilot.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through feat-bt-util-3m and q-bt-who-accepts.
Notes: work/bt-logit-baseline.md, work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md, work/feat-bt-util-3m.md, work/q-bt-who-accepts.md

## Q6
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: work/cli-logreg-baseline.md, work/cli-xgb-v1.md, work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback. The first is reached through the feature and model notes, and the other two through the bsm-app-gbm-v10b and bsm-cutoff-logit chain.
Notes: work/ds-bsm-v10-cohorts-2026.md, work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q8
The line ends at cu-uplift-v3, the version in force (cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3). It builds on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v1.md, work/cu-uplift-v2.md, work/cu-uplift-v3.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-v8-history and ds-bsm-app-dev-2024. It reaches them through bsm-app-gbm-v10a, feat-bsm-score-map-v2, feat-bsm-thin-file-flag and bsm-app-gbm-v8.
Notes: work/bsm-app-gbm-v10b.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md, work/ds-bsm-v8-history.md, work/ds-bsm-app-dev-2024.md, work/bsm-app-gbm-v10a.md, work/feat-bsm-score-map-v2.md, work/feat-bsm-thin-file-flag.md, work/bsm-app-gbm-v8.md

## Q10
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/fsm-churn-xgb-v2.md, work/fsm-spend-lgbm-v2.md, work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md