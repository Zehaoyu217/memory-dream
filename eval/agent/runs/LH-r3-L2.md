## Q1
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q2
churn-lr-base-2025 is the only current model that builds directly on a replaced feature: it rests on feat-c25-util-v1, which has since been replaced by feat-c25-util-v2. The current churn-gbm-2025-v2 rests on no replaced feature or dataset.
Notes: churn-2025/churn-lr-base-2025.md

## Q3
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map and dec-bsm-keep-v8-fallback (through their inputs), and dec-bsm-cutover-2026q3 (through find-bsm-ks-parity and bsm-cutoff-logit). None rests on it directly.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q4
cr-lgbm-v1 was replaced by cr-lgbm-v2, which was replaced by cr-lgbm-v3, the note in force now. cr-lgbm-v3 is built directly on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md

## Q5
Only one note of another project builds directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
csb-lr-base rests directly on the dataset notes ds-csb-churn-labels and ds-csb-oot-2025q1. Following those and the feature notes back, it also rests on ds-csb-biz-accounts, the root dataset.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q7
cli-logreg-baseline and cli-xgb-v1 both build directly on feat-cli-util-v1 (since replaced by feat-cli-util-v2), feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q8
csb-lr-base is the only current model that builds directly on a replaced feature: it rests on feat-csb-spend-raw, which has been replaced by feat-csb-spend-sa-v2. The current csb-xgb-v2 rests on no replaced feature or dataset.
Notes: churn-small-business/csb-lr-base.md

## Q9
Three decision notes rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers, dec-cb-extend-flat-pilot and dec-cb-threshold-2500, all through intermediate notes. None rests on it directly.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q10
dec-cb-extend-flat-pilot was replaced by dec-cb-adopt-banded-tiers, which was replaced by dec-cb-threshold-2500, the decision in force now. dec-cb-threshold-2500 is built directly on find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/dec-cb-adopt-banded-tiers.md