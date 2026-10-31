---
from: []
updated: 2025-02-12
---
# callcenter.calls outcomes give a promise-to-pay label within 14 days for early-collections contacts
Label is 1 when a `callcenter.calls` row with outcome PTP (promise to pay) or PAID exists within 14 days after the contact, else 0. Built by joining `callcenter.calls` to `cards.payments_daily`.
Base rate on 2025 Jan-Feb contacts: 18.6% positive (n=52,310 contacts).
Calls and SMS both feed the label. Email is excluded because replies are not logged to `callcenter.calls`.
The label is per contact, not per account, so an account contacted twice appears twice.
