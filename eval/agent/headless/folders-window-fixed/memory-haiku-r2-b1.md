## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. They reach it through aml-xgb-v1/v2/v3, exp-40x and the findings built on those.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
The line ends at aml-xgb-v3, which is the current ranker. It is built directly on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
One note from another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1, which uses its BT propensity score. No other folder's note has bt-xgb-v3 among its direct inputs.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions directly, and ds-aml-alerts and ds-aml-cash-txn through feat-aml-structuring-v1, feat-aml-new-counterparty and ds-aml-dispositions.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1. cr-lgbm-v1 also uses caller history, tenure and exp-101, which cr-logreg-v1 does not.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
Only bt-logit-baseline fits. It is a current model built directly on feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2. bt-xgb-v3 is current, but its direct inputs are models and decisions, not a replaced feature or dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard. They reach it through the depth, push and active-days features, the score models, and the experiments and findings built on them.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-dashboard.md

## Q8
The line ends at bt-xgb-v3, which is current in production. It is built directly on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
One note from another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull, which re-scores applications on the mapped v10 score.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log. It reaches them through the active-days, depth and push-open features.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md