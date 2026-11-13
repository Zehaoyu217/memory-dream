## Q1
app-gbm-v2 rests on two dataset notes: `ds-app-applications-2024`, reached through app-gbm-v1, app-scorecard-v3 and exp-501, and `ds-app-reject-sample`, reached through exp-501 and find-app-reject-inference-gain.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
Both csb-lr-base and csb-xgb-v1 build directly on `feat-csb-spend-raw` and `feat-csb-tenure-band`. Note that `feat-csb-spend-raw` is itself superseded by `feat-csb-spend-sa-v2`.
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-margin-label, dec-bt-cut-mailer-top30, dec-pa-6m-default and dec-pa-no-12m-subprime. The first two sit on it through bt-xgb-v2 and exp-107-margin-label, and the three others through their own chains of models and findings.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The note in force at the end of the line is `dec-cb-threshold-2500`, which sets the top tier at $2,500 for the Q3 2026 launch. It builds on `dec-cb-adopt-banded-tiers`, `exp-206-breakeven-sim` and `find-cb-breakeven-lift`.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: `ds-bt-bureau-join` directly, and `ds-bt-offer-log` through both ds-bt-bureau-join and feat-bt-util-3m.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md