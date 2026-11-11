## Q1
feat-rs-region-rate is a target-encoded recovery rate by postcode region. It lifted rs-xgb-v1 Gini from 0.41 to 0.44 on recovery-scoring-holdout-2023h2 (exp-303), but exp-304 showed a 2.9x recovery spread across region deciles at equal balance and payment history, so it was treated as a neighbourhood-demographics proxy and dropped from all recovery-scoring models on 2025-05-22 (dec-rs-drop-region).
Sources: memory/recovery-scoring/feat-rs-region-rate.md, memory/recovery-scoring/exp-303.md, memory/recovery-scoring/exp-304.md, memory/recovery-scoring/find-rs-region-proxy.md, memory/recovery-scoring/dec-rs-drop-region.md

## Q2
exp-403-callcentre-naive found that a call in the prior 90 days looked like +1.8 points of open rate (4.9% vs 3.1%). After matching on propensity and tenure the effect fell to +0.6 points, not significant, so the naive effect was mostly selection (find-xs-call-overstated). A causal forest (xs-call-uplift-v1, exp-406) then found +1.2 points in deciles 1-2, and call-centre outreach was restricted to those deciles (dec-xs-call-low-deciles, 2025-11-10).
Sources: memory/cross-sell-savings/exp-403-callcentre-naive.md, memory/cross-sell-savings/find-xs-call-overstated.md, memory/cross-sell-savings/xs-call-uplift-v1.md, memory/cross-sell-savings/dec-xs-call-low-deciles.md, memory/cross-sell-savings/exp-406-call-uplift.md

## Q3
sfc-hier-v3 is built on feat-sfc-active-accounts (active account count per segment, used as a regressor), on the MinT reconciliation from exp-207 and fnd-sfc-q4-reconciled (Q4 bias -0.4%), and on feat-sfc-cpi-lag6 (six-month lag of year-on-year CPI). It supersedes sfc-lgbm-v2, which it was built to replace. Its note also lists sfc-oot-2025h2 as its evaluation set and total MAPE 2.3%.
Sources: memory/spend-forecasting/sfc-hier-v3.md, memory/spend-forecasting/feat-sfc-active-accounts.md, memory/spend-forecasting/exp-207.md, memory/spend-forecasting/fnd-sfc-q4-reconciled.md, memory/spend-forecasting/feat-sfc-cpi-lag6.md

## Q4
The current fraud-2026 model is fraud26-gbm-v3, promoted on 2026-08-26 with an alert threshold of 0.66 and no travel-specific uplift. At 0.66 the candidate gave a 0.6% alert rate and 21.5% precision (exp-208). It replaced v2, which ran at 0.62.
Sources: memory/fraud-2026/dec-f26-promote-v3.md, memory/fraud-2026/exp-208.md, memory/fraud-2026/fraud26-gbm-v3.md, memory/fraud-2026/dec-f26-promote-v2.md

## Q5
mrisk-gbm-v2 reached AUC 0.86 and precision@100 0.43 on mrisk-oot-2026h1 (exp-505, 2026-07-06). It has since been superseded by mrisk-gbm-v3, which scores AUC 0.91 and precision@100 0.58 on the same holdout (exp-507).
Sources: memory/merchant-risk/exp-505.md, memory/merchant-risk/mrisk-gbm-v2.md, memory/merchant-risk/exp-507.md

## Q6
The v3 scorecard's Gini fell from 0.41 to 0.33 on the 2026-Q1 holdout (n=18,900) as bureau scores drifted (find-app-gini-v3-drift). The rebuild as v4 (dec-app-rebuild-v4, 2026-06-26) keeps the explainable points-based form and adds v10 bureau bands, an income estimate and reject-inference weights from app-gbm-v2. On the out-of-time set v4 scored Gini 0.42 against 0.35 for v3 (exp-507).
Sources: memory/application-scorecard/dec-app-rebuild-v4.md, memory/application-scorecard/find-app-gini-v3-drift.md, memory/application-scorecard/app-scorecard-v4.md, memory/application-scorecard/exp-507.md

## Q7
feat-txc-normalise-v2 strips store numbers, hash codes and city suffixes from transaction descriptors; the rule list is versioned in the repo, and new suffixes are added by pull request. Adding it to txc-gbm-v2 lifted macro-F1 from 0.78 to 0.81 on holdout-2025q2 (exp-104, n=2,000). It is an input to txc-gbm-v3, the current model at macro-F1 0.83 on txc-oot-2026h1, shipped on 2026-03-10.
Sources: memory/txn-categorization/feat-txc-normalise-v2.md, memory/txn-categorization/exp-104.md, memory/txn-categorization/txc-gbm-v3.md, memory/txn-categorization/dec-txc-ship-gbm-v3.md

## Q8
exp-205 added the 6-month payment-to-minimum ratio (feat-ed-minpay-v2) to ed-gbm-v1 and dropped the limit-change feature. AUC rose from 0.781 to 0.803 on early-delinquency-holdout-2024q4 (n=402,000), with no leakage. The result went into ed-gbm-v2 (2025-09-10), which was later superseded by ed-gbm-v3 (AUC 0.809 on early-delinquency-oot-2026h1).
Sources: memory/early-delinquency/exp-205.md, memory/early-delinquency/find-ed-minpay.md, memory/early-delinquency/ed-gbm-v2.md, memory/early-delinquency/feat-ed-minpay-v2.md

## Q9
fsm-churn-xgb-v2 reads 41 store features: v1's 40 features, with feat-fsm-payment-lag-v2 (UTC timestamps) and feat-fsm-util-ratio (balance over limit at month-end) taken from the feature store, plus feat-fsm-spend-cv-30d. It reached holdout AUC 0.791 against 0.782 for v1 (exp-105, holdout-2025q2).
Sources: memory/feature-store-migration/fsm-churn-xgb-v2.md, memory/feature-store-migration/exp-105.md, memory/feature-store-migration/feat-fsm-payment-lag-v2.md, memory/feature-store-migration/feat-fsm-util-ratio.md, memory/feature-store-migration/feat-fsm-spend-cv-30d.md

## Q10
The current approval cutoff on the v10 scale is 652, in force from 2026-09-01 (dec-bsm-cutover-2026q3). It replaces the v8 cutoff of 640 and holds the 58% approval rate with a 4.1% bad rate (exp-305). The cutover uses bsm-app-gbm-v10b and bsm-cutoff-logit, with the v8 fallback kept.
Sources: memory/bureau-score-migration/dec-bsm-cutover-2026q3.md, memory/bureau-score-migration/exp-305.md, memory/bureau-score-migration/bsm-cutoff-logit.md