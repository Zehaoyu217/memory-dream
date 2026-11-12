## Q1
One note from another project builds directly on find-cu-sms-cost: the finding find-ch-sms-call-gap in collections-channel-mix. Another collections-channel-mix note, dec-ch-call-escalation, depends on it only indirectly.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
Following its sources all the way back, bt-logit-baseline rests on two datasets. It uses ds-bt-bureau-join directly, and reaches ds-bt-offer-log through other notes.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
Only csb-lr-base. It is still current and builds directly on feat-csb-spend-raw, which feat-csb-spend-sa-v2 has since replaced. The other current model, csb-xgb-v2, builds only on notes that are still current.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026, all through other notes: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, and cu-uplift-v3 is the one in force now. It is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
One note from another project builds directly on feat-cli-util-v2: feat-cld-risk-band-v2 in limit-decrease-policy.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
Following its sources all the way back, bsm-app-gbm-v10b rests on five datasets: ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024, ds-bsm-v10-cohorts-2026, ds-bsm-v8-history, and ds-app-applications-2024 from application-scorecard.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md, application-scorecard/ds-app-applications-2024.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
Only cli-logreg-baseline. It is still current and builds directly on feat-cli-util-v1, which feat-cli-util-v2 has since replaced. The other current model, cli-xgb-v3, builds only on exp-107 and find-cli-uplift-wins, and neither has been replaced.
Notes: credit-line-increase/cli-logreg-baseline.md