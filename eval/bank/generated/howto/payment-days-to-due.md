---
updated: 2025-10-07
---
# Days to due is measured from the last payment date to the statement due date
Feature `feat_pay_days_to_due_last_v1` equals the statement due date minus the date of the last payment in `cards.payments_daily` before observation. Negative values mean the payment came after the due date. Values are capped at -30 and 60.
Priya Nair's onboarding team owns the feature. Measuring from the statement close date instead cost 0.01 AUC on the onboarding model.
