## Q1
Only one note of another project is built directly on find-cu-sms-cost: `collections-channel-mix/find-ch-sms-call-gap`, which also replaces `find-ch-sms-matches-call`.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log through ds-bt-bureau-join and feat-bt-util-3m. The chain also includes the feature feat-bt-util-3m and the question q-bt-who-accepts.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base, which has no superseding note, builds directly on feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2. The other current model, csb-xgb-v2, builds only on notes that have not been replaced.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-cutover-2026q3 (via exp-305 and exp-306), and dec-bsm-keep-v8-fallback (via exp-307 and exp-304).
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line is cu-uplift-v1, then cu-uplift-v2, then cu-uplift-v3, which is the note in force now. cu-uplift-v3 is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note of another project is built directly on feat-cli-util-v2: `limit-decrease-policy/feat-cld-risk-band-v2`.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on five dataset notes: ds-app-applications-2024 (application-scorecard), ds-bsm-dual-pull-sample, ds-bsm-app-dev-2024, ds-bsm-v10-cohorts-2026 and ds-bsm-v8-history. Only feat-app-thin-file and feat-bsm-score-map-v2 are direct inputs; the datasets are reached through the chain.
Notes: application-scorecard/ds-app-applications-2024.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md

## Q9
Both fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline, which has no superseding note, builds directly on feat-cli-util-v1, which was replaced by feat-cli-util-v2. The other current model, cli-xgb-v3, builds only on notes that have not been replaced.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md