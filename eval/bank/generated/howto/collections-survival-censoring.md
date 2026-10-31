---
updated: 2025-09-16
---
# Collections roll models censor cases that close in full, rather than dropping them
In `collections.cases`, a case that closes with payment in full is a censored observation at its close date, not a non-roll. Dropping these cases biased 60-day roll rates upward by about 3 points in the 2025 H1 analysis.
Use a Kaplan-Meier or discrete-time hazard fit with censoring at close. Raj Patel reads roll rate per 100 open cases.
