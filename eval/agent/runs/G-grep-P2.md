## Q1
Chloe Martin reports campaign lift as a point estimate with its 95% confidence interval, for example "+1.8 pts (95% CI +0.6 to +3.0)". She never shows p-values in readouts, because business readers take "p = 0.04" as proof. Cost per response in $ goes in the same table as the lift. Under the team's general uplift rule (not one of Chloe's own notes), a CI that includes zero is labelled "no clear difference", and the interval comes from 500 account-level bootstrap resamples using the 95% percentile method.
Sources: memory/prefs/chloe-martin-campaign-readout.md, memory/reporting/significance-uplift-ci.md, memory/reporting/campaign-readout-template.md, memory/howto/bootstrap-ci-for-uplift.md
Tool calls for this question: 6
## Q2
She colours the winning campaign orange `#E07B24` and makes every other campaign mid-grey. She avoids brand blue because blue series were read as "baseline" in the Q3 2025 campaign readout. Maya Ortiz does the opposite and uses brand blue `#1F4E9A` for her focal cohort; each chart follows its owner's convention, and house style allows only one orange highlight per chart.
Sources: memory/prefs/chloe-martin-highlight-orange.md, memory/reporting/chart-style-colour.md, memory/prefs/maya-ortiz-focal-colour.md
Tool calls for this question: 5
## Q3
Since 2026-06-01, a PSI above 0.20 on any top-20 feature triggers a drift review for any `cli-` model. All other model families keep the 0.25 trigger, with 0.10 to 0.25 as "watch". The rule was tightened because `cli-glm-v2` drifted to PSI 0.22 on `cli_util_ratio` in 2026-04 and was not reviewed until the next cycle. This replaces the earlier rule of 0.25 for every model, and retraining is still a separate decision that needs an OOT performance check.
Sources: memory/reporting/monthly-review-psi-trigger-v2.md (supersedes memory/reporting/monthly-review-psi-trigger.md), memory/corrections/psi-two-tier-thresholds.md
Tool calls for this question: 6
## Q4
Default rates, PD and roll rates in risk tables are shown to 2 decimal places in percent, for example 3.84%. Retention, share and campaign-response percentages use only 1 decimal, for example 88.4%, and changes are written as "pts". Lena Fischer's risk packs follow the same rule for PD and default rates and also show Gini and KS to 2 decimals.
Sources: memory/reporting/rounding-percent.md, memory/prefs/lena-fischer-risk-rounding.md
Tool calls for this question: 4
## Q5
Each account's offer tier is assigned from the `offers.tier_matrix` table; it is the account's credit-line and pricing band. The tiers run A to E, and the correction confirms A is the highest (best promotional APRs) and E the lowest. On the retention side, the same table holds Maya Ortiz's offer grid of 10 churn-score deciles by 3 value bands: v3 has been in force since 2025-09-01, and v4 applies from the April 2026 cycle. Since 2026-10-08, the churn risk-tier cuts at 0.20 and 0.50 on churn-xgb-v2 scores are also written to it every night.
Sources: memory/glossary/tier.md, memory/corrections/tier-a-highest.md, memory/glossary/cli.md, memory/retention-offers-roi/ds-ror-tier-matrix.md, memory/retention-offers-roi/dec-ror-matrix-v4.md, memory/churn-2026/dec-risk-tiers.md
Tool calls for this question: 6
## Q6
Use the blended rate of 1.9%, so $100 of purchases earns $1.90. Do not use the old 2.5%, which was only the premium-card rate; standard cards sit around 1.6–1.8%. The Q4 2025 finance pack used 2.5% and was restated to 1.9%. In finance text, Ben Carter wants it called "interchange income", not "revenue".
Sources: memory/corrections/interchange-blended.md (supersedes memory/glossary/interchange.md), memory/prefs/ben-carter-interchange-wording.md
Tool calls for this question: 4
## Q7
No. OOT has to be a period after the training window that was never used for training, tuning or feature selection; the last months of the training data only count as in-time validation. For example, the fraud model's 0.88 AUC was in-time, and its true OOT AUC (2024-10 to 2024-12) was 0.84. The standard split is on `observation_date` with a six-month gap: train through 2024-12, leave 2025-01 to 2025-06 unused, and use 2025-07 to 2025-09 as OOT.
Sources: memory/corrections/oot-not-training-tail.md (supersedes memory/glossary/oot.md), memory/howto/oot-split-by-observation-date.md, memory/qa/retention-oot-window-2025.md
Tool calls for this question: 4
## Q8
Since 2025-11-01, DPD counts from the minimum payment due date rather than the statement close date. Day 1 is the day after the due date, and a payment posted on the due date still counts as current (0 DPD). The 2025-11 rule said day 1 was the due date itself, which was one day off; the `cards.payments_daily` pipeline was fixed on 2026-01-15. That fix shifts the Nov–Dec 2025 1-29 bucket counts by one day and leaves the 30+ buckets unchanged; 30+ means DPD of 30 or more.
Sources: memory/corrections/dpd-due-date-offbyone.md (supersedes memory/corrections/dpd-due-date.md, which superseded memory/glossary/dpd.md), memory/howto/dpd-bucket-labelling.md
Tool calls for this question: 4
## Q9
You don't report it as uplift: uplift is only reported when treatment and control are randomised holdouts. A difference taken from `marketing.campaign_responses` without randomisation is called "lift". For example, Chloe Martin's Oct 2025 CLI report showed a 1.8 pp "uplift" that was observational, and the randomised uplift was 0.9 pp. To get a real uplift, hold out a random 10% of the eligible list before sending (`arm = control`), with at least 3,000 accounts in each arm.
Sources: memory/corrections/uplift-randomised-only.md (supersedes memory/glossary/uplift.md), memory/howto/campaign-holdout-design.md, memory/howto/uplift-eval-qini-at-20pct.md
Tool calls for this question: 4
## Q10
`feat_disp_cnt_90d_v1` read data up to 14 days past the observation date, and the leak scan (`scripts/leak_scan.py`) flagged it. Once it was restricted to days on or before observation, holdout AUC fell from 0.79 to an honest 0.72. It was rebuilt as v2, which reads only those days, and v1 was removed from training. A separate case in complaint-classification: dispute link v1 (a count and a flag) was replaced by v2 in May 2026 because it counted disputes opened after the complaint, which turned a +0.14 macro-F1 gain into an honest +0.03.
Sources: memory/qa/dispute-feature-leak.md, memory/howto/leakage-check-post-period.md, memory/complaint-classification/fnd-cc-dispute-link-leak.md, memory/complaint-classification/feat-cc-dispute-link-v2.md
Tool calls for this question: 6
Total tool calls in this task: 22
Minutes spent: 4