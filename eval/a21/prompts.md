# A21 prompts (as sent to the Opus subagents, `<W>` = the run's world directory)

## memory runs (`mem-N`: Haiku-indexed memory + skills/memory-dream/)

You are answering questions about a data-science team's past project work. Work only inside <W> — do
not read or search anything outside that directory.

The project memory is in <W>/memory/. How to use it is described in <W>/skills/memory-dream/SKILL.md
— read that first and follow its "Read" section (memory.py = python3
<W>/skills/memory-dream/scripts/memory.py --root <W>/memory). This is a read-only task: do not write or
edit notes and do not run `dream` or `log`.

Answer these 10 questions from the memory: (Q1–Q10 from questions.json)

Reply in exactly this format, nothing else:
## Q1
<answer in 1–4 sentences with the key numbers>
Sources: <note paths>
Tool calls for this question: <n>
## Q2
...

## grep baseline runs (`grep-N`: the same 30 notes only)

You are answering questions about a data-science team's past project work. Work only inside <W> — do
not read or search anything outside that directory.

The project notes are markdown files under <W>/memory/ (one note per question, experiment, finding,
decision, or dataset/feature/model description; the `# ` line states the point; frontmatter `from:`
names notes it built on and `supersedes:` names notes it overturns; log/ holds daily scratch lines).
Find what you need with grep, find, ls and cat via Bash, or with Read. This is a read-only task: do not
write or edit anything.

Answer these 10 questions from the notes: (same Q1–Q10, same reply format)
