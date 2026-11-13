## Q1
The dataset notes app-gbm-v2 rests on, directly or through other notes, are ds-app-applications-2024 and ds-app-reject-sample. The second is reached through exp-501-application-scorecard and the reject-inference question.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band. csb-xgb-v1 also uses feat-csb-deposit-volatility, which csb-lr-base only reaches through exp-203.
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, dec-bt-margin-label, dec-pa-6m-default and dec-pa-no-12m-subprime. Another 26 unplaced notes in work/ may also rest on it, but no note links them to it, so they are not counted here.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-cut-mailer-top30.md, work/dec-bt-margin-label.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The note in force is dec-cb-threshold-2500, which sets the top tier at $2,500. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through feat-bt-util-3m and q-bt-who-accepts.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md

## Q6
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback. Another 26 unplaced notes in work/ may also rest on it, but no note links them to it, so they are not counted here.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q8
The note in force is cu-uplift-v3, a T-learner with the bureau 3-month delta. It builds on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-app-dev-2024 and ds-bsm-v8-history. All four are reached through bsm-app-gbm-v10a, feat-bsm-score-map-v2 or their own upstream chains. The path for ds-bsm-app-dev-2024 is inferred from the folder, not confirmed by a note listing.
Notes: work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md

## Q10
Both fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md