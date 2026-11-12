## Q1
cld-gbm-v3 is the model in force at the end of the line (cld-gbm-v1 → v2 → v3). It is built on cld-gbm-v2 and feat-cld-payment-shock, which rest on cld-gbm-v1, feat-cld-risk-band-v2 and feat-cli-util-v2.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md, limit-decrease-policy/feat-cld-risk-band-v2.md

## Q2
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer (through xs-gbm-v2) and dec-xs-retrain-quarterly (through exp-407-oot-2026h1 and find-xs-drift-2026).
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v3 is the model in force (mrisk-gbm-v1 → v2 → v3). It is built on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2, which rest on the merchant-risk datasets and, through feat-mrisk-dispute-ratio, on dispute-triage's ds-disp-merchant-link.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop directly (via feat-cli-pay-behaviour, feat-cli-spend-velocity and feat-cli-util-v1), and ds-cli-outcome-90d, which is built on ds-cli-eligible-pop.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2, both through the clv-ml and exp-505 chain.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-gmm-v3 is the segment model in force (pbs-kmeans-v1 → pbs-gmm-v2 → pbs-gmm-v3). It is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2, which rest on the ds-pbs-payments-12m and ds-pbs-statement-balances datasets.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre (through exp-403-callcentre-naive and feat-xs-call-recent) and ds-xs-offer-log (through q-xs-propensity).
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst, dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in. The first two are directly built on the labels; the other two come through the auto-resolve experiments and disp-lgbm-v3.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v3 is the model in force (rs-xgb-v1 → v2 → v3). It is built on exp-308 and rs-xgb-v2, which rest on the recovery-scoring datasets and features.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md