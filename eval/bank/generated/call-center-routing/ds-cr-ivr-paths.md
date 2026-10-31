---
from: [ds-cr-calls]
updated: 2025-12-03
---
# `callcenter.ivr_menu_paths` has one row per IVR menu selection, from 2025-03-01
Owner Tomás Rivera (data engineering). The table starts on 2025-03-01, when the IVR vendor changed; earlier menu events use a different format and are excluded.
About 2.9M rows covering 2025-03-01 to 2025-11-30. 96 percent of calls have at least one menu event.
Fields: call_id, menu_level (1 to 6), selection_key, event_ts.
Calls with no menu event (4 percent) get the token NONE in the path feature.
