## Q1
app-gbm-v2 rests on two dataset notes, ds-app-applications-2024 and ds-app-reject-sample, both reached through app-gbm-v1, find-app-reject-inference-gain and the scorecard chain behind them.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
csb-lr-base and csb-xgb-v1 both build on two feature notes directly: feat-csb-spend-raw and feat-csb-tenure-band.
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, dec-bt-margin-label, dec-pa-6m-default and dec-pa-no-12m-subprime. About 90 other work notes may also rest on it, but they have no recorded link to it, so I did not count them.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-cut-mailer-top30.md, work/dec-bt-margin-label.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The note in force now is dec-cb-threshold-2500, which sets the top tier at $2,500 for the Q3 2026 launch. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes, ds-bt-bureau-join directly and ds-bt-offer-log through feat-bt-util-3m and q-bt-who-accepts.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md