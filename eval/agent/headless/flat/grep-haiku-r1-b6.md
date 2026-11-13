## Q1
Three decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer and dec-xs-retrain-quarterly directly through xs-gbm-v1 and xs-gbm-v2, and dec-xs-call-low-deciles only through xs-call-uplift-v1. The last one is an inference: xs-call-uplift-v1 measures its effect in the deciles of xs-gbm-v2, but it does not name the model as a dependency.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md, work/dec-xs-call-low-deciles.md, work/feat-xs-balance-proxy.md, work/xs-gbm-v1.md, work/xs-gbm-v2.md, work/feat-xs-payroll-flag-v2.md, work/exp-405-top-decile.md, work/exp-407-oot-2026h1.md, work/find-xs-drift-2026.md, work/xs-call-uplift-v1.md

## Q2
The mrisk-gbm-v1 line ends in mrisk-gbm-v3, the model in force on 2026-11-12. It builds on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2. The chain is v1 → v2 (2026-06-09) → v3 (2026-10-08).
Notes: work/mrisk-gbm-v1.md, work/mrisk-gbm-v2.md, work/mrisk-gbm-v3.md

## Q3
cli-logreg-baseline rests on two dataset notes. ds-cli-eligible-pop feeds feat-cli-pay-behaviour and feat-cli-util-v1 directly. ds-cli-outcome-90d feeds feat-cli-spend-velocity.
Notes: work/cli-logreg-baseline.md, work/feat-cli-pay-behaviour.md, work/feat-cli-util-v1.md, work/feat-cli-spend-velocity.md, work/ds-cli-outcome-90d.md, work/ds-cli-eligible-pop.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2. The chain is holdout → exp-501-customer-lifetime-value → clv-bgnbd-v1 (through the BG/NBD versus GBM accuracy test) → clv-ml-v1 → dec-clv-ship-ml-v1 → clv-ml-v2 → dec-clv-ship-ml-v2.
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md, work/ds-clv-holdout-2021h1.md, work/exp-501-customer-lifetime-value.md, work/clv-bgnbd-v1.md, work/clv-ml-v1.md, work/clv-ml-v2.md

## Q5
pbs-kmeans-v1 is superseded by pbs-gmm-v2, which is in turn replaced by pbs-gmm-v3. pbs-gmm-v3 is the current segment model. It builds on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and the second GMM model.
Notes: work/pbs-kmeans-v1.md, work/pbs-gmm-v2.md, work/pbs-gmm-v3.md

## Q6
xs-call-uplift-v1 rests on two dataset notes. ds-xs-callcentre feeds exp-403-callcentre-naive, the naive call comparison and the recent-call feature. ds-xs-offer-log feeds ds-xs-callcentre through the eligible offer log.
Notes: work/xs-call-uplift-v1.md, work/exp-403-callcentre-naive.md, work/feat-xs-call-recent.md, work/find-xs-call-overstated.md, work/ds-xs-callcentre.md, work/ds-xs-offer-log.md

## Q7
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, and dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in through the dispute model chain. The link to dec-disp-fraud-score-in is inferred: exp-307 builds on "the fresh april 2026 labels experiment", which is not named, though it fits the same label set.
Notes: work/dec-disp-labels-two-analyst.md, work/dec-disp-autoresolve-090.md, work/dec-disp-autoresolve-095.md, work/dec-disp-fraud-score-in.md, work/ds-disp-analyst-labels.md, work/exp-301-dispute-triage.md, work/disp-lgbm-v2.md, work/disp-lgbm-v3.md, work/exp-307-dispute-triage.md

## Q8
rs-xgb-v1 was superseded by rs-xgb-v2 on 2025-09-18, and rs-xgb-v2 was superseded by rs-xgb-v3 on 2026-02-10. rs-xgb-v3 is the current model. It builds on exp-308-recovery-scoring and rs-xgb-v2.
Notes: work/rs-xgb-v1.md, work/rs-xgb-v2.md, work/rs-xgb-v3.md

## Q9
clv-bgnbd-v1 rests on three dataset notes. ds-clv-holdout-2021h1 is reached through the accuracy test in exp-501. ds-clv-revenue-monthly feeds the six-month revenue feature, and ds-clv-cohort-panel feeds the months-on-book feature through feat-clv-tenure. The accuracy-test link is inferred from the note wording.
Notes: work/clv-bgnbd-v1.md, work/exp-501-customer-lifetime-value.md, work/ds-clv-holdout-2021h1.md, work/feat-clv-arpu-v1.md, work/ds-clv-revenue-monthly.md, work/feat-clv-tenure.md, work/ds-clv-cohort-panel.md

## Q10
Two decision notes rest on ds-ed-bureau-join: dec-ed-promote-v3 directly, through ed-gbm-v3 and feat-ed-bureau-slope-v1, and dec-ed-gbm-for-watchlist. The second link is inferred: it builds on find-ed-gbm-vs-logit, which compares against the scorecard, and that scorecard is ed-logit-v1, which builds on ds-ed-bureau-join.
Notes: work/dec-ed-promote-v3.md, work/dec-ed-gbm-for-watchlist.md, work/ds-ed-bureau-join.md, work/ed-logit-v1.md, work/feat-ed-bureau-slope-v1.md, work/ed-gbm-v3.md, work/exp-201-early-delinquency.md, work/find-ed-gbm-vs-logit.md