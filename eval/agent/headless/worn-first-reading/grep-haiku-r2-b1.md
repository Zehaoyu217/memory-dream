## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-suppress-018, dec-aml-sample-10 and dec-aml-ranker-v3. Each reaches it through the ranker and experiment chain (exp-401, aml-find-fp-baseline, aml-xgb-v1/v2/v3, ds-aml-oot, ds-aml-dispositions).
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-ranker-v3.md

## Q2
aml-xgb-v1 was replaced by aml-xgb-v2, which was replaced by aml-xgb-v3, so aml-xgb-v3 is in force. It is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note in another project builds directly on bt-xgb-v3: pa-bal-forecast-v1 in promo-apr-test.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on the datasets ds-aml-dispositions, ds-aml-cash-txn and ds-aml-alerts. It reaches ds-aml-dispositions directly, and ds-aml-alerts through it. It reaches ds-aml-cash-txn through feat-aml-new-counterparty and feat-aml-structuring-v1.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/feat-aml-new-counterparty.md, aml-alerts/feat-aml-structuring-v1.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature, feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2. Its notes say it is no longer scored in production, but no note formally supersedes it.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-score-v2, dec-ae-no-push-credit, dec-ae-dashboard and dec-ae-tenure-norm. They reach it through ae-score-v1/v2 with feat-ae-active-days-v1, and through feat-ae-depth-v1 and feat-ae-depth-v2.
Notes: app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/ds-ae-sessions-daily.md

## Q8
bt-xgb-v1 was replaced by bt-xgb-v2, which was replaced by bt-xgb-v3, so bt-xgb-v3 is in force. It is built on bt-xgb-v2 (the depth-5 xgboost model), dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note in another project builds directly on feat-bsm-score-map-v2: ds-app-bureau-v10-pull in application-scorecard.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log. It reaches them through feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1.
Notes: app-engagement/ae-score-v1.md, app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md