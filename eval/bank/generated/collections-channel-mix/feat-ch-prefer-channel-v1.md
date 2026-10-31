---
from: [ds-ch-contact-costs]
updated: 2025-08-20
---
# feat-ch-prefer-channel-v1 is the channel that produced a promise-to-pay or payment after a prior contact
Feature: the channel (SMS or call) that produced a PTP or payment within 14 days of a previous contact, or null if none.
Source: `callcenter.calls` and the SMS delivery log.
Accounts with a prior responsive channel are the ones where channel choice matters most.
