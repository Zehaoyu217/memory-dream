## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample. It gets them through app-gbm-v1, app-scorecard-v3, the thin-file and velocity features, find-app-reject-inference-gain and exp-501.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
Both models build directly on two features: feat-csb-spend-raw and feat-csb-tenure-band. csb-xgb-v1 also uses feat-csb-deposit-volatility, but csb-lr-base does not.
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decisions rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, dec-bt-margin-label, dec-pa-6m-default and dec-pa-no-12m-subprime.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-cut-mailer-top30.md, work/dec-bt-margin-label.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
The line runs dec-cb-extend-flat-pilot → dec-cb-adopt-banded-tiers → dec-cb-threshold-2500, so dec-cb-threshold-2500 is in force now. It builds on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes. It uses ds-bt-bureau-join directly, and reaches ds-bt-offer-log through ds-bt-bureau-join and feat-bt-util-3m.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md

## Q6
Both models build directly on the same three features: feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q7
Three decisions rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q8
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, so cu-uplift-v3 is in force now. It builds on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-v8-history and ds-bsm-app-dev-2024. It reaches them through v10a, v8, the score maps, the thin-file and missing-score features, and exp-301.
Notes: work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md, work/ds-bsm-v8-history.md, work/ds-bsm-app-dev-2024.md

## Q10
Both models build directly on two features: feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. Only fsm-churn-xgb-v2 also uses feat-fsm-util-ratio.
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md