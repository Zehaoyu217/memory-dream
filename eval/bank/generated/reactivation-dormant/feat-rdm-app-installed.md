---
from: [ds-rdm-contact-channels]
updated: 2025-04-02
---
# feat-rdm-app-installed: app installed and push-capable flag
- Two binary fields: app installed (from `app.sessions_daily` device table) and push-capable (installed plus notifications on).
- Used in rdm-propensity-lr, rdm-uplift-v1 and rdm-uplift-v2.
- Keeps the app-installed group distinguishable from SMS and email reach.
