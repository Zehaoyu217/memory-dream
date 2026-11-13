## Q1
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2) and dec-xs-retrain-quarterly (through find-xs-drift-2026). The memory tool's list of 90 unplaced notes was not counted, since no note links them to this feature.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
mrisk-gbm-v3 is the one in force (mrisk-gbm-v1 → v2 → v3). It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes. Its features come from feat-cli-util-v1 (via ds-cli-eligible-pop and q-cli-utilization-trigger), feat-cli-pay-behaviour (via ds-cli-eligible-pop) and feat-cli-spend-velocity (via ds-cli-outcome-90d, which builds on ds-cli-eligible-pop). The memory tool's dependency summary printed a different model's chain (churn-lr-base-2025), so I followed the note texts instead.
Notes: work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2. The link runs through exp-501-customer-lifetime-value, which clv-bgnbd-v1 names as its "bg/nbd versus gbm accuracy test", then clv-ml-v1, then the two decisions. exp-502 also scores on the same holdout, but it does not name it as an input, so the finance-netting decisions are not counted.
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md

## Q5
dec-pbs-gmm-v3-current is in force (pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3 → this decision). It is built on fnd-pbs-five-segments and pbs-gmm-v3.
Notes: work/dec-pbs-gmm-v3-current.md, work/fnd-pbs-five-segments.md, work/pbs-gmm-v3.md

## Q6
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (via exp-403-callcentre-naive and feat-xs-call-recent) and ds-xs-offer-log (via q-xs-propensity, for the propensity covariates). Its words-only links all point to notes already in that chain.
Notes: work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst (direct), and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in (through disp-lgbm-v1, disp-lgbm-v2 and disp-lgbm-v3).
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md

## Q8
rs-xgb-v3 is the one in force (rs-xgb-v1 → v2 → v3). It is built on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v3.md, work/exp-308-recovery-scoring.md, work/rs-xgb-v2.md

## Q9
clv-bgnbd-v1 rests on three dataset notes: ds-clv-cohort-panel and ds-clv-revenue-monthly (through feat-clv-tenure and feat-clv-arpu-v1), and ds-clv-holdout-2021h1 (through exp-501, the accuracy test it names in its own words).
Notes: work/ds-clv-cohort-panel.md, work/ds-clv-revenue-monthly.md, work/ds-clv-holdout-2021h1.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 (through ed-gbm-v3) and dec-ed-gbm-for-watchlist (through ed-logit-v1 and ed-gbm-v2). The second is superseded but still rests on the join.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md