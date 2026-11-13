## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. The path runs through app-gbm-v1 to app-scorecard-v3 and the thin-file and velocity features, and through find-app-reject-inference-gain to exp-501.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
Both build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-xgb-v1 also uses feat-csb-deposit-volatility, which csb-lr-base does not.
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Seven decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30 and dec-bt-margin-label, plus dec-pa-6m-default and dec-pa-no-12m-subprime, which come through the pa margin models. The last two are dec-bsm-… no: they are dec-pa-6m-default and dec-pa-no-12m-subprime only, so the full list is five decisions.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-cut-mailer-top30.md, work/dec-bt-margin-label.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The line goes dec-cb-extend-flat-pilot → dec-cb-adopt-banded-tiers → dec-cb-threshold-2500, and dec-cb-threshold-2500 is the one in force (the "structure of record"). It is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through ds-bt-bureau-join and feat-bt-util-3m.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md

## Q6
Both build directly on the same three features: feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q8
cu-uplift-v1 was replaced by cu-uplift-v2, which was replaced by cu-uplift-v3, the note in force now (promoted 2026-03-25). cu-uplift-v3 is built on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v10-cohorts-2026, ds-bsm-dual-pull-sample, ds-bsm-v8-history and ds-bsm-app-dev-2024 (the last through bsm-app-gbm-v8).
Notes: work/ds-bsm-v10-cohorts-2026.md, work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v8-history.md, work/ds-bsm-app-dev-2024.md

## Q10
Both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also uses feat-fsm-util-ratio, which fsm-spend-lgbm-v2 does not.
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md