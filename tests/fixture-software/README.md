# fixture-software: a coding project's memory (payments-api)

Thirty notes an agent working on a card-payment service would have written: components (`svc-`, `mod-`, `lib-`),
design records (`adr-`), a bug and its fix (`bug-`, `fix-`), releases (`rel-`), an incident, decisions, findings,
questions, a plan, a risk, a requirement, a metric, two preferences, one how-to and two log days. Three supersession
chains (the idempotency ADR v1 → v2 → v3, the capture decision, the retry library), a bug → fix → release chain by
`from:`, ownership and call/read/write sentences with backticked names, and numbers with their basis and date.

Questions: `eval/questions/software-payments-api.jsonl` (30: lookup, lineage, dependency, current, numeric, why).
Run on a copy, never here (`dream` writes the registries and `_dream/` into the root):

    cp -R tests/fixture-software/memory /tmp/w-soft && M="python3 skills/memory-dream/scripts/memory.py --root /tmp/w-soft"
    $M dream && $M check
    python3 eval/retrieval.py /tmp/w-soft eval/questions/software-payments-api.jsonl
    python3 eval/adversarial.py /tmp/w-soft eval/questions/software-payments-api.jsonl
