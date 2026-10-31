---
from: [ds-ch-contact-costs]
updated: 2025-08-22
---
# feat-ch-send-window-v1 is the send-hour bucket of the SMS, from delivery timestamps
Buckets: morning 08-11, midday 11-14, afternoon 14-18, evening 18-21.
Source: SMS delivery timestamps. Calls use the same buckets from `callcenter.calls` attempt time.
