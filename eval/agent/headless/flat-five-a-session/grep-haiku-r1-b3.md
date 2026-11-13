## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 (the 2024 application base) and ds-app-reject-sample (the 8,400 manual approvals used for reject inference). It reaches them through app-gbm-v1, find-app-reject-inference-gain, exp-501-application-scorecard and q-app-reject-inference.
Notes: work/app-gbm-v2.md, work/app-gbm-v1.md, work/app-scorecard-v3.md, work/feat-app-thin-file.md, work/feat-app-velocity-apps.md, work/feat-app-util-new.md, work/find-app-reject-inference-gain.md, work/exp-501-application-scorecard.md, work/q-app-reject-inference.md, work/ds-app-reject-sample.md, work/ds-app-applications-2024.md

## Q2
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: work/csb-lr-base.md, work/csb-xgb-v1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Three decisions rest on ds-bt-offer-log: dec-bt-drop-post-offer-features (via find-bt-limit-leak, exp-104-limit-headroom-full, bt-xgb-v1, feat-bt-util-3m), dec-bt-margin-label (via find-bt-margin-top30, exp-107-margin-label, bt-xgb-v2, feat-bt-util-3m), and dec-bt-cut-mailer-top30 (via bt-xgb-v3 and dec-bt-margin-label).
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/find-bt-limit-leak.md, work/exp-104-limit-headroom-full.md, work/bt-xgb-v1.md, work/find-bt-margin-top30.md, work/exp-107-margin-label.md, work/bt-xgb-v2.md, work/bt-xgb-v3.md, work/feat-bt-util-3m.md, work/ds-bt-offer-log.md

## Q4
The line ends at dec-cb-threshold-2500 (top tier at $2,500), which is in force and has no later replacement. It is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-extend-flat-pilot.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-threshold-2500.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on ds-bt-bureau-join directly and on ds-bt-offer-log, which it reaches through ds-bt-bureau-join and feat-bt-util-3m (ds-bt-offer-log itself builds on q-bt-who-accepts).
Notes: work/bt-logit-baseline.md, work/ds-bt-bureau-join.md, work/feat-bt-util-3m.md, work/ds-bt-offer-log.md, work/q-bt-who-accepts.md