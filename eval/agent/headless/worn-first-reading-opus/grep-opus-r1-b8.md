## Q1
The line ends at cld-gbm-v3: v1 was replaced by v2, and v2 by v3. cld-gbm-v3 is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three datasets. It is built directly on ds-cc-qa-labels and ds-cc-taxonomy-v3, and it reaches ds-cc-tickets-raw through both ds-cc-qa-labels and feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decisions rest on it. dec-xs-top-decile-offer comes through xs-gbm-v2 and exp-405. dec-xs-retrain-quarterly comes through xs-gbm-v2, exp-407 and find-xs-drift-2026. The path to xs-gbm-v2 runs through xs-gbm-v1 or feat-xs-payroll-flag-v2.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
The line ends at mrisk-gbm-v3, which is the current model: v1 was replaced by v2, and v2 by v3. mrisk-gbm-v3 is built on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline is built on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1. Through these it rests on two datasets: ds-cli-eligible-pop and ds-cli-outcome-90d (via feat-cli-spend-velocity).
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decisions rest on it. dec-clv-ship-ml-v1 comes through exp-501, clv-bgnbd-v1, clv-ml-v1 and fnd-clv-bgnbd-bias. dec-clv-ship-ml-v2 comes through clv-ml-v2 and dec-clv-ship-ml-v1, and it replaces dec-clv-ship-ml-v1.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
The line ends at pbs-gmm-v3, which is the current segment model: pbs-kmeans-v1 was replaced by pbs-gmm-v2, and pbs-gmm-v2 by pbs-gmm-v3. pbs-gmm-v3 is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 is built on exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated. Through these it rests on two datasets: ds-xs-callcentre, and ds-xs-offer-log, which ds-xs-callcentre is built on.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decisions rest on it:
- dec-disp-labels-two-analyst, directly.
- dec-disp-autoresolve-090, through disp-lgbm-v1/v2 and exp-301 to exp-305.
- dec-disp-autoresolve-095, through dec-disp-autoresolve-090, exp-305 and disp-find-precision-real.
- dec-disp-fraud-score-in, through exp-306 and exp-307.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
The line ends at rs-xgb-v3: v1 was replaced by v2, and v2 by v3. rs-xgb-v3 is built on exp-308 and rs-xgb-v2.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md