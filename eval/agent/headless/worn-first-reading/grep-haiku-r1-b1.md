## Q1
Four decision notes rest on ds-aml-alerts: dec-aml-queue-only (via aml-find-fp-baseline and q-aml-signoff), dec-aml-ranker-v3 (via aml-xgb-v3), dec-aml-suppress-018 (via aml-find-ranker-top40-revised), and dec-aml-sample-10 (via dec-aml-suppress-018). Each reaches ds-aml-alerts through ds-aml-oot, exp-401 or ds-aml-dispositions.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-sample-10.md

## Q2
aml-xgb-v3 is the one in force; it replaced aml-xgb-v2, which had replaced aml-xgb-v1. aml-xgb-v3 is built on aml-xgb-v2, ds-aml-oot, exp-405 and exp-407.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/ds-aml-oot.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md

## Q3
Only one note from another project builds directly on bt-xgb-v3: pa-bal-forecast-v1 in promo-apr-test, which uses it for the BT propensity score.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v1 rests on three dataset notes: ds-aml-dispositions (which rests on ds-aml-alerts), and ds-aml-cash-txn (reached through feat-aml-new-counterparty and feat-aml-structuring-v1). The full set is ds-aml-alerts, ds-aml-dispositions and ds-aml-cash-txn.
Notes: aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-dispositions.md, aml-alerts/ds-aml-cash-txn.md

## Q5
Both cr-lgbm-v1 and cr-logreg-v1 build directly on feat-cr-ivr-path-v1 and feat-cr-transcript-tfidf-v1.
Notes: call-center-routing/feat-cr-ivr-path-v1.md, call-center-routing/feat-cr-transcript-tfidf-v1.md

## Q6
bt-logit-baseline is the only current-looking model that builds directly on a replaced feature, feat-bt-util-3m (replaced by feat-bt-util-trend-v2). Caveat: the note is marked "no longer scored in production", so it is a reference model rather than a live one.
Notes: balance-transfer-propensity/bt-logit-baseline.md

## Q7
Four decision notes rest on ds-ae-sessions-daily: dec-ae-score-v2 and dec-ae-tenure-norm, plus dec-ae-no-push-credit (via ae-score-v1 and fnd-ae-push-null) and dec-ae-dashboard (via dec-ae-score-v2).
Notes: app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-tenure-norm.md, app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v3 is the one in force; it replaced bt-xgb-v2, which had replaced bt-xgb-v1. bt-xgb-v3 is built on bt-xgb-v2 (the depth-5 xgboost model), dec-bt-margin-label and exp-107-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/dec-bt-margin-label.md, balance-transfer-propensity/exp-107-margin-label.md

## Q9
Only one note from another project builds directly on feat-bsm-score-map-v2: ds-app-bureau-v10-pull in application-scorecard.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
ae-score-v1 rests on two dataset notes: ds-ae-sessions-daily (directly, via feat-ae-active-days-v1 and feat-ae-depth-v1, and via ds-ae-push-log) and ds-ae-push-log (via feat-ae-push-open-v1).
Notes: app-engagement/ds-ae-sessions-daily.md, app-engagement/ds-ae-push-log.md