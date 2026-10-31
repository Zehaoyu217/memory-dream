---
from: [q-xs-propensity]
updated: 2025-04-08
---
# `sav.offer_log` holds 1.42M eligible cardholder-wave rows, Jan 2025 to May 2026, open rate 2.9%
Built from `crm.contacts` and the offer engine. One row per eligible cardholder per offer wave; `opened` = savings account opened within 30 days.
Wave open rates run 2.4% to 3.5%. Eligibility: no savings account, card open over six months, no negative account status.
Owner: onboarding (Priya Nair). Source table `sav.offer_log`.
