## Q1
Two decision notes rest on feat-xs-balance-proxy. dec-xs-top-decile-offer and dec-xs-retrain-quarterly both reach it through xs-gbm-v2, which builds on xs-gbm-v1 (built on the proxy); the retrain decision goes via exp-407 and the top-decile decision via exp-405.
Notes: work/dec-xs-top-decile-offer.md, work/dec-xs-retrain-quarterly.md

## Q2
The line runs mrisk-gbm-v1 → mrisk-gbm-v2 → mrisk-gbm-v3, and mrisk-gbm-v3 is the one in force. It is built on exp-507-merchant-risk, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: work/mrisk-gbm-v3.md, work/exp-507-merchant-risk.md, work/feat-mrisk-dispute-ratio.md, work/mrisk-gbm-v2.md

## Q3
cli-logreg-baseline rests on two dataset notes. ds-cli-eligible-pop is the base for feat-cli-pay-behaviour and feat-cli-util-v1, and ds-cli-outcome-90d (which builds on ds-cli-eligible-pop) is the base for feat-cli-spend-velocity.
Notes: work/ds-cli-eligible-pop.md, work/ds-cli-outcome-90d.md

## Q4
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 (via exp-501, clv-bgnbd-v1 and fnd-clv-bgnbd-bias) and dec-clv-ship-ml-v2 (via clv-ml-v1, exp-503 and dec-clv-ship-ml-v1). dec-clv-include-losses and dec-clv-discount-rate do not count, because their stated basis (exp-502) uses the holdout only as a test set.
Notes: work/dec-clv-ship-ml-v1.md, work/dec-clv-ship-ml-v2.md

## Q5
The line runs pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3, and pbs-gmm-v3 is the one in force. It is built on exp-403-payment-behavior-segments, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: work/pbs-gmm-v3.md, work/exp-403-payment-behavior-segments.md, work/feat-pbs-timing-v2.md, work/pbs-gmm-v2.md