## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. They reach it through the dispositions dataset, the KYC band feature, the aml-xgb-v3 line, and exp-406/exp-407/exp-408.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
aml-xgb-v3 is the note in force at the end of the aml-xgb-v1 → v2 → v3 line. It is built directly on aml-xgb-v2 (replaced), ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only promo-apr-test/pa-bal-forecast-v1 is built directly on bt-xgb-v3 from another project. The other promo-apr-test notes reach bt-xgb-v3 only through it or through other notes.
Notes: balance-transfer-propensity/bt-xgb-v3.md, promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on two dataset notes: ds-aml-dispositions directly, and ds-aml-alerts through it. It also rests on ds-aml-cash-txn through the two features feat-aml-new-counterparty and feat-aml-structuring-v1.
Notes: aml-alerts/aml-xgb-v1.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both models build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1. cr-lgbm-v1 also builds directly on caller-history, tenure and exp-101, which cr-logreg-v1 does not use.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature. It is built on feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2. bt-xgb-v3 is current too, but it builds on no feature or dataset note directly.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-dashboard, dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-tenure-norm. They reach it through ae-score-v1, ae-score-v2, the depth features and the finding notes.
Notes: app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md

## Q8
bt-xgb-v3 is the note in force at the end of the bt-xgb-v1 → v2 → v3 line. It is built directly on bt-xgb-v2 (replaced), dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only application-scorecard/ds-app-bureau-v10-pull is built directly on feat-bsm-score-map-v2 from another project. The other application-scorecard notes reach it only through that dataset.
Notes: bureau-score-migration/feat-bsm-score-map-v2.md, application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily directly through its features, and ds-ae-push-log through feat-ae-push-open-v1.
Notes: app-engagement/ae-score-v1.md, app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md