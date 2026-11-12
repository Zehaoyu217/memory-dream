# The headless arms of RESULTS phase S

What the agents answered, one file a batch of ten questions (`<arm>-<model>-r<run>-b<batch>.md`), and what each
batch cost (`usage.jsonl`, the CLI's own figures). The questions are `eval/questions/linkage-100.jsonl`. To print a
row of the table in RESULTS S6 again, with no model:

    python3 eval/agent/run_headless.py table eval/questions/linkage-100.jsonl eval/agent/headless/<folder>

| folder | base and memory | arms |
|---|---|---|
| `tidy` | the tidy bank, its links on frontmatter | grep and memory, Haiku 5.5, one run |
| `worn-first-reading` | the worn bank; the memory as the keepers first read it | grep and memory, Haiku 5.5, three runs |
| `worn-first-reading-opus` | the same | grep (two runs) and memory (one), Opus 5.5 |
| `worn-items-asked-again` | the items no note answered to put to a keeper once more | memory, Haiku 5.5, three runs |
| `worn-ask-prints-what-is-not-placed` | the same memory, `ask` printing the words it could not place | memory, Haiku 5.5, three runs |
| `worn-lines-read-twice` | every line that states lineage read a second time (`eval/real/worn-index`) | memory, Haiku 5.5, three runs |
| `worn-lines-read-twice-opus` | the same | memory, Opus 5.5, one run |

Paths of the machine the arms ran on are written `<workspace>` and `<path>`. The tool calls themselves are not kept
here; `outside` in a row of `usage.jsonl` is how many of them named a path outside the arm's workspace. The one in
`worn-first-reading` is the CLI's own file of that session's tool output, which the agent opened to read it whole.

To run an arm: `run_headless.py prepare <dreamed memory> <arms dir>`, then `run <grep|memory> <haiku|opus> <arms dir>
<questions> <out> --runs 3`, then `table <questions> <out>`.
