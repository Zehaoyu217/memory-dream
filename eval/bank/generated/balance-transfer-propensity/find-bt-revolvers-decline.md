---
from: [feat-bt-revolve-share, bt-xgb-v2]
updated: 2025-10-06
---
# Finding: revolvers accept balance transfers at 6.8%, the rest at 1.2%
On bt-holdout-2025q1 (n=41,800), accounts with revolve share at or above 0.5 accept at 6.8%. The rest accept at 1.2%.
Revolvers are the BT market; transactors rarely take a transfer. The mailer rules already skip most transactors, so this mainly confirms the revolve feature.
Source: `bt.offer_log` joined to feat-bt-revolve-share.
