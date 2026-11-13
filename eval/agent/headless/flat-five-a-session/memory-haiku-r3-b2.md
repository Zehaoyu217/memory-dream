## Q1
bt-xgb-v1 was replaced by bt-xgb-v2, which was replaced by bt-xgb-v3, so bt-xgb-v3 is the note in force. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q2
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log. It gets there through feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1.
Notes: work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q3
churn-gbm-2025-v2 and churn-lr-base-2025 both build directly on feat-c25-payment-behaviour and feat-c25-txn-recency. They differ on the utilisation feature (feat-c25-util-v2 for the GBM, feat-c25-util-v1 for the logistic baseline).
Notes: work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q4
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-rebuild-v4, dec-app-cutoff-v4 and dec-app-no-gbm. They reach it through app-scorecard-v3 and the models and experiments built on it.
Notes: work/dec-app-cutoff-v3.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md, work/dec-app-no-gbm.md

## Q5
cr-lgbm-v1 was replaced by cr-lgbm-v2, which was replaced by cr-lgbm-v3, so cr-lgbm-v3 is the note in force. It is built on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold.
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md