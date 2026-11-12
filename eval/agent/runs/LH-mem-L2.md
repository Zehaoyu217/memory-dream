## Q1
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw and feat-csb-tenure-band (csb-xgb-v1 also uses deposit volatility, which csb-lr-base does not).
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md
## Q2
churn-lr-base-2025 is still current and was built directly on feat-c25-util-v1, which was replaced by feat-c25-util-v2. churn-gbm-2025-v2, the other current model, is built on util-v2 and is not affected.
Notes: churn-2025/churn-lr-base-2025.md
## Q3
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (directly via exp-303), dec-bsm-cutover-2026q3 (via exp-305 and bsm-cutoff-logit, which trace back to exp-303 and find-bsm-ks-parity, which trace to exp-306), and dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap, which trace back to feat-bsm-thin-file-flag). dec-bsm-linear-map does not rest on it.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md
## Q4
The line ends at cr-lgbm-v3 (it supersedes cr-lgbm-v2, which superseded cr-lgbm-v1), and cr-lgbm-v3 is in force. It is built on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md
## Q5
Only one note of another project is built directly on churn-gbm-2025-v2: retention-offers-roi/feat-ror-churn-score.md, which takes its 60-day churn score from that model.
Notes: retention-offers-roi/feat-ror-churn-score.md
## Q6
csb-lr-base rests on two dataset notes: ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts through feat-csb-spend-raw, feat-csb-tenure-band, ds-csb-oot-2025q1 and ds-csb-churn-labels. ds-csb-churn-labels is a finding-kind note built on ds-csb-biz-accounts.
Notes: churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md
## Q7
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour.
Notes: credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md
## Q8
csb-lr-base is the only current model in churn-small-business that builds directly on a replaced note: it uses feat-csb-spend-raw, which was superseded by feat-csb-spend-sa-v2. csb-xgb-v2 uses only current features, and csb-xgb-v1 is superseded.
Notes: churn-small-business/csb-lr-base.md
## Q9
Eight decision-kind notes trace back to ds-cb-spend-panel, but only three are decisions in the sense of the question. dec-cb-extend-flat-pilot rests on it via find-cb-flat-wins, exp-201 and ds-cb-pilot-2025q4. dec-cb-adopt-banded-tiers rests on it via cb-elasticity-v2 and feat-cb-spend-base. dec-cb-threshold-2500 rests on it via find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md
## Q10
dec-cb-extend-flat-pilot was superseded by dec-cb-adopt-banded-tiers, which was superseded by dec-cb-threshold-2500. dec-cb-threshold-2500 is the one in force and is built on find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/dec-cb-adopt-banded-tiers.md