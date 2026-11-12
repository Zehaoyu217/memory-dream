## Q1
find-ch-sms-call-gap in collections-channel-mix is the only note from another project built directly on find-cu-sms-cost. It lists "collections-uplift/find-cu-sms-cost" in its build line.
Notes: collections-channel-mix/find-ch-sms-call-gap.md

## Q2
bt-logit-baseline rests on two dataset notes: ds-bt-bureau-join directly, and ds-bt-offer-log both directly (via feat-bt-util-3m) and through ds-bt-bureau-join. The chain ends at ds-bt-offer-log, which builds on the question q-bt-who-accepts, not on another dataset.
Notes: balance-transfer-propensity/bt-logit-baseline.md, balance-transfer-propensity/ds-bt-bureau-join.md, balance-transfer-propensity/feat-bt-util-3m.md, balance-transfer-propensity/ds-bt-offer-log.md

## Q3
Both cli-logreg-baseline and cli-xgb-v1 build directly on feat-cli-util-v1, feat-cli-spend-velocity and feat-cli-pay-behaviour (the full-pay versus minimum-pay feature).
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/cli-xgb-v1.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-spend-velocity.md, credit-line-increase/feat-cli-pay-behaviour.md

## Q4
csb-lr-base is still current (it stays on as the monitoring challenger) and builds directly on feat-csb-spend-raw, which feat-csb-spend-sa-v2 replaced from January 2026. csb-xgb-v2, the current scoring model, does not build directly on any replaced feature or dataset note.
Notes: churn-small-business/csb-lr-base.md, churn-small-business/feat-csb-spend-raw.md, churn-small-business/feat-csb-spend-sa-v2.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q5
Three decision notes rest on ds-bsm-v10-cohorts-2026: dec-bsm-isotonic-map (via exp-303), dec-bsm-keep-v8-fallback (via exp-307 and find-bsm-thin-file-gap, which goes through feat-bsm-thin-file-flag), and dec-bsm-cutover-2026q3 (via find-bsm-ks-parity and exp-306, and via bsm-cutoff-logit and exp-305).
Notes: bureau-score-migration/dec-bsm-isotonic-map.md, bureau-score-migration/dec-bsm-keep-v8-fallback.md, bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/exp-303.md, bureau-score-migration/exp-306.md, bureau-score-migration/exp-307.md, bureau-score-migration/feat-bsm-thin-file-flag.md, bureau-score-migration/find-bsm-thin-file-gap.md, bureau-score-migration/find-bsm-ks-parity.md, bureau-score-migration/bsm-cutoff-logit.md, bureau-score-migration/exp-305.md

## Q6
cu-uplift-v1 was replaced by cu-uplift-v2, which was replaced by cu-uplift-v3. cu-uplift-v3 is the one in force, promoted to call routing on 2026-03-25 and not superseded. It builds on the calibrated uplift model (cu-uplift-v2), exp-106 and feat-cu-bureau-delta.
Notes: collections-uplift/cu-uplift-v3.md, collections-uplift/cu-uplift-v2.md, collections-uplift/exp-106.md, collections-uplift/feat-cu-bureau-delta.md

## Q7
Only feat-cld-risk-band-v2 in limit-decrease-policy builds directly on credit-line-increase/feat-cli-util-v2.
Notes: limit-decrease-policy/feat-cld-risk-band-v2.md

## Q8
bsm-app-gbm-v10b rests on four dataset notes: ds-bsm-v8-history at the root, ds-bsm-dual-pull-sample, ds-bsm-v10-cohorts-2026 and ds-bsm-app-dev-2024. The v10b model reaches them through bsm-app-gbm-v10a, feat-bsm-score-map-v2, feat-bsm-thin-file-flag and bsm-app-gbm-v8.
Notes: bureau-score-migration/bsm-app-gbm-v10b.md, bureau-score-migration/bsm-app-gbm-v10a.md, bureau-score-migration/bsm-app-gbm-v8.md, bureau-score-migration/feat-bsm-score-map-v2.md, bureau-score-migration/feat-bsm-score-map-v1.md, bureau-score-migration/feat-bsm-thin-file-flag.md, bureau-score-migration/feat-bsm-score-missing-impute.md, bureau-score-migration/ds-bsm-app-dev-2024.md, bureau-score-migration/ds-bsm-v8-history.md, bureau-score-migration/ds-bsm-dual-pull-sample.md, bureau-score-migration/ds-bsm-v10-cohorts-2026.md

## Q9
fsm-churn-xgb-v2 and fsm-spend-lgbm-v2 both build directly on feat-fsm-payment-lag-v2 and feat-fsm-spend-cv-30d. fsm-churn-xgb-v2 also builds on feat-fsm-util-ratio, which fsm-spend-lgbm-v2 does not list.
Notes: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/fsm-spend-lgbm-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
cli-logreg-baseline is the only current model note that builds directly on a replaced feature. It builds on feat-cli-util-v1, which feat-cli-util-v2 replaced on 2025-10-14. No note marks cli-logreg-baseline itself as retired, though its 2025 cutoff was superseded by dec-cli-uplift-targeting.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/feat-cli-util-v1.md, credit-line-increase/feat-cli-util-v2.md