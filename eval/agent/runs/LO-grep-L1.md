## Q1
All four aml-alerts decisions rest on ds-aml-alerts. dec-aml-queue-only gets there through aml-xgb-v1, q-aml-signoff and aml-find-fp-baseline, which lead back through ds-aml-dispositions and exp-401. dec-aml-suppress-018 builds on dec-aml-queue-only and exp-406. dec-aml-ranker-v3 builds on aml-xgb-v3 and dec-aml-suppress-018. dec-aml-sample-10 builds on exp-408 and dec-aml-suppress-018.
Notes: aml-alerts/dec-aml-queue-only.md, aml-alerts/dec-aml-suppress-018.md, aml-alerts/dec-aml-ranker-v3.md, aml-alerts/dec-aml-sample-10.md

## Q2
aml-xgb-v2 replaced aml-xgb-v1, and aml-xgb-v3 then replaced aml-xgb-v2. No note replaces aml-xgb-v3, so it is the one in force. It is built on aml-xgb-v2, exp-405, exp-407 and ds-aml-oot.
Notes: aml-alerts/aml-xgb-v3.md, aml-alerts/aml-xgb-v2.md, aml-alerts/exp-405.md, aml-alerts/exp-407.md, aml-alerts/ds-aml-oot.md

## Q3
One note in another project builds directly on bt-xgb-v3: the promo-apr-test balance forecast pa-bal-forecast-v1, which uses the BT propensity score.
Notes: promo-apr-test/pa-bal-forecast-v1.md

## Q4
aml-xgb-v2 rests on three dataset notes. ds-aml-cash-txn comes in through the structuring, new-counterparty, round-amount and cash-velocity features. ds-aml-dispositions comes in through aml-xgb-v1 and exp-401. ds-aml-alerts comes in through ds-aml-dispositions, feat-aml-kyc-band and the exp-404→403→402→401 chain. ds-aml-oot is not in its lineage.
Notes: aml-alerts/ds-aml-alerts.md, aml-alerts/ds-aml-cash-txn.md, aml-alerts/ds-aml-dispositions.md

## Q5
Both models build directly on feat-c25-txn-recency and feat-c25-payment-behaviour. They differ on utilization: v2 uses util-v2 and the baseline uses util-v1. The baseline also uses app-sessions.
Notes: churn-2025/feat-c25-txn-recency.md, churn-2025/feat-c25-payment-behaviour.md

## Q6
Only bt-logit-baseline. It is not superseded, though its note says it is now a reference model only, no longer scored in production. It builds directly on feat-bt-util-3m, which feat-bt-util-trend-v2 has replaced. The other current model, bt-xgb-v3, builds only on bt-xgb-v2, exp-107 and dec-bt-margin-label, so it has no replaced feature or dataset input.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/feat-bt-util-trend-v2.md

## Q7
Three decisions rest on feat-ae-push-open-v1. dec-ae-no-push-credit gets there through ae-score-v1 and through fnd-ae-push-null (via exp-503 and fnd-ae-push-assoc). dec-ae-score-v2 builds on ae-score-v2, which builds on dec-ae-no-push-credit. dec-ae-dashboard builds on dec-ae-score-v2 and fnd-ae-quintiles. dec-ae-tenure-norm does not rest on it.
Notes: app-engagement/dec-ae-no-push-credit.md, app-engagement/dec-ae-score-v2.md, app-engagement/dec-ae-dashboard.md

## Q8
bt-xgb-v2 replaced bt-xgb-v1, and bt-xgb-v3 then replaced bt-xgb-v2. No note replaces bt-xgb-v3, so it is the one in force. It is built on bt-xgb-v2, exp-107-margin-label and dec-bt-margin-label.
Notes: balance-transfer-propensity/bt-xgb-v3.md, balance-transfer-propensity/bt-xgb-v2.md, balance-transfer-propensity/exp-107-margin-label.md, balance-transfer-propensity/dec-bt-margin-label.md

## Q9
One note in another project builds directly on feat-bsm-score-map-v2: application-scorecard's ds-app-bureau-v10-pull.
Notes: application-scorecard/ds-app-bureau-v10-pull.md

## Q10
bsm-app-gbm-v10b rests on all four bureau-score-migration datasets. ds-bsm-app-dev-2024 and ds-bsm-v8-history come in through bsm-app-gbm-v10a→v8. ds-bsm-dual-pull-sample comes in through score-map-v1/v2 and exp-301. ds-bsm-v10-cohorts-2026 comes in through feat-bsm-thin-file-flag and feat-bsm-score-missing-impute.
Notes: bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md