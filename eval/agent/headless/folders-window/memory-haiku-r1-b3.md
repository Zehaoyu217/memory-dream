## Q1
Only one note from another project is built directly on find-cu-sms-cost: the collections-channel-mix finding on the 8-29 DPD SMS-to-call gap, which replaces find-ch-sms-matches-call.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests directly on ds-bt-bureau-join and feat-bt-util-3m. Through those it reaches ds-bt-offer-log, so the dataset notes are ds-bt-bureau-join and ds-bt-offer-log. One note, dec-bt-margin-label, has an unmatched link that may point to bt-logit-baseline, but no dataset is involved.
Notes: balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both models build directly on the same three feature notes: feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1.
Notes: credit-line-increase/feat-cli-pay-behaviour.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-util-v1.md

## Q4
csb-lr-base is still current and builds directly on feat-csb-spend-raw, which was replaced by feat-csb-spend-sa-v2. The other current model, csb-xgb-v2, uses no replaced feature or dataset.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map, dec-bsm-cutover-2026q3 and dec-bsm-keep-v8-fallback. Each reaches it through exp-303, feat-bsm-v10-band, exp-307 or bsm-app-gbm-v10b.
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md

## Q6
The line runs cu-uplift-v1 → cu-uplift-v2 → cu-uplift-v3, and cu-uplift-v3 is in force now. It is built on cu-uplift-v2, exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only one note from another project is built directly on feat-cli-util-v2: the limit-decrease-policy risk-band feature feat-cld-risk-band-v2.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-dual-pull-sample and ds-bsm-v10-cohorts-2026 directly or through its parents, and ds-bsm-v8-history and ds-bsm-app-dev-2024 further back.
Notes: bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-app-dev-2024.md

## Q9
The two models share feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. feat-fsm-util-ratio feeds only fsm-churn-xgb-v2.
Notes: feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is still current and builds directly on feat-cli-util-v1, which was replaced by feat-cli-util-v2. The current cli-xgb-v3 builds on no replaced feature or dataset.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md