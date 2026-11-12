## Q1
Both csb-lr-base and csb-xgb-v1 build directly on feat-csb-spend-raw (raw trailing three-month spend) and feat-csb-tenure-band (five tenure bands). Only csb-xgb-v1 also uses feat-csb-deposit-volatility.
Notes: churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-tenure-band.md

## Q2
churn-lr-base-2025 has not been replaced, and it builds directly on feat-c25-util-v1, which feat-c25-util-v2 replaced. The other current model, churn-gbm-2025-v2, already uses util-v2.
Notes: churn-2025/churn-lr-base-2025.md

## Q3
Three decisions rest on ds-bsm-v10-cohorts-2026. dec-bsm-isotonic-map comes through exp-303 and find-bsm-psi-after-map. dec-bsm-cutover-2026q3 comes through exp-306 and find-bsm-ks-parity, and also through feat-bsm-v10-band, exp-305 and bsm-cutoff-logit. dec-bsm-keep-v8-fallback comes through feat-bsm-thin-file-flag, find-bsm-thin-file-gap, bsm-app-gbm-v10b and exp-307. dec-bsm-linear-map does not rest on it.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q4
cr-lgbm-v2 replaced cr-lgbm-v1, and cr-lgbm-v3 replaced cr-lgbm-v2. cr-lgbm-v3 is the current router. It is built on cr-lgbm-v2, fnd-cr-threshold, ds-cr-intent-labels and exp-106.
Notes: call-center-routing/cr-lgbm-v3.md, call-center-routing/cr-lgbm-v2.md, call-center-routing/fnd-cr-threshold.md, call-center-routing/ds-cr-intent-labels.md, call-center-routing/exp-106.md

## Q5
One note in another project builds directly on churn-gbm-2025-v2: feat-ror-churn-score in retention-offers-roi. ror-uplift-v1 uses that score too, but only through feat-ror-churn-score.
Notes: retention-offers-roi/feat-ror-churn-score.md

## Q6
csb-lr-base rests on three dataset notes. It uses ds-csb-oot-2025q1 and ds-csb-churn-labels directly. It reaches ds-csb-biz-accounts through its features and through those two datasets. It does not reach ds-csb-merchant-mix.
Notes: churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-biz-accounts.md

## Q7
Both build directly on the same three features: feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour. cli-xgb-v1 also uses the dataset ds-cli-holdout-2025q4.
Notes: credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q8
csb-lr-base has not been replaced, and it builds directly on feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. The other current model, csb-xgb-v2, uses only notes that are still current.
Notes: churn-small-business/csb-lr-base.md

## Q9
All three cashback-redesign decisions rest on ds-cb-spend-panel. dec-cb-extend-flat-pilot comes through ds-cb-pilot-2025q4, exp-201 and find-cb-flat-wins. dec-cb-adopt-banded-tiers comes through feat-cb-spend-base, exp-204 and cb-elasticity-v2. dec-cb-threshold-2500 comes through ds-cb-rewards-ledger, cb-sim-v1 and exp-206. Only dec-cb-threshold-2500 is still in force.
Notes: cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q10
dec-cb-adopt-banded-tiers replaced dec-cb-extend-flat-pilot, and dec-cb-threshold-2500 replaced dec-cb-adopt-banded-tiers. dec-cb-threshold-2500 is in force now: the top tier starts at $2,500 for the Q3 2026 launch. It is built on find-cb-breakeven-lift, exp-206-breakeven-sim and dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-threshold-2500.md, cashback-redesign/find-cb-breakeven-lift.md, cashback-redesign/exp-206-breakeven-sim.md, cashback-redesign/dec-cb-adopt-banded-tiers.md