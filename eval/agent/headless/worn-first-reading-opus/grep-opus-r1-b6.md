I've read all the notes I need and am writing up the answers now.

## Q1
Only one note in another project builds directly on fraud26-gbm-v3: the dispute-triage feature that takes the fraud-2026 v3 score on the original authorisation. The dispute decision and disp-lgbm-v3 reach v3 only through that feature.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
Tracing every "Builds on" link back from churn-gbm-2025-v2, the chain reaches all four churn-2025 datasets: the account-month snapshot, the app-engagement data, the churn labels and the 2024H1 out-of-time holdout. The labels and holdout themselves rest on the snapshot.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-churn-labels.md, churn-2025/ds-c25-oot-2024h1.md

## Q3
Both models build directly on the app-installed flag and on last-activity v1. The propensity baseline also uses balance band and prior response, but rdm-uplift-v1 does not list those.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is still kept as the baseline and builds directly on feat-rdm-last-activity-v1, which last-activity v2 replaced. rdm-uplift-v1 also uses v1, but it is no longer current because rdm-uplift-v2 replaced it.
Notes: reactivation-dormant/rdm-propensity-lr.md

## Q5
Four decision notes rest on ds-csb-churn-labels. The 90-day window decision builds on it directly. The tenure floor builds on it through exp-202 and fnd-csb-tenure-cut. Both ship decisions build on it through csb-lr-base, exp-203/exp-204 and the xgb models.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
find-hp-naive-effect was replaced by find-hp-adjusted-effect, which was then replaced by find-hp-effect-v2 (−4.7pp). That is the note in force now. It builds on exp-404 (difference-in-differences), exp-408 (caliper matching on the holdout) and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
Only application-scorecard's income-band feature builds directly on inc-gbm-v3. The other scorecard notes use the estimate only through that feature.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three datasets: the churn labels and the 2025Q1 holdout directly, and the SMB account base through those two and its spend and tenure features.
Notes: churn-small-business/ds-csb-biz-accounts.md, churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md

## Q9
Both build directly on the cross-border share feature and the seasonality-adjustment feature. trv-ridge-v3 also adds funnel v2.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1 has not been replaced and still feeds the current ror-roi-v2. It builds directly on feat-ror-value-band-v1, which value band v2 replaced. ror-roi-v2 itself uses value band v2.
Notes: retention-offers-roi/ror-uplift-v1.md