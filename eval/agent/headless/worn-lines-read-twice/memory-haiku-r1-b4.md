## Q1
Four decision notes rest on ds-cr-ivr-paths: dec-cr-lgbm (through cr-logreg-v1 and cr-lgbm-v1), dec-cr-caller-v2, dec-cr-cost-matrix and dec-cr-pilot (through cr-lgbm-v3 and the later routing notes). These are all four decisions in call-center-routing.
Notes: call-center-routing/dec-cr-lgbm.md, call-center-routing/dec-cr-caller-v2.md, call-center-routing/dec-cr-cost-matrix.md, call-center-routing/dec-cr-pilot.md

## Q2
cli-xgb-v3 is in force: it replaced cli-xgb-v2, which had replaced cli-xgb-v1. It is built on exp-106, exp-107 and find-cli-uplift-wins.
Notes: credit-line-increase/cli-xgb-v3.md, credit-line-increase/exp-106.md, credit-line-increase/exp-107.md, credit-line-increase/find-cli-uplift-wins.md

## Q3
Only merchant-risk/feat-mrisk-dispute-ratio is built directly on ds-disp-merchant-link from another project. The other merchant-risk notes reach it only through that feature.
Notes: merchant-risk/feat-mrisk-dispute-ratio.md

## Q4
cr-lgbm-v1 rests on two dataset notes: ds-cr-calls directly, through feat-cr-caller-history-v1 and feat-cr-transcript-tfidf-v1, and ds-cr-ivr-paths, through feat-cr-ivr-path-v1.
Notes: call-center-routing/ds-cr-calls.md, call-center-routing/ds-cr-ivr-paths.md

## Q5
Both fraud25-gbm-v1 and fraud25-gbm-v2 build directly on feat-f25-amt-ratio, feat-f25-device-age, feat-f25-hour-band and feat-f25-velocity-v1.
Notes: fraud-2025/feat-f25-amt-ratio.md, fraud-2025/feat-f25-device-age.md, fraud-2025/feat-f25-hour-band.md, fraud-2025/feat-f25-velocity-v1.md

## Q6
None. The only current model is clv-ml-v2, and it builds on feat-clv-arpu-v2 and feat-clv-hazard, neither of which has been replaced. Its replaced inputs are the models clv-ml-v1 and exp-503, not a feature or dataset.
Notes: customer-lifetime-value/clv-ml-v2.md

## Q7
Three decisions rest on ds-cb-spend-panel: dec-cb-adopt-banded-tiers and dec-cb-extend-flat-pilot directly through the elasticity and finding notes, and dec-cb-threshold-2500 through dec-cb-adopt-banded-tiers.
Notes: cashback-redesign/dec-cb-adopt-banded-tiers.md, cashback-redesign/dec-cb-extend-flat-pilot.md, cashback-redesign/dec-cb-threshold-2500.md

## Q8
disp-lgbm-v3 is in force: it replaced disp-lgbm-v2, which had replaced disp-lgbm-v1. It is built on dec-disp-fraud-score-in, exp-307 and feat-disp-fraud-score, plus disp-lgbm-v2.
Notes: dispute-triage/disp-lgbm-v3.md, dispute-triage/dec-disp-fraud-score-in.md, dispute-triage/exp-307.md, dispute-triage/feat-disp-fraud-score.md

## Q9
Only model-monitoring/mm-limit-glm-v2 is built directly on feat-fsm-util-ratio from another project. Its other feature-store-migration links are in the same project.
Notes: model-monitoring/mm-limit-glm-v2.md

## Q10
cb-elasticity-v1 rests on ds-cb-pilot-2025q4 directly and on ds-cb-spend-panel through its inputs. ds-cb-spend-panel is built from cb_spend_panel.sql and cards.txn_daily, which have no linked note in this chain; a note titled cards.txn_daily does exist at data-quality-txn/ds-dq-txn-daily.md, but nothing links it here.
Notes: cashback-redesign/ds-cb-pilot-2025q4.md, cashback-redesign/ds-cb-spend-panel.md