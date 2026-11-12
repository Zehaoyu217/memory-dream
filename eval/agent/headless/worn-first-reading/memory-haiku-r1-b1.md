## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only, dec-aml-ranker-v3, dec-aml-sample-10 and dec-aml-suppress-018. They reach it through the aml-xgb-v1 to v3 chain, the structuring experiments and the findings.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md, aml-alerts/dec-aml-suppress-018.md

## Q2
The note in force is aml-xgb-v3, the current ranker that orders the queue. It is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note from another project is built directly on bt-xgb-v3: promo-apr-test/pa-bal-forecast-v1, which uses it as the BT propensity score.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions and ds-aml-cash-txn directly, and ds-aml-alerts through ds-aml-dispositions.
Notes: aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-alerts.md

## Q5
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
bt-logit-baseline is the only current model that builds directly on a replaced note: it uses feat-bt-util-3m, which was replaced by feat-bt-util-trend-v2. bt-xgb-v3 builds on no replaced feature or dataset note.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-dashboard, dec-ae-no-push-credit, dec-ae-score-v2 and dec-ae-tenure-norm. They reach it through the active-days and depth features, the engagement scores and the findings.
Notes: app-engagement/dec-ae-dashboard.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md

## Q8
The note in force is bt-xgb-v3. It is built on bt-xgb-v2, dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only application-scorecard/ds-app-bureau-v10-pull is built directly on feat-bsm-score-map-v2 from another project.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily, through the active-days and depth features, and ds-ae-push-log, through the push-open feature.
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md