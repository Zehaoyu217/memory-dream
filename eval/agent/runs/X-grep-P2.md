## Q1
Chloe Martin reports campaign lift as a point estimate with its 95% confidence interval, for example "+1.8 pts (95% CI +0.6 to +3.0)". She never shows p-values, because business readers take "p = 0.04" as proof. Cost per response in $ goes in the same table as the lift. Under the deck rule, an uplift whose CI includes zero is labelled "no clear difference", not "not significant". The intervals come from 500 account-level bootstrap resamples within each arm, using the 95% percentile method.
Sources: memory/prefs/chloe-martin-campaign-readout.md, memory/reporting/significance-uplift-ci.md, memory/reporting/campaign-readout-template.md, memory/howto/bootstrap-ci-for-uplift.md
## Q2
She colours the winning campaign orange `#E07B24` and makes every other campaign mid-grey. She avoids brand blue as a highlight because blue series were read as "baseline" in the Q3 2025 campaign readout. Maya Ortiz does the opposite and uses brand blue `#1F4E9A` for her focal cohort; each chart follows its owner's convention. The house rule allows only one orange highlight per chart.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/reporting/chart-style-colour.md, memory/prefs/maya-ortiz-focal-colour.md
## Q3
Since 2026-06-01, a PSI above 0.20 on any top-20 feature of a `cli-` model triggers a drift review. All other model families keep the 0.25 trigger, with 0.10 to 0.25 as "watch". The change followed `cli-glm-v2` drifting to PSI 0.22 on `cli_util_ratio` in 2026-04 and going unreviewed until the next cycle. This supersedes the earlier rule of 0.25 for every model.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md, memory/reporting/monthly-review-psi-trigger.md
## Q4
Default rates, PD and roll rates in risk tables use 2 decimals in percent, for example 3.84%. General percentages such as retention, share and campaign response use 1 decimal, for example 88.4%. Lena Fischer's risk packs follow the same rule and also show Gini and KS to 2 decimals.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md
## Q5
Offer tiers are the credit-line and pricing band assigned to each account from the `offers.tier_matrix` table. They run A to E, and a 2025-05-19 correction confirms A is the highest tier, with the best promotional APRs. Retention (Maya Ortiz) owns the matrix: v3 is a grid of 10 churn deciles by 3 value bands. The churn risk-tier cuts on churn-xgb-v2 scores (0.50 or more means call, 0.20 to 0.50 means email) are written to the table every night.
Sources: memory/glossary/tier.md, memory/corrections/tier-a-highest.md, memory/retention-offers-roi/ds-ror-tier-matrix.md, memory/churn-2026/dec-risk-tiers.md, memory/glossary/cli.md
## Q6
Use the blended rate of 1.9%, so $100 of purchases earns $1.90. The old 2.5% figure was the premium-card rate only; standard cards sit around 1.6–1.8%. The Q4 2025 finance pack used 2.5% and was restated to 1.9%. In finance text, call it "interchange income", not "revenue".
Sources: memory/corrections/interchange-blended.md, memory/glossary/interchange.md, memory/prefs/ben-carter-interchange-wording.md
## Q7
No. OOT must be a period after the training window that was never used for training, tuning or feature selection; the last months of the training data are in-time validation. The correction (2025-07-15) found the fraud model's 0.88 AUC was in-time, and its true OOT AUC for 2024-10 to 2024-12 was 0.84. The current split is on `observation_date`, with a six-month unused gap before a three-month OOT window. For example, train through 2024-12, gap 2025-01 to 2025-06, OOT 2025-07 to 2025-09.
Sources: memory/corrections/oot-not-training-tail.md, memory/glossary/oot.md, memory/howto/oot-split-by-observation-date.md, memory/qa/retention-oot-window-2025.md
## Q8
DPD counts from the minimum payment due date, not the statement close date (changed 2025-11-01). Day 1 is the day after the due date, so a payment posted on the due date still counts as current (0 DPD). The 2025-11 rule had made the due date itself day 1, which was off by one; `cards.payments_daily` was fixed on 2026-01-15. That shifted the Nov–Dec 2025 1-29 bucket counts by one day, and the 30+ buckets did not change.
Sources: memory/corrections/dpd-due-date-offbyone.md, memory/corrections/dpd-due-date.md, memory/glossary/dpd.md
## Q9
Don't call it uplift. Uplift is reported only when treatment and control are randomised holdouts; observational differences from `marketing.campaign_responses` are reported as "lift". The rule came from Chloe Martin's Oct 2025 CLI report, whose 1.8 pp "uplift" was observational; the randomised uplift was 0.9 pp. A proper holdout is 10% of the eligible list drawn at random before send, with at least 3,000 accounts per arm.
Sources: memory/corrections/uplift-randomised-only.md, memory/glossary/uplift.md, memory/howto/campaign-holdout-design.md
## Q10
The leak scan flagged `feat_disp_cnt_90d_v1` because it read 14 days past the observation date. That leak inflated holdout AUC: 0.79 with the leak against 0.72 when restricted to days on or before observation. The feature was rebuilt as v2, which reads only data on or before observation, and v1 was removed from training.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md