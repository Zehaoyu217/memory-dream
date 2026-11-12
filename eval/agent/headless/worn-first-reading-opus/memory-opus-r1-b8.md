## Q1
cld-gbm-v1 was replaced by cld-gbm-v2, and cld-gbm-v2 was replaced by cld-gbm-v3, which is the one in force now. cld-gbm-v3 is built on cld-gbm-v2 and feat-cld-payment-shock.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/feat-cld-payment-shock.md

## Q2
cc-ft-v1 rests on three dataset notes. It uses ds-cc-qa-labels and ds-cc-taxonomy-v3 directly. It also reaches ds-cc-tickets-raw through ds-cc-qa-labels and feat-cc-embed-v1.
Notes: complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer and dec-xs-retrain-quarterly. Both reach it through other notes, not directly.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v1 was replaced by mrisk-gbm-v2, and mrisk-gbm-v2 was replaced by mrisk-gbm-v3, which is the one in force now. mrisk-gbm-v3 is built on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md, merchant-risk/mrisk-gbm-v2.md

## Q5
cli-logreg-baseline rests on two dataset notes, ds-cli-eligible-pop and ds-cli-outcome-90d. It reaches both through its feature notes.
Notes: credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1 and dec-clv-ship-ml-v2. Both reach it through exp-501 and the notes built on it.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-kmeans-v1 was replaced by pbs-gmm-v2, and pbs-gmm-v2 was replaced by pbs-gmm-v3, which is the one in force now. pbs-gmm-v3 is built on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md, payment-behavior-segments/pbs-gmm-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes, ds-xs-callcentre and ds-xs-offer-log. ds-xs-callcentre itself is built on ds-xs-offer-log.
Notes: cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels. dec-disp-labels-two-analyst is built on it directly. dec-disp-autoresolve-090, dec-disp-autoresolve-095 and dec-disp-fraud-score-in reach it through other notes.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v1 was replaced by rs-xgb-v2, and rs-xgb-v2 was replaced by rs-xgb-v3, which is the one in force now. rs-xgb-v3 is built on exp-308 and rs-xgb-v2.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/exp-308.md, recovery-scoring/rs-xgb-v2.md