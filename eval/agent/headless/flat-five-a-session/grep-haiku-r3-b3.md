## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 (the 2024 application base) and ds-app-reject-sample (the 8,400 manual approvals). It reaches them through app-gbm-v1, find-app-reject-inference-gain, app-scorecard-v3, feat-app-thin-file, feat-app-velocity-apps, feat-app-util-new, exp-501-application-scorecard and q-app-reject-inference.
Notes: work/app-gbm-v2.md, work/app-gbm-v1.md, work/find-app-reject-inference-gain.md, work/exp-501-application-scorecard.md, work/q-app-reject-inference.md, work/app-scorecard-v3.md, work/feat-app-thin-file.md, work/feat-app-velocity-apps.md, work/feat-app-util-new.md, work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw (trailing three-month card spend) and feat-csb-tenure-band (the five tenure bands).
Notes: work/csb-lr-base.md, work/csb-xgb-v1.md, work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Three decisions rest on ds-bt-offer-log: dec-bt-drop-post-offer-features (via exp-104-limit-headroom-full and find-bt-limit-leak), dec-bt-margin-label (via exp-107-margin-label, which uses the depth-5 bt-xgb-v2 model), and dec-bt-cut-mailer-top30 (via bt-xgb-v3, which builds on dec-bt-margin-label).
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-margin-label.md, work/dec-bt-cut-mailer-top30.md, work/ds-bt-offer-log.md, work/exp-104-limit-headroom-full.md, work/find-bt-limit-leak.md, work/exp-107-margin-label.md, work/find-bt-margin-top30.md, work/bt-xgb-v2.md, work/bt-xgb-v3.md, work/feat-bt-util-3m.md, work/feat-bt-util-trend-v2.md, work/exp-103-util-trend.md, work/feat-bt-revolve-share.md

## Q4
The line ends at dec-cb-threshold-2500, which is in force (its own text says it is the structure of record). It is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift. dec-cb-adopt-banded-tiers replaced dec-cb-extend-flat-pilot.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/dec-cb-extend-flat-pilot.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log both through ds-bt-bureau-join and through feat-bt-util-3m.
Notes: work/bt-logit-baseline.md, work/ds-bt-bureau-join.md, work/feat-bt-util-3m.md, work/ds-bt-offer-log.md