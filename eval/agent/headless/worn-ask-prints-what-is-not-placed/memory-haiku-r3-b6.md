## Q1
The only note from another project built directly on fraud26-gbm-v3 is dispute-triage/feat-disp-fraud-score, which takes the model's score for each dispute. The dispute-triage decision dec-disp-fraud-score-in only names fraud26-gbm-v3 as a dependency; its build line lists exp-307 and feat-disp-fraud-score, not the model.
Notes: dispute-triage/feat-disp-fraud-score.md

## Q2
churn-gbm-2025-v2 rests on four dataset notes: ds-c25-accounts-snapshot and ds-c25-app-engagement directly or through its features and experiments, and ds-c25-oot-2024h1 and ds-c25-churn-labels through the experiments and decisions.
Notes: churn-2025/ds-c25-accounts-snapshot.md, churn-2025/ds-c25-app-engagement.md, churn-2025/ds-c25-oot-2024h1.md, churn-2025/ds-c25-churn-labels.md

## Q3
rdm-propensity-lr and rdm-uplift-v1 both build directly on feat-rdm-app-installed and feat-rdm-last-activity-v1.
Notes: reactivation-dormant/feat-rdm-app-installed.md, reactivation-dormant/feat-rdm-last-activity-v1.md

## Q4
rdm-propensity-lr is the only current model that builds directly on a replaced feature or dataset: it uses feat-rdm-last-activity-v1, which was superseded by feat-rdm-last-activity-v2. rdm-uplift-v2 uses only current features, and rdm-uplift-v1 is itself superseded.
Notes: reactivation-dormant/rdm-propensity-lr.md

## Q5
Four decision notes rest on ds-csb-churn-labels: dec-csb-90d-window directly, and dec-csb-tenure-floor, dec-csb-ship-xgb-v1 and dec-csb-ship-xgb-v2 through the LR baseline and XGBoost chain.
Notes: churn-small-business/dec-csb-90d-window.md, churn-small-business/dec-csb-tenure-floor.md, churn-small-business/dec-csb-ship-xgb-v1.md, churn-small-business/dec-csb-ship-xgb-v2.md

## Q6
The note in force is find-hp-effect-v2, which gives a 4.7pp reduction in the 30-to-60 roll. It is built directly on exp-404, exp-408 and find-hp-adjusted-effect.
Notes: hardship-programs/find-hp-effect-v2.md, hardship-programs/exp-404.md, hardship-programs/exp-408.md, hardship-programs/find-hp-adjusted-effect.md

## Q7
Only application-scorecard/feat-app-income-est built directly on inc-gbm-v3 from another project; it takes the live income estimate as an input band.
Notes: application-scorecard/feat-app-income-est.md

## Q8
csb-lr-base rests on three dataset notes: ds-csb-churn-labels and ds-csb-oot-2025q1 directly, and ds-csb-biz-accounts, the root dataset, through them.
Notes: churn-small-business/ds-csb-churn-labels.md, churn-small-business/ds-csb-oot-2025q1.md, churn-small-business/ds-csb-biz-accounts.md

## Q9
trv-ridge-v2 and trv-ridge-v3 both build directly on feat-trv-cross-border-share and feat-trv-seasonality-adj.
Notes: travel-spend-recovery/feat-trv-cross-border-share.md, travel-spend-recovery/feat-trv-seasonality-adj.md

## Q10
ror-uplift-v1, which is still current, builds directly on feat-ror-value-band-v1, and feat-ror-value-band-v2 supersedes that feature. ror-roi-v2 builds only on current inputs, so ror-uplift-v1 is the only match.
Notes: retention-offers-roi/ror-uplift-v1.md, retention-offers-roi/feat-ror-value-band-v1.md