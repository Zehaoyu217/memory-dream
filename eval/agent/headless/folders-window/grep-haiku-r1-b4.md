## Q1
Four decisions rest on ds-cr-ivr-paths: dec-cr-lgbm (via cr-lgbm-v1 and feat-cr-ivr-path-v1), dec-cr-caller-v2 (via exp-104 and fnd-cr-leak-corrected), dec-cr-cost-matrix (via cr-lgbm-v3) and dec-cr-pilot (via cr-lgbm-v3).
Notes: call-center-routing/ds-cr-ivr-paths.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/cr-lgbm-v1.md, call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is the model in force at the end of the replacement line (cli-xgb-v1, then cli-xgb-v2, then cli-xgb-v3). It builds on the out-of-time AUC check for v2 (exp-106), exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v1.md, credit-line-increase/cli-xgb-v2.md, credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only one note in another project builds directly on ds-disp-merchant-link: merchant-risk/feat-mrisk-dispute-ratio, which borrows the dispute ratio for mrisk-gbm-v3. merchant-risk/dec-mrisk-dispute-feature names the dependency but builds on the lift test and feat-mrisk-dispute-ratio, not on the dataset.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/dec-mrisk-dispute-feature.md, dispute-triage/ds-disp-merchant-link.md

## Q4
cr-lgbm-v1 rests on two dataset notes, ds-cr-calls and ds-cr-ivr-paths. ds-cr-calls feeds through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1, and ds-cr-ivr-paths feeds through feat-cr-ivr-path-v1. feat-cr-tenure-v1 has no dataset note; its source is `cards.accounts_monthly`.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md, call-center-routing/feat-cr-caller-history-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-tenure-v1.md

## Q5
fraud25-gbm-v1 and fraud25-gbm-v2 both build directly on four feature notes: feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1. v2 adds feat-f25-mcc-travel on top of these.
Notes: fraud-2025/fraud25-gbm-v1.md, fraud-2025/fraud25-gbm-v2.md, fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
clv-bgnbd-v1 is the current model that builds on a replaced feature. It builds on the six-month average revenue feature, feat-clv-arpu-v1, which was replaced by feat-clv-arpu-v2 in November 2025. clv-bgnbd-v1 is kept as a marketing sanity check and is not formally superseded. The finance model clv-ml-v2 uses arpu v2 and is not affected.
Notes: customer-lifetime-value/clv-bgnbd-v1.md, customer-lifetime-value/feat-clv-arpu-v1.md, customer-lifetime-value/feat-clv-arpu-v2.md, customer-lifetime-value/clv-ml-v2.md

## Q7
Three decisions rest on ds-cb-spend-panel. dec-cb-extend-flat-pilot does so through find-cb-flat-wins, cb-elasticity-v1 and ds-cb-pilot-2025q4. dec-cb-adopt-banded-tiers does so through cb-elasticity-v2, feat-cb-spend-band-v2 and feat-cb-spend-base. dec-cb-threshold-2500 does so through dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/ds-cb-spend-panel.md, cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/find-cb-flat-wins.md, cashback-redesign/cb-elasticity-v1.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/cb-elasticity-v2.md, cashback-redesign/feat-cb-spend-band-v2.md, cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is the model in force at the end of the replacement line (disp-lgbm-v1, then disp-lgbm-v2, then disp-lgbm-v3). It builds on dec-disp-fraud-score-in, disp-lgbm-v2, the fraud score lift experiment exp-307 and feat-disp-fraud-score.
Notes: dispute-triage/disp-lgbm-v1.md, dispute-triage/disp-lgbm-v2.md, dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only one note in another project builds directly on feat-fsm-util-ratio: model-monitoring/mm-limit-glm-v2. It is still current, since mm-limit-glm-v1 is the only note marked superseded by it.
Notes: model-monitoring/mm-limit-glm-v2.md, feature-store-migration/feat-fsm-util-ratio.md

## Q10
cb-elasticity-v1 rests on two dataset notes, ds-cb-pilot-2025q4 and ds-cb-spend-panel. It uses ds-cb-pilot-2025q4 directly, and ds-cb-spend-panel through ds-cb-pilot-2025q4 and through feat-cb-spend-base.
Notes: cashback-redesign/cb-elasticity-v1.md, cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/feat-cb-spend-base.md, cashback-redesign/ds-cb-spend-panel.md