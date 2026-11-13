## Q1
sfc-hier-v3 is the note in force (sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3). It is built on exp-207-spend-forecasting (the MinT reconciliation run), feat-sfc-active-accounts, fnd-sfc-q4-reconciled, and sfc-lgbm-v2 as the per-segment LightGBM model.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md

## Q2
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels (the 8,900 hand labels, 7,450 with two-analyst agreement) directly through the two-analyst label decision, and ds-disp-disputes (cards.disputes) through the TF-IDF reason-text feature.
Notes: work/disp-lgbm-v1.md, work/dec-disp-labels-two-analyst.md, work/q-disp-label-source.md, work/feat-disp-reason-text.md, work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-timezone-utc (via exp-102 and exp-101) and dec-fsm-cutover (via fnd-parity-post-fix, and via fsm-churn-xgb-v2 and feat-fsm-util-ratio).
Notes: work/ds-fsm-parity-sample.md, work/exp-101-feature-store-migration.md, work/exp-102-feature-store-migration.md, work/exp-107-feature-store-migration.md, work/fnd-parity-pre-fix.md, work/fnd-parity-post-fix.md, work/feat-fsm-payment-lag-v2.md, work/feat-fsm-util-ratio.md, work/exp-105-feature-store-migration.md, work/fnd-churn-lift.md, work/fsm-churn-xgb-v2.md, work/dec-fsm-timezone-utc.md, work/dec-fsm-cutover.md

## Q4
txc-gbm-v3 is the note in force (txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3). It is built on feat-txc-descriptor-tokens-v2, feat-txc-normalise-v2, feat-txc-mcc-prior, and txc-gbm-v2.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-normalise-v2.md, work/feat-txc-mcc-prior.md

## Q5
ed-gbm-v2 rests on two dataset notes: ds-ed-current-base (the 0-DPD current-account population, reached via feat-ed-util-trend-v1 and ed-gbm-v1) and ds-ed-label-30p3m (the 30+ DPD label, reached via feat-ed-minpay-v2).
Notes: work/ed-gbm-v2.md, work/ed-gbm-v1.md, work/exp-206-early-delinquency.md, work/find-ed-minpay.md, work/exp-205-early-delinquency.md, work/feat-ed-util-trend-v1.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md, work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md