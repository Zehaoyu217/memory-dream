---
from: [q-bt-who-accepts]
updated: 2025-03-03
---
# `bt.offer_log` holds 1.91M BT exposures from 2025-01-06 to 2026-06-30, acceptance 4.3%
Built by `bt_build_log.sql` from `offers.tier_matrix` joined to campaign sends. Four mail waves in 2025, two in 2026.
One row per account per wave; `accepted` = BT booked within 45 days of offer open.
Owner: retention (Maya Ortiz). Refreshed weekly.
Known gap: waves before 2025-04 have no tier code; it is filled from `offers.tier_matrix` at send date.
