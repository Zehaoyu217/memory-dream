## Q1
cld-gbm-v1 was replaced by cld-gbm-v2, which was replaced by cld-gbm-v3, so cld-gbm-v3 is the one in force now (AUC 0.81 on cld-test-2026q1). It is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 is built on ds-cc-qa-labels, ds-cc-taxonomy-v3 and feat-cc-embed-v1. Both ds-cc-qa-labels and feat-cc-embed-v1 are built on the raw ticket table. So it rests on three datasets: ds-cc-qa-labels, ds-cc-taxonomy-v3 and ds-cc-tickets-raw.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decisions. dec-xs-top-decile-offer rests on the balance proxy through xs-gbm-v1, xs-gbm-v2 and exp-405. dec-xs-retrain-quarterly rests on it through xs-gbm-v2, exp-407 and find-xs-drift-2026. dec-xs-call-low-deciles does not rest on the balance proxy.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v1 was replaced by mrisk-gbm-v2, which was replaced by mrisk-gbm-v3, the current model (AUC 0.91, watchlist cut 0.65). It is built on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline is built on feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1. Those lead back to two datasets: ds-cli-eligible-pop and ds-cli-outcome-90d (which is itself built on ds-cli-eligible-pop).
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
The holdout feeds exp-501, which leads through clv-bgnbd-v1, fnd-clv-bgnbd-bias, exp-503 and clv-ml-v1 to dec-clv-ship-ml-v1. That decision, along with clv-ml-v2, leads to dec-clv-ship-ml-v2. dec-clv-include-losses and dec-clv-discount-rate do not rest on the holdout.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-kmeans-v1 was replaced by pbs-gmm-v2, which was replaced by pbs-gmm-v3, the current segment model (five components, seed ARI 0.81). It is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 is built on exp-403-callcentre-naive, feat-xs-call-recent and find-xs-call-overstated. These lead back to ds-xs-callcentre, which is built on ds-xs-offer-log. So it rests on two datasets: ds-xs-callcentre and ds-xs-offer-log.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
All four decision notes in dispute-triage rest on the analyst labels. dec-disp-labels-two-analyst is built on them directly. dec-disp-autoresolve-090 and dec-disp-autoresolve-095 rest on them through disp-lgbm-v2 and exp-304/305. dec-disp-fraud-score-in rests on them through exp-306 and exp-307.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v1 was replaced by rs-xgb-v2, which was replaced by rs-xgb-v3 (v2 plus a regression head for recovered share and a 2025 recalibration), so v3 is in force now. It is built on exp-308 and rs-xgb-v2.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md