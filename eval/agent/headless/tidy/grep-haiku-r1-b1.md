## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. The first three reach it through aml-xgb-v1, aml-xgb-v3 and exp-408 respectively, and dec-aml-suppress-018 through exp-406 and aml-find-ranker-top40-revised.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
aml-xgb-v3 is in force; it superseded aml-xgb-v2, which had superseded aml-xgb-v1. It is built on aml-xgb-v2, exp-405, exp-407 and ds-aml-oot.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md, aml-alerts/ds-aml-oot.md

## Q3
Only promo-apr-test/pa-bal-forecast-v1 is built directly on bt-xgb-v3 from another project. The other direct child, dec-bt-cut-mailer-top30, is in the same project.
Notes: promo-apr-test/pa-bal-forecast-v1.md, balance-transfer-propensity/bt-xgb-v3.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-alerts, ds-aml-cash-txn and ds-aml-dispositions. It reaches ds-aml-alerts and ds-aml-cash-txn through ds-aml-dispositions and the structuring and counterparty features.
Notes: aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-dispositions.md

## Q5
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-transcript-tfidf-v1 and feat-cr-ivr-path-v1.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md, call-center-routing/feat-cr-ivr-path-v1.md

## Q6
bt-logit-baseline is the only current model that builds directly on a replaced feature, feat-bt-util-3m, which was superseded by feat-bt-util-trend-v2. The other current model, bt-xgb-v3, builds only on models and decision notes.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-dashboard, dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-tenure-norm. The first three go through ae-score-v1, ae-score-v2 or the depth and push features, and dec-ae-tenure-norm through feat-ae-depth-v2.
Notes: app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md

## Q8
bt-xgb-v3 is in force; it superseded bt-xgb-v2, which had superseded bt-xgb-v1. It is built on bt-xgb-v2, exp-107-margin-label and dec-bt-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/exp-107-margin-label.md, balance-transfer-propensity/dec-bt-margin-label.md

## Q9
Only application-scorecard/ds-app-bureau-v10-pull is built directly on feat-bsm-score-map-v2 from another project. The other direct children are all in bureau-score-migration.
Notes: application-scorecard/ds-app-bureau-v10-pull.md, bureau-score-migration/feat-bsm-score-map-v2.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily and ds-ae-push-log. It reaches them through feat-ae-active-days-v1, feat-ae-depth-v1 and feat-ae-push-open-v1.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md