---
from: [ds-rs-chargeoff-base]
updated: 2025-08-11
---
# feat-rs-contact-attempts counts in-house contact attempts in the 60 days before placement, from callcenter.calls
Features: count of calls and SMS attempts in 60 days before placement, days since last successful contact, and a flag for no successful contact.
Source: `callcenter.calls` and the SMS delivery log.
Accounts with at least one successful contact recover at about 1.3 times the rate of those with none.
