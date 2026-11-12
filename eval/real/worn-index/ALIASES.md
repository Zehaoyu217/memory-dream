# ALIASES — entity ids that name the same thing; the first id on a line is canonical. Edit freely.
- top-40-capture = top-40pct-capture | why: Both are the same metric written as "top 40%" and "top-40% capture" ("Top-40% capture"), the share of SAR-referred alerts in the top 40%. | by: curator 2026-11-12
- ds-bt-holdout-2025q1 = bt-holdout-2025q1 | why: Both are datasets, and the note "Builds on bt-logit-baseline and ds-bt-holdout-2025q1" uses the ds- prefix for the same holdout set. | by: curator 2026-11-12
- cr-logreg-v1 = logistic-regression-baseline | why: "the logistic regression baseline" and "Multinomial logistic regression baseline" name the same baseline model. | by: curator 2026-11-12
- ds-cb-rewards-ledger = cb.rewards_ledger | why: Both are the rewards ledger dataset: `cb.rewards_ledger` in some notes, "ds-cb-rewards-ledger" in others, with the same rewards-cost role. | by: curator 2026-11-12
- flat-1-25 = flat-1.25-cell | why: "flat 1.25% pilot cell" and "Flat 1.25% cell" name the same flat 1.25% arm of the pilot. | by: curator 2026-11-12
- containment = containment-rate | why: Both are metrics written as "34 percent containment", and containment-rate is the same containment figure. | by: curator 2026-11-12
- ds-c25-oot-2024h1 = c25-oot-2024h1 | why: Both are the "Holdout c25-oot-2024h1" dataset, written with the same name. | by: curator 2026-11-12
- recall-at-10 = recall-at-10pct | why: Both are written as "recall@10% 0.27" or "recall@10% 0.34", so they name the same metric at the same 10% cutoff. | by: curator 2026-11-12
- ds-xs-offer-log = sav-offer-log | why: "offer log" is written for both, and ds-xs-offer-log is described as "the eligible offer log table", which is the `sav.offer_log` table. | by: curator 2026-11-12
- ds-dq-partition-arrivals = dq.partition_arrivals | why: Both are datasets about one row per partition's arrival, and the notes write the same name in two forms (dotted and hyphenated). | by: curator 2026-11-12
- live-alert-threshold = threshold-0.62 | why: "0.62 alert threshold" and "score >= 0.62" under threshold-0.62 match "The 0.62 threshold" under live-alert-threshold, the same alert cutoff. | by: curator 2026-11-12
- lbl-fraud-gbm-v4 = fraud-model-v4 | why: "Fraud model v4" in the exp-405 note and "lbl-fraud-gbm-v4" in the promotion decision name the same fraud model version. | by: curator 2026-11-12
- feat-lbl-churn-flag-60d = churn-60-day-rule | why: "The 60-day rule" and "the 60-day version" name the churn definition that the feature flag "no approved transaction in 60 days" implements. | by: curator 2026-11-12
- feat-lbl-churn-flag-90d = churn-90-day-rule | why: "90-day rule" and the flag "no approved transaction in 90 days" are the same churn definition, with the feature as its implementation. | by: curator 2026-11-12
- dec-cld-cap-25pct = cap-25pct | why: Both name the same 25% per-cycle cap on risk-based decreases ("cap any single risk-based decrease at 25% of the prior limit per cycle" and "the 25% per-cycle ca | by: curator 2026-11-12
- ds-mm-reference-train = mon.reference_samples | why: Both notes write the thing as "the frozen training reference samples table", and ds-mm-reference-train's note says it builds on that same table. | by: curator 2026-11-12
- feat-nps-complaint-flag-v1 = complaint-flag | why: The notes call the feature "Complaint flag" (any complaint call in the 90 days before send) and "the complaint call flag feature", so the v1 id names the same f | by: curator 2026-11-12
- feat-rdm-last-activity-v2 = last-activity-v2 | why: Both are the v2 activity feature, written as "the v2 activity feature" and "last activity v2" / "last-activity v2". | by: curator 2026-11-12
- ds-rdm-dormant-pool = reactivation-pool | why: "Dormant pool" and "the pool" both name the accounts dormant for 6 or more months. | by: curator 2026-11-12
- 29.99-apr-cap = apr-cap-29-99 | why: "29.99% APR cap" and "29.99% cap scenario" name the same policy, with the same $54M figure. | by: curator 2026-11-12
- ds-rev26-rate-schedule = fin.rate_schedule | why: Both describe the APR rate schedule with the roll-off dates of the 0% promo cohorts, so they look like one table written two ways. | by: curator 2026-11-12
- sfc-ets-v1 = holt-winters | why: sfc-ets-v1 is written as "the holt-winters segment model", and holt-winters is written as "Damped Holt-Winters" and "Holt-Winters". | by: curator 2026-11-12
not: app-sessions / feat-mq3-app-sessions-30d | by: review 2026-11-12
- band-under-640 = under-640-band | by: review 2026-11-12
- ds-bt-offer-log = bt.offer_log | by: review 2026-11-12
not: ds-ror-holdout-2025q3 / holdout-2025q3 | by: review 2026-11-12
not: lena-fischer / maya-ortiz | by: review 2026-11-12
- lift = lift-top-decile | by: review 2026-11-12
- recall-at-10 = metric-recall-at-10 | by: review 2026-11-12
not: mq3-response-gbm-v1 / response-model | by: review 2026-11-12
not: rdm-uplift-v1 / t-learner | by: review 2026-11-12
not: recall / recall-at-1pct | by: review 2026-11-12
- recall-at-1pct = recall-at-1 | by: review 2026-11-12
not: retention-uplift / uplift | by: review 2026-11-12
not: retention-uplift / uplift-at-20 | by: review 2026-11-12
not: uplift / uplift-at-20 | by: review 2026-11-12
