## Q1
app-gbm-v2 rests on two dataset notes: ds-app-applications-2024 and ds-app-reject-sample, both reached through the scorecard and reject-inference chain.
Notes: work/ds-app-applications-2024.md, work/ds-app-reject-sample.md

## Q2
csb-lr-base and csb-xgb-v1 both build directly on feat-csb-spend-raw (trailing three-month card spend) and feat-csb-tenure-band (five tenure bands).
Notes: work/feat-csb-spend-raw.md, work/feat-csb-tenure-band.md

## Q3
Five decision notes rest on ds-bt-offer-log: dec-bt-drop-post-offer-features, dec-bt-cut-mailer-top30, dec-bt-margin-label, dec-pa-6m-default and dec-pa-no-12m-subprime. Another 26 notes in work/ may also depend on it, but the memory does not link them to a chain, so I left them out.
Notes: work/dec-bt-drop-post-offer-features.md, work/dec-bt-cut-mailer-top30.md, work/dec-bt-margin-label.md, work/dec-pa-6m-default.md, work/dec-pa-no-12m-subprime.md

## Q4
dec-cb-extend-flat-pilot was superseded by dec-cb-adopt-banded-tiers, which was superseded by dec-cb-threshold-2500, the decision in force now. dec-cb-threshold-2500 is built on dec-cb-adopt-banded-tiers, exp-206-breakeven-sim and find-cb-breakeven-lift.
Notes: work/dec-cb-threshold-2500.md, work/dec-cb-adopt-banded-tiers.md, work/exp-206-breakeven-sim.md, work/find-cb-breakeven-lift.md

## Q5
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through feat-bt-util-3m and q-bt-who-accepts.
Notes: work/ds-bt-bureau-join.md, work/ds-bt-offer-log.md

## Q6
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-util-v1 (3-month and peak utilisation), feat-cli-spend-velocity (30-day over 90-day purchase ratio) and feat-cli-pay-behaviour (full-pay versus minimum-pay share).
Notes: work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/feat-cli-pay-behaviour.md

## Q7
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback.
Notes: work/dec-bsm-isotonic-map.md, work/dec-bsm-cutover-2026q3.md, work/dec-bsm-keep-v8-fallback.md

## Q8
cu-uplift-v1 was superseded by cu-uplift-v2, which was superseded by cu-uplift-v3, the model in force now. cu-uplift-v3 is built on cu-uplift-v2, exp-106-collections-uplift and feat-cu-bureau-delta.
Notes: work/cu-uplift-v3.md, work/cu-uplift-v2.md, work/exp-106-collections-uplift.md, work/feat-cu-bureau-delta.md

## Q9
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026, ds-bsm-app-dev-2024 and ds-bsm-v8-history.
Notes: work/ds-bsm-dual-pull-sample.md, work/ds-bsm-v10-cohorts-2026.md, work/ds-bsm-app-dev-2024.md, work/ds-bsm-v8-history.md

## Q10
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 (payment lag with UTC timestamps) and feat-fsm-spend-cv-30d (30-day coefficient of variation of approved spend).
Notes: work/feat-fsm-payment-lag-v2.md, work/feat-fsm-spend-cv-30d.md