## Q1
feat-rs-region-rate is an out-of-fold, smoothed target-encoded recovery rate by postcode region. It added about 0.02 Gini (0.41 to 0.44 in exp-303), but the region deciles spread 2.9x at equal balance and payment history, so compliance treated it as a proxy for neighbourhood demographics. It was dropped from all recovery-scoring models on 2025-05-22 (removed from rs-xgb-v2, excluded from rs-xgb-v3), accepting the 0.02 Gini cost.
Sources: memory/recovery-scoring/feat-rs-region-rate.md, memory/recovery-scoring/dec-rs-drop-region.md, memory/recovery-scoring/find-rs-region-proxy.md

## Q2
exp-403 found a naive call effect of +1.8 points (open rate 4.9% with a call vs 3.1% without), which fell to +0.6 points (CI -0.1 to +1.3, not significant) once matched on propensity and tenure. That finding showed the raw gap was mostly selection. It led to the causal forest in xs-call-uplift-v1, which gives +1.2 points in deciles 1-2, and to the decision to send call-centre outreach only to deciles 1-2.
Sources: memory/cross-sell-savings/exp-403-callcentre-naive.md, memory/cross-sell-savings/find-xs-call-overstated.md, memory/cross-sell-savings/xs-call-uplift-v1.md, memory/cross-sell-savings/dec-xs-call-low-deciles.md

## Q3
sfc-hier-v3 depends on LightGBM base forecasts for the six segments, reconciled with MinT across segments and the total. It uses feat-sfc-active-accounts as a regressor, and it was built on fnd-sfc-q4-reconciled and exp-207. It supersedes sfc-lgbm-v2, and it was adopted for FY26 volume (total MAPE 2.3% on sfc-oot-2025h2).
Sources: memory/spend-forecasting/sfc-hier-v3.md, memory/spend-forecasting/dec-sfc-ship-hier-v3.md

## Q4
The fraud-2026 model fraud26-gbm-v3 uses an alert threshold of 0.66, set by dec-f26-promote-v3 on 2026-08-26 (replacing 0.62 from v2). At 0.66 exp-208 gave 21.5% precision at a 0.6% alert rate.
Sources: memory/fraud-2026/dec-f26-promote-v3.md, memory/fraud-2026/fraud26-gbm-v3.md, memory/fraud-2026/exp-208.md

## Q5
mrisk-gbm-v2 reached AUC 0.86 and precision@100 0.43 on mrisk-oot-2026h1 (exp-505, 2026-07-06). It was later superseded by mrisk-gbm-v3, which reached AUC 0.91 and precision@100 0.58 on the same set.
Sources: memory/merchant-risk/mrisk-gbm-v2.md, memory/merchant-risk/exp-505.md

## Q6
The v3 scorecard's Gini fell from 0.41 to 0.33 on the 2026-Q1 holdout (n=18,900) because the v8 bureau score drifted, while the utilisation and velocity features stayed stable. v4 was rebuilt on the v10 bureau bands, reject-inference weights and the income estimate, keeping the points-based form. Lena Fischer approved it on 2026-06-26.
Sources: memory/application-scorecard/dec-app-rebuild-v4.md, memory/application-scorecard/find-app-gini-v3-drift.md, memory/application-scorecard/app-scorecard-v4.md

## Q7
feat-txc-normalise-v2 strips store numbers, '#' hash codes, trailing city and state suffixes, and repeated whitespace from transaction descriptors before tokenising. On txc-gbm-v2 it raised holdout-2025q2 macro-F1 from 0.78 to 0.81 (exp-104), mostly in Travel and Fuel. The rule list is versioned in the repo, so new suffixes are added by pull request rather than by the model, and it is part of the input to txc-gbm-v3.
Sources: memory/txn-categorization/feat-txc-normalise-v2.md

## Q8
exp-205 added the payment-to-minimum ratio (feat-ed-minpay-v2) to ed-gbm-v1 without the limit-change feature, lifting AUC from 0.781 to 0.803 on early-delinquency-holdout-2024q4 (Gini 0.606, KS 0.44). The gain has no leakage concern, since the feature uses posting dates and is known at the snapshot. It was recommended as the replacement for the limit-change feature, which was dropped.
Sources: memory/early-delinquency/exp-205.md, memory/early-delinquency/find-ed-minpay.md

## Q9
fsm-churn-xgb-v2 reads 41 store features: the 40 features of v1 with payment lag (feat-fsm-payment-lag-v2, UTC timestamps) and the util ratio taken from the store, plus feat-fsm-spend-cv-30d. It uses the same trees and hyperparameters as v1, and it reached holdout AUC 0.791 against 0.782 for v1.
Sources: memory/feature-store-migration/fsm-churn-xgb-v2.md, memory/feature-store-migration/feat-fsm-payment-lag-v2.md, memory/feature-store-migration/fsm-churn-xgb-v1.md

## Q10
The approval cutoff for application decisions on the v10 scale is 652, which matches the v8 cutoff of 640 at 58% approval. It was set by dec-bsm-cutover-2026q3 for the 2026-09-01 cutover, with bsm-app-gbm-v10b and bsm-cutoff-logit. The log entry of 2026-08-25 records the same cutoff.
Sources: memory/bureau-score-migration/dec-bsm-cutover-2026q3.md, memory/bureau-score-migration/bsm-cutoff-logit.md, memory/log/2026-08-25.md