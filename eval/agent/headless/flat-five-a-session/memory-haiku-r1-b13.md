## Q1
sfc-ets-v1 was replaced by sfc-lgbm-v2, which was replaced by sfc-hier-v3, the note in force now. sfc-hier-v3 is built on exp-207-spend-forecasting, feat-sfc-active-accounts, fnd-sfc-q4-reconciled and sfc-lgbm-v2.
Notes: work/sfc-ets-v1.md, work/sfc-lgbm-v2.md, work/sfc-hier-v3.md, work/exp-207-spend-forecasting.md, work/feat-sfc-active-accounts.md, work/fnd-sfc-q4-reconciled.md

## Q2
disp-lgbm-v1 rests on two dataset notes: ds-disp-analyst-labels (8,900 hand labels, 7,450 with two-analyst agreement), which feeds the training-label decision, and ds-disp-disputes (cards.disputes, 2025-01 to 2026-09), which feeds the reason-text feature.
Notes: work/ds-disp-analyst-labels.md, work/ds-disp-disputes.md

## Q3
Two decision notes rest on ds-fsm-parity-sample: dec-fsm-cutover, through fnd-parity-post-fix and fsm-churn-xgb-v2, and dec-fsm-timezone-utc, through exp-102-feature-store-migration and exp-101-feature-store-migration.
Notes: work/dec-fsm-cutover.md, work/dec-fsm-timezone-utc.md

## Q4
txc-logreg-v1 was replaced by txc-gbm-v2, which was replaced by txc-gbm-v3, the note in force now. txc-gbm-v3 is built on feat-txc-descriptor-tokens-v2, feat-txc-mcc-prior, feat-txc-normalise-v2 and txc-gbm-v2.
Notes: work/txc-logreg-v1.md, work/txc-gbm-v2.md, work/txc-gbm-v3.md, work/feat-txc-descriptor-tokens-v2.md, work/feat-txc-mcc-prior.md, work/feat-txc-normalise-v2.md

## Q5
ed-gbm-v2 rests on two dataset notes: ds-ed-current-base (accounts at 0 DPD from cards.accounts_monthly, the scoring population) and ds-ed-label-30p3m (30+ DPD label within 3 months, built on the current base). One link is unresolved: feat-ed-cashadv-v1 cites "the current-account scoring population" with no matching note, which most likely means ds-ed-current-base.
Notes: work/ds-ed-current-base.md, work/ds-ed-label-30p3m.md