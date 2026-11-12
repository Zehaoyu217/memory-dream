## Q1
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q2
churn-lr-base-2025 is the only current model in churn-2025 that builds directly on a replaced feature. It is built on feat-c25-util-v1, which feat-c25-util-v2 replaced in March 2025.
Notes: churn-2025/churn-lr-base-2025.md, churn-2025/feat-c25-util-v1.md, churn-2025/feat-c25-util-v2.md

## Q3
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-cutover-2026q3 (via exp-305, which runs through feat-bsm-v10-band and exp-303), and dec-bsm-keep-v8-fallback (via exp-307, which runs through bsm-app-gbm-v10b and feat-bsm-thin-file-flag).
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q4
The line runs cr-lgbm-v1 (replaced by cr-lgbm-v2) and then cr-lgbm-v2 (replaced by cr-lgbm-v3). cr-lgbm-v3 is in force. It is built on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md

## Q5
Only one note in another project builds directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
csb-lr-base rests on three dataset notes: ds-csb-biz-accounts (the root), ds-csb-churn-labels (built on ds-csb-biz-accounts), and ds-csb-oot-2025q1 (built on ds-csb-biz-accounts and ds-csb-churn-labels). It reaches ds-csb-biz-accounts through feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q7
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q8
csb-lr-base is the one current model in churn-small-business built directly on a replaced feature. It is built on feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. csb-lr-base is not superseded and stays on as the monitoring challenger.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q9
Three decision notes rest on ds-cb-spend-panel: dec-cb-extend-flat-pilot (via find-cb-flat-wins, exp-201 and ds-cb-pilot-2025q4), dec-cb-adopt-banded-tiers (via cb-elasticity-v2 and feat-cb-grocery-share), and dec-cb-threshold-2500 (via exp-206-breakeven-sim and cb-sim-v1).
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q10
The line runs dec-cb-extend-flat-pilot (replaced by dec-cb-adopt-banded-tiers) and then dec-cb-adopt-banded-tiers (replaced by dec-cb-threshold-2500). dec-cb-threshold-2500 is in force. It is built on find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/dec-cb-adopt-banded-tiers.md