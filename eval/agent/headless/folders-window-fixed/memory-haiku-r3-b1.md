## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. Each reaches it through the aml-xgb or exp-40x chain, not directly.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
aml-xgb-v1 was superseded by aml-xgb-v2, which was superseded by aml-xgb-v3, the note in force now. aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note of another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1, which uses it as its BT propensity score. The other BT notes that use bt-xgb-v3 are in balance-transfer-propensity itself.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions and ds-aml-alerts (through it), and ds-aml-cash-txn (through feat-aml-structuring-v1 and feat-aml-new-counterparty). ds-aml-alerts is the root, reached via ds-aml-dispositions.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/cr-lgbm-v1.md, call-center-routing/cr-logreg-v1.md, call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
Only bt-logit-baseline is still current and builds directly on a replaced feature. It uses feat-bt-util-3m, which was superseded by feat-bt-util-trend-v2. The current model bt-xgb-v3 builds on models, a decision and an experiment, not on any replaced feature or dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-no-push-credit, dec-ae-score-v2, dec-ae-tenure-norm and dec-ae-dashboard. All reach it through the score, feature and experiment chain.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v1 was superseded by bt-xgb-v2, which was superseded by bt-xgb-v3, the note in force now. bt-xgb-v3 is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note of another project is built directly on feat-bsm-score-map-v2: application-scorecard/ds-app-bureau-v10-pull, which re-scores applications on the mapped v10 score.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily (via feat-ae-active-days-v1 and feat-ae-depth-v1) and ds-ae-push-log (via feat-ae-push-open-v1).
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md