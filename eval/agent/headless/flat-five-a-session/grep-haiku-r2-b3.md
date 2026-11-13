## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 (the base 2024 application set) and ds-app-reject-sample. Every path back runs through app-gbm-v1, app-scorecard-v3 or exp-501-application-scorecard, and both datasets trace to the start.
Notes: work/app-gbm-v2.md, work/app-gbm-v1.md, work/find-app-reject-inference-gain.md, work/exp-501-application-scorecard.md, work/app-scorecard-v3.md, work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
The two feature notes built on directly by both csb-lr-base and csb-xgb-v1 are feat-csb-spend-raw and feat-csb-tenure-band. I took the "tenure bands feature" in csb-lr-base to be feat-csb-tenure-band.
Notes: work/csb-lr-base.md, work/csb-xgb-v1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log, directly or through notes built on it: dec-bt-drop-post-offer-features, dec-bt-margin-label, dec-bt-cut-mailer-top30, dec-pa-6m-default and dec-pa-no-12m-subprime. The first two chain through the bt-xgb models and feat-bt-util-3m. The pa decisions chain through pa-bal-forecast-v1 and bt-xgb-v3.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md, work/ds-bt-offer-log.md, work/feat-bt-util-3m.md, work/bt-xgb-v1.md, work/bt-xgb-v2.md, work/bt-xgb-v3.md, work/pa-bal-forecast-v1.md

## Q4
dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was in turn replaced by dec-cb-threshold-2500 (2026-03-10). That is the note in force, and it builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-extend-flat-pilot.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join and ds-bt-offer-log. feat-bt-util-3m also builds on ds-bt-offer-log, and that chain ends at the question note q-bt-who-accepts, which is not a dataset.
Notes: work/bt-logit-baseline.md, work/ds-bt-bureau-join.md, work/feat-bt-util-3m.md, work/ds-bt-offer-log.md, work/q-bt-who-accepts.md