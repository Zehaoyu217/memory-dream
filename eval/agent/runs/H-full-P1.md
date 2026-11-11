## Q1
feat-rs-region-rate is the out-of-fold recovery rate by postcode region, smoothed toward the book mean. It lifted Gini from 0.41 to 0.44 (exp-303), but exp-304 showed a 2.9x recovery spread across region deciles at equal balance and payment history, a proxy pattern compliance flagged. On 2025-05-22 the team agreed to drop it from all recovery-scoring models, accepting the 0.02 Gini cost.
Sources: recovery-scoring/feat-rs-region-rate.md, recovery-scoring/exp-303.md, recovery-scoring/exp-304.md, recovery-scoring/find-rs-region-proxy.md, recovery-scoring/dec-rs-drop-region.md

## Q2
exp-403-callcentre-naive found a raw open-rate gap of 4.9% with a call against 3.1% without, which is +1.8 points. After matching on propensity and tenure the effect was +0.6 points (CI -0.1 to +1.3), not significant, so most of the gap was selection. The causal forest in xs-call-uplift-v1 then found +1.2 points in deciles 1-2, and the decision dec-xs-call-low-deciles limits call-centre outreach to those deciles.
Sources: cross-sell-savings/exp-403-callcentre-naive.md, cross-sell-savings/find-xs-call-overstated.md, cross-sell-savings/xs-call-uplift-v1.md, cross-sell-savings/dec-xs-call-low-deciles.md

## Q3
sfc-hier-v3 is a LightGBM base forecast for six segments, reconciled across segments and the total with MinT (exp-207), and it adds feat-sfc-active-accounts as a regressor. It also uses feat-sfc-cpi-lag6, the six-month lag of year-on-year CPI, and it was built from the sfc-lgbm-v2 line. Finance adopted it for FY26 volume, and revenue-forecast-2026 uses it as the spend input for interchange.
Sources: spend-forecasting/sfc-hier-v3.md, spend-forecasting/exp-207.md, spend-forecasting/feat-sfc-active-accounts.md, spend-forecasting/feat-sfc-cpi-lag6.md, spend-forecasting/dec-sfc-ship-hier-v3.md

## Q4
The fraud-2026 model now uses an alert threshold of 0.66 on fraud26-gbm-v3, the current model promoted on 2026-08-26 in place of v2's 0.62. The 0.66 cut was chosen for 21.5% precision at a 0.6% alert rate (recall 0.61), against 17.8% precision at 0.62, to keep alert volume near the 2025 level.
Sources: fraud-2026/dec-f26-promote-v3.md, fraud-2026/exp-208.md, fraud-2026/fraud26-gbm-v3.md, fraud-2026/dec-f26-promote-v2.md

## Q5
mrisk-gbm-v2 reached AUC 0.86 and precision@100 of 0.43 on mrisk-oot-2026h1 (exp-505). It has since been superseded by mrisk-gbm-v3, which reached AUC 0.91 and precision@100 0.58 on the same set (exp-507).
Sources: merchant-risk/mrisk-gbm-v2.md, merchant-risk/exp-505.md, merchant-risk/exp-507.md, merchant-risk/mrisk-gbm-v3.md

## Q6
app-scorecard-v3's Gini fell from 0.41 to 0.33 on the 2026-Q1 holdout as bureau scores drifted, so the team set a target of 0.42 out-of-time Gini with no manual overrides. v4 was rebuilt on the v10 bands, the income estimate and reject-inference weights, and it reached Gini 0.42 against 0.35 for v3 on application-scorecard-oot-2026h1 (exp-507). The rebuild was decided on 2026-06-26 (dec-app-rebuild-v4).
Sources: application-scorecard/find-app-gini-v3-drift.md, application-scorecard/q-app-gini-target.md, application-scorecard/dec-app-rebuild-v4.md, application-scorecard/exp-507.md, application-scorecard/app-scorecard-v4.md

## Q7
feat-txc-normalise-v2 strips store numbers, '#' codes, trailing city and state suffixes and repeated whitespace from transaction descriptors before tokenising. On txc-gbm-v2 it lifted holdout-2025q2 macro-F1 from 0.78 to 0.81 (exp-104), mostly in Travel and Fuel. It is an input to txc-gbm-v3, which shipped on 2026-03-10 with macro-F1 0.83 on txc-oot-2026h1, and its rule list is versioned in the repo and changed by pull request.
Sources: txn-categorization/feat-txc-normalise-v2.md, txn-categorization/exp-104.md, txn-categorization/txc-gbm-v3.md, txn-categorization/dec-txc-ship-gbm-v3.md

## Q8
exp-205 added the 6-month payment-to-minimum ratio (feat-ed-minpay-v2) to ed-gbm-v1 and, with no limit-change feature, lifted AUC from 0.781 to 0.803 on early-delinquency-holdout-2024q4. The team then built ed-gbm-v2 on it in September 2025, and find-ed-minpay recommended it as the replacement for the limit-change feature. The later ed-gbm-v3 (AUC 0.809 on OOT 2026H1) keeps it.
Sources: early-delinquency/exp-205.md, early-delinquency/find-ed-minpay.md, early-delinquency/ed-gbm-v2.md, early-delinquency/feat-ed-minpay-v2.md, early-delinquency/ed-gbm-v3.md

## Q9
fsm-churn-xgb-v2 reads 41 store features: the v1 set of 40 with the store version of the payment lag (feat-fsm-payment-lag-v2, UTC timestamps) and the store util ratio (feat-fsm-util-ratio, latest limit on or before month-end), plus feat-fsm-spend-cv-30d. It reads v2 features only.
Sources: feature-store-migration/fsm-churn-xgb-v2.md, feature-store-migration/feat-fsm-payment-lag-v2.md, feature-store-migration/feat-fsm-util-ratio.md, feature-store-migration/feat-fsm-spend-cv-30d.md, feature-store-migration/dec-fsm-cutover.md

## Q10
The approval cutoff on the v10 scale is 652, which matches the v8 cutoff of 640 at a 58% approval rate and 4.1% bad rate (exp-305). It was set by dec-bsm-cutover-2026q3 to take effect on 2026-09-01, using bsm-app-gbm-v10b and the bsm-cutoff-logit recalibration, with the v8 fallback kept.
Sources: bureau-score-migration/dec-bsm-cutover-2026q3.md, bureau-score-migration/exp-305.md, bureau-score-migration/bsm-cutoff-logit.md, bureau-score-migration/bsm-app-gbm-v10b.md