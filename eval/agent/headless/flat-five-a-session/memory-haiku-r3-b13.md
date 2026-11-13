## Q1
The note in force is `sfc-hier-v3`, reached through `sfc-ets-v1` → `sfc-lgbm-v2` → `sfc-hier-v3`. It is built on `sfc-lgbm-v2`, `feat-sfc-active-accounts`, `fnd-sfc-q4-reconciled` and `exp-207-spend-forecasting`, and through `feat-sfc-active-accounts` it rests on the `ds-sfc-segment-monthly` dataset.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md, work/exp-207-spend-forecasting.md, work/ds-sfc-segment-monthly.md

## Q2
`disp-lgbm-v1` rests directly on the dataset `ds-disp-analyst-labels`, and through it and `feat-disp-reason-text` on the dataset `ds-disp-disputes`. The chain also runs through `dec-disp-labels-two-analyst` and the question `q-disp-label-source`.
Notes: work/disp-lgbm-v1.md, work/dec-disp-labels-two-analyst.md, work/ds-disp-analyst-labels.md, work/feat-disp-reason-text.md, work/ds-disp-disputes.md, work/q-disp-label-source.md

## Q3
Two decision notes rest on `ds-fsm-parity-sample`: `dec-fsm-timezone-utc` (via `exp-102-feature-store-migration` ← `exp-101-feature-store-migration`) and `dec-fsm-cutover` (via `fnd-parity-post-fix` and `fsm-churn-xgb-v2`). I checked the other FSM decisions (`dec-fsm-naming-rule`) and the bureau decisions, and none of them trace back to the parity sample.
Notes: work/dec-fsm-timezone-utc.md, work/dec-fsm-cutover.md, work/ds-fsm-parity-sample.md, work/exp-101-feature-store-migration.md, work/exp-102-feature-store-migration.md, work/fnd-parity-post-fix.md, work/fsm-churn-xgb-v2.md

## Q4
The note in force is `txc-gbm-v3`, reached through `txc-logreg-v1` → `txc-gbm-v2` → `txc-gbm-v3`. It is built on `txc-gbm-v2`, `feat-txc-descriptor-tokens-v2`, `feat-txc-mcc-prior` and `feat-txc-normalise-v2`, and through those it rests on the datasets `ds-txc-descriptor-sample`, `ds-txc-mcc-crosswalk`, `ds-txc-labelled-merchants` and `ds-txc-gold-holdout`.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md, work/ds-txc-descriptor-sample.md, work/ds-txc-mcc-crosswalk.md, work/ds-txc-labelled-merchants.md, work/ds-txc-gold-holdout.md

## Q5
`ed-gbm-v2` rests on the datasets `ds-ed-current-base` (via the cash-advance and utilisation-trend features) and `ds-ed-label-30p3m` (via `feat-ed-minpay-v2`). The chain also runs through `ed-gbm-v1`, `exp-205-early-delinquency`, `exp-206-early-delinquency` and three features.
Notes: work/ed-gbm-v2.md, work/ed-gbm-v1.md, work/exp-205-early-delinquency.md, work/exp-206-early-delinquency.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md, work/feat-ed-util-trend-v1.md, work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md