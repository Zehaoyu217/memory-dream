## Q1
Only `dispute-triage/feat-disp-fraud-score.md` builds directly on fraud-2026/fraud26-gbm-v3. `dispute-triage/dec-disp-fraud-score-in.md` says it creates a dependency on the model, but its "Builds on" line names only exp-307 and that feature note.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
Its dataset roots are the four dataset notes below, reached through the decision, experiment and feature notes it builds on: the account-month snapshot, the 60-day churn labels, the app engagement data (via the app-session feature), and the 2024 holdout.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
Both build directly on `feat-rdm-app-installed` and `feat-rdm-last-activity-v1`, per their "Builds on" lines. `rdm-uplift-v1`'s body also uses prior response and balance band as inputs, but its "Builds on" line doesn't name them.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
`rdm-propensity-lr` is still the kept baseline and builds directly on `feat-rdm-last-activity-v1`, which `feat-rdm-last-activity-v2` replaced in June 2025. `rdm-uplift-v2` builds only on current features, and `rdm-uplift-v1` is superseded.
Notes: reactivation-dormant/rdm-propensity-lr.md

## Q5
Four decisions rest on `ds-csb-churn-labels`: `dec-csb-90d-window` directly, and `dec-csb-tenure-floor`, `dec-csb-ship-xgb-v1` and `dec-csb-ship-xgb-v2` through `csb-lr-base`, `exp-202`, `exp-203` and the XGBoost chain.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The line ends at `find-hp-effect-v2`, the current effect of -4.7pp. It is built on `exp-404` (the difference-in-differences check), `exp-408` (the propensity matching holdout) and `find-hp-adjusted-effect`, which itself replaced `find-hp-naive-effect`.
Notes: hardship-programs/find-hp-naive-effect.md, hardship-programs/find-hp-adjusted-effect.md, hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md

## Q7
Only `application-scorecard/feat-app-income-est.md` builds directly on `income-estimation/inc-gbm-v3`.
Notes: application-scorecard/feat-app-income-est.md

## Q8
`csb-lr-base` rests on three dataset notes: the SMB account population (directly, and through the feature and label notes), the 90-day churn labels, and the Q1 2025 holdout.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q9
Both build directly on `feat-trv-cross-border-share` and `feat-trv-seasonality-adj`.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
`ror-uplift-v1` is the only current model that builds on a replaced feature: its "Builds on" line includes the first value-band feature, which `feat-ror-value-band-v2` replaced. It is still in use as the input to the current `ror-roi-v2`.
Notes: retention-offers-roi/ror-uplift-v1.md