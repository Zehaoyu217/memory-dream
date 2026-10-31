---
from: [exp-405, aml-find-ranker-top40]
supersedes: [aml-find-ranker-top40]
updated: 2026-05-15
---
# On fresh labels the top-40% capture is 93.5%; 96% needs the top 55%
Fresh Jan-Mar 2026 labels (aml-oot-2026h1, n=9,870, 188 SARs): aml-xgb-v2 captures 93.5% in the top 40%.
Reaching 96% needs the top 55% of the queue, which is too deep to be useful.
Supersedes the 98.2% in-sample figure; v3 recalibration followed (exp-407).
