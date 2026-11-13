## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-suppress-018, dec-aml-ranker-v3 and dec-aml-sample-10. Each one reaches it through the dispositions dataset and the aml-xgb models and experiments built on it.
Notes: work/dec-aml-queue-only.md, work/dec-aml-suppress-018.md, work/dec-aml-ranker-v3.md, work/dec-aml-sample-10.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by aml-xgb-v3, the current ranker. Its links are written only in its text: it builds on aml-xgb-v2, ds-aml-oot, exp-405-aml-alerts and "the experiment on recalibrated v3 top-40% capture", which is exp-407-aml-alerts.
Notes: work/aml-xgb-v3.md, work/aml-xgb-v2.md, work/ds-aml-oot.md, work/exp-405-aml-alerts.md, work/exp-407-aml-alerts.md

## Q3
aml-xgb-v1 rests on three dataset notes. It builds on ds-aml-dispositions directly, and on ds-aml-alerts and ds-aml-cash-txn through ds-aml-dispositions and its two features (new-counterparty and structuring-v1).
Notes: work/ds-aml-dispositions.md, work/ds-aml-alerts.md, work/ds-aml-cash-txn.md

## Q4
Both models build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: work/feat-cr-ivr-path-v1.md, work/feat-cr-transcript-tfidf-v1.md

## Q5
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-tenure-norm, dec-ae-score-v2 and dec-ae-dashboard.
Notes: work/dec-ae-no-push-credit.md, work/dec-ae-tenure-norm.md, work/dec-ae-score-v2.md, work/dec-ae-dashboard.md

## Q6
bt-xgb-v1 was replaced by bt-xgb-v2, which was replaced by bt-xgb-v3, the current production model. bt-xgb-v3 builds on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: work/bt-xgb-v3.md, work/bt-xgb-v2.md, work/dec-bt-margin-label.md, work/exp-107-margin-label.md

## Q7
ae-score-v1 rests on two dataset notes, ds-ae-sessions-daily and ds-ae-push-log. It reaches them through its features (active-days-v1, depth-v1 and push-open-v1); the "28-day active days count" in its text is feat-ae-active-days-v1.
Notes: work/ds-ae-sessions-daily.md, work/ds-ae-push-log.md

## Q8
Both models build directly on feat-c25-payment-behaviour and feat-c25-txn-recency.
Notes: work/feat-c25-payment-behaviour.md, work/feat-c25-txn-recency.md

## Q9
Four decision notes rest on feat-app-util-new: dec-app-cutoff-v3, dec-app-no-gbm, dec-app-rebuild-v4 and dec-app-cutoff-v4. dec-app-cutoff-v3 has since been replaced by dec-app-cutoff-v4.
Notes: work/dec-app-cutoff-v3.md, work/dec-app-no-gbm.md, work/dec-app-rebuild-v4.md, work/dec-app-cutoff-v4.md

## Q10
cr-lgbm-v1 was replaced by cr-lgbm-v2, which was replaced by cr-lgbm-v3, the current router. cr-lgbm-v3 builds on cr-lgbm-v2, ds-cr-intent-labels, exp-106-call-center-routing and fnd-cr-threshold.
Notes: work/cr-lgbm-v3.md, work/cr-lgbm-v2.md, work/ds-cr-intent-labels.md, work/exp-106-call-center-routing.md, work/fnd-cr-threshold.md