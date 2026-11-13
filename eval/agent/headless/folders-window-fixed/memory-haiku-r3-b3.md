## Q1
The only note of another project built directly on find-cu-sms-cost is the channel-mix finding that compares SMS and call gaps on 8-29 DPD accounts. The other notes that cite it are in collections-uplift itself.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through feat-bt-util-3m and ds-bt-bureau-join.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current and builds directly on feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced. No other current model in churn-small-business builds directly on a replaced feature or dataset.
Notes: churn-small-business/csb-lr-base.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: the isotonic-map decision directly through exp-303 and feat-bsm-score-map-v2, the cutover decision through bsm-cutoff-logit, and the v8 fallback decision through exp-307 and find-bsm-thin-file-gap. The application-scorecard decision dec-app-cutoff-v4 rests on bureau-score-migration only through feat-bsm-score-map-v2, not this dataset.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The note in force at the end of that line is cu-uplift-v3, which replaced cu-uplift-v2. It is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
The only note of another project built directly on feat-cli-util-v2 is the limit-decrease risk-band feature, feat-cld-risk-band-v2.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v10-cohorts-2026 and ds-bsm-dual-pull-sample directly through its feature inputs, and ds-bsm-v8-history and ds-bsm-app-dev-2024 further back through the model chain.
Notes: bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both models build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is still current and builds directly on feat-cli-util-v1, which feat-cli-util-v2 replaced. cli-xgb-v1 also used feat-cli-util-v1, but it has been superseded, so it does not count.
Notes: credit-line-increase/cli-logreg-baseline.md