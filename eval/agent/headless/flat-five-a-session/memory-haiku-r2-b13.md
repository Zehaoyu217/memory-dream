## Q1
sfc-ets-v1 was superseded by sfc-lgbm-v2, which was superseded by sfc-hier-v3, so sfc-hier-v3 is in force. It is built on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md

## Q2
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels directly, and ds-disp-disputes through feat-disp-reason-text and ds-disp-analyst-labels.
Notes: work/disp-lgbm-v1.md, work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md, work/feat-disp-reason-text.md, work/dec-disp-labels-two-analyst.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover, which goes through fnd-parity-post-fix and exp-102/exp-107, and dec-fsm-timezone-utc, which goes through exp-102-feature-store-migration and exp-101-feature-store-migration.
Notes: work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-logreg-v1 was superseded by txc-gbm-v2, which was superseded by txc-gbm-v3, so txc-gbm-v3 is in force. It is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md

## Q5
ed-gbm-v2 rests on two dataset notes: ds-ed-current-base through feat-ed-cashadv-v1 and feat-ed-util-trend-v1, and ds-ed-label-30p3m through feat-ed-minpay-v2. feat-ed-cashadv-v1 also cites a "current-account scoring population" that no note records, which is probably ds-ed-current-base but is unconfirmed.
Notes: work/ed-gbm-v2.md, work/ed-gbm-v1.md, work/exp-205-early-delinquency.md, work/exp-206-early-delinquency.md, work/feat-ed-cashadv-v1.md, work/feat-ed-minpay-v2.md, work/feat-ed-util-trend-v1.md, work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md