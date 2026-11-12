## Q1
cld-gbm-v1 was replaced by cld-gbm-v2, which was replaced by cld-gbm-v3, the note in force. cld-gbm-v3 builds directly on cld-gbm-v2 and feat-cld-payment-shock, and through them on cld-gbm-v1, feat-cld-util-after-decrease, feat-cld-risk-band-v2 and the decrease cohort.
Notes: limit-decrease-policy/cld-gbm-v3.md, limit-decrease-policy/cld-gbm-v2.md, limit-decrease-policy/cld-gbm-v1.md, limit-decrease-policy/feat-cld-payment-shock.md, limit-decrease-policy/feat-cld-util-after-decrease.md, limit-decrease-policy/feat-cld-risk-band-v2.md, limit-decrease-policy/ds-cld-decrease-cohort.md

## Q2
cc-ft-v1 rests on three dataset notes: ds-cc-qa-labels and ds-cc-taxonomy-v3 directly, and ds-cc-tickets-raw through ds-cc-qa-labels and feat-cc-embed-v1.
Notes: complaint-classification/cc-ft-v1.md, complaint-classification/ds-cc-qa-labels.md, complaint-classification/ds-cc-taxonomy-v3.md, complaint-classification/ds-cc-tickets-raw.md

## Q3
Two decision notes rest on feat-xs-balance-proxy: dec-xs-top-decile-offer, which builds on xs-gbm-v2 via feat-xs-payroll-flag-v2, and dec-xs-retrain-quarterly, which builds on exp-407-oot-2026h1 and find-xs-drift-2026.
Notes: cross-sell-savings/dec-xs-top-decile-offer.md, cross-sell-savings/dec-xs-retrain-quarterly.md

## Q4
mrisk-gbm-v1 was replaced by mrisk-gbm-v2, which was replaced by mrisk-gbm-v3, the note in force. mrisk-gbm-v3 builds directly on exp-507, feat-mrisk-dispute-ratio and mrisk-gbm-v2, and through them on mrisk-gbm-v1, exp-504, feat-mrisk-mcc-base, the merchant-month panel, the chargeback labels and dispute-triage's ds-disp-merchant-link.
Notes: merchant-risk/mrisk-gbm-v3.md, merchant-risk/mrisk-gbm-v2.md, merchant-risk/mrisk-gbm-v1.md, merchant-risk/exp-507.md, merchant-risk/feat-mrisk-dispute-ratio.md

## Q5
cli-logreg-baseline rests on two dataset notes: ds-cli-eligible-pop, which feeds feat-cli-pay-behaviour, feat-cli-util-v1 and q-cli-utilization-trigger, and ds-cli-outcome-90d, which feeds feat-cli-spend-velocity.
Notes: credit-line-increase/cli-logreg-baseline.md, credit-line-increase/ds-cli-eligible-pop.md, credit-line-increase/ds-cli-outcome-90d.md

## Q6
Two decision notes rest on ds-clv-holdout-2021h1: dec-clv-ship-ml-v1, through exp-501 and fnd-clv-bgnbd-bias, and dec-clv-ship-ml-v2, through exp-505 and fnd-clv-offer-cost.
Notes: customer-lifetime-value/dec-clv-ship-ml-v1.md, customer-lifetime-value/dec-clv-ship-ml-v2.md

## Q7
pbs-kmeans-v1 was replaced by pbs-gmm-v2, which was replaced by pbs-gmm-v3, the note in force. pbs-gmm-v3 builds directly on exp-403, feat-pbs-timing-v2 and pbs-gmm-v2, and through them on exp-402, feat-pbs-interest-paid, pbs-kmeans-v1, and the payments and statement-balance datasets.
Notes: payment-behavior-segments/pbs-gmm-v3.md, payment-behavior-segments/pbs-gmm-v2.md, payment-behavior-segments/pbs-kmeans-v1.md, payment-behavior-segments/exp-403.md, payment-behavior-segments/feat-pbs-timing-v2.md

## Q8
xs-call-uplift-v1 rests on two dataset notes: ds-xs-callcentre, which feeds exp-403-callcentre-naive and feat-xs-call-recent, and ds-xs-offer-log, which feeds ds-xs-callcentre.
Notes: cross-sell-savings/xs-call-uplift-v1.md, cross-sell-savings/ds-xs-callcentre.md, cross-sell-savings/ds-xs-offer-log.md

## Q9
Four decision notes rest on ds-disp-analyst-labels: dec-disp-labels-two-analyst directly, dec-disp-autoresolve-090 and dec-disp-autoresolve-095 through exp-301 to exp-305, and dec-disp-fraud-score-in through disp-lgbm-v2 and exp-306 to exp-307.
Notes: dispute-triage/dec-disp-labels-two-analyst.md, dispute-triage/dec-disp-autoresolve-090.md, dispute-triage/dec-disp-autoresolve-095.md, dispute-triage/dec-disp-fraud-score-in.md

## Q10
rs-xgb-v1 was replaced by rs-xgb-v2, which was replaced by rs-xgb-v3, the note in force. rs-xgb-v3 builds directly on exp-308 and rs-xgb-v2, and through them on rs-xgb-v1, exp-306, feat-rs-contact-attempts, find-rs-region-proxy, exp-303, ds-rs-agency-placements and ds-rs-chargeoff-base.
Notes: recovery-scoring/rs-xgb-v3.md, recovery-scoring/rs-xgb-v2.md, recovery-scoring/rs-xgb-v1.md, recovery-scoring/exp-308.md