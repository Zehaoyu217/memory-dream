#!/usr/bin/env python3
"""Deterministic stand-in for the dreamer model, for the churn-2026 fixture.

Prompt on stdin, JSON on stdout, like `claude -p`. Answers extraction and review prompts
from a hand-written oracle. Knobs (env):
  FAKE_LOG     append one line per call: "<kind> <note path or ->"
  FAKE_INJECT  JSON file {note stem: raw answer text} returned verbatim instead of the oracle
  FAKE_REVIEW  JSON file {"types": {...}, "entities": {...}, "conflicts": {...}, "etypes": {...}, "kinds": {...},
               "tags": {...}} overriding review answers (every word not named is answered "label")
  FAKE_EXTRA   JSON file {note stem: {field: value}} merged into that note's reading (tags, a kind word)
  FAKE_SAVE    directory: save every prompt there (NNN-<kind>.txt)
  FAKE_CURATE  JSON file with the curator's `same` list, returned in place of the oracle's
  FAKE_SKIP    packets only: note stems, comma-separated, whose line is left out of the answer
  FAKE_CUT     packets only: the answer's last line is cut in half, as an answer that ran out of room is

A packet (`dream --packets`, many notes in one prompt) is answered with one line of JSON per note.
"""
import json
import os
import re
import sys

GLOBAL = {  # surface → (id, type); matched case-insensitively on word boundaries
    "cards.txn_daily": ("cards.txn_daily", "dataset"),
    "cards.churn_labels": ("cards.churn_labels", "dataset"),
    "cards.churn_scores": ("cards.churn_scores", "dataset"),
    "holdout-2025q4": ("holdout-2025q4", "dataset"),
    "offers.tier_matrix": ("offers.tier_matrix", "dataset"),
    "recall@10": ("recall-at-10", "metric"),
    "AUC": ("auc", "metric"),
    "feat-velocity-v2": ("feat-velocity-v2", "feature"),
    "velocity v2": ("feat-velocity-v2", "feature"),
    "feat-velocity-v3": ("feat-velocity-v3", "feature"),
    "feat-utilization-v1": ("feat-utilization-v1", "feature"),
    "utilization features": ("feat-utilization-v1", "feature"),
    "logreg-baseline": ("logreg-baseline", "model"),
    "churn-xgb-v2": ("churn-xgb-v2", "model"),
    "churn-xgb-v3": ("churn-xgb-v3", "model"),
    "XGBoost": ("xgboost", "tool"),
    "risk-tier cuts": ("risk-tier-cuts", "concept"),
    "risk tier cutoffs": ("risk-tier-cutoffs", "concept"),
    "new accounts": ("new-accounts", "segment"),
    "data-eng-cards": ("data-eng-cards", "other"),
    "Maya Ortiz": ("maya-ortiz", "person"),
    "Priya Nair": ("priya-nair", "person"),
    "Sam Lee": ("sam-lee", "person"),
}
V2 = ("feat-velocity-v2", "feature", ["velocity features"])
NOTE = {  # stem → kind, extra entities, excluded global ids, relations (s, type, o, quote[, def]), refs
    "q-churn-drivers": {"kind": "question"},
    "ds-txn-2025q4": {"kind": "dataset", "rel": [("cards.txn_daily", "owned-by", "data-eng-cards", "Owned by data-eng-cards")]},
    "ds-churn-labels": {"kind": "dataset", "rel": [
        ("cards.churn_labels", "built-on", "cards.txn_daily", "Built by the retention-labels job from `cards.txn_daily`"),
        ("cards.churn_labels", "maintained-by", "data-eng-cards", "maintained by data-eng-cards")]},
    "ds-holdout-2025q4": {"kind": "dataset"},
    "metric-recall-at-10": {"kind": "metric"},
    "feat-velocity-v2": {"kind": "feature", "rel": [("feat-velocity-v2", "built-on", "cards.txn_daily", "Built on `cards.txn_daily`")]},
    "feat-utilization-v1": {"kind": "feature", "extra": [("feat-utilization-v1", "feature", ["Credit utilization features"])],
                            "rel": [("feat-utilization-v1", "uses", "cards.txn_daily",
                                     "feat-utilization-v1 uses `balance` and `credit_limit` from `cards.txn_daily`")]},
    "exp-011-baseline": {"kind": "experiment", "rel": [
        ("logreg-baseline", "learned-from", "cards.churn_labels", "logreg-baseline, fit on `cards.churn_labels`"),
        ("logreg-baseline", "evaluated-on", "holdout-2025q4", "AUC 0.71, recall@10 0.29 on holdout-2025q4")]},
    "exp-014": {"kind": "experiment", "extra": [V2]},
    "churn-xgb-v2": {"kind": "model", "rel": [
        ("churn-xgb-v2", "uses", "feat-velocity-v2", "churn-xgb-v2 uses feat-velocity-v2"),
        ("churn-xgb-v2", "uses", "feat-utilization-v1", "feat-velocity-v2 and feat-utilization-v1"),
        ("churn-xgb-v2", "learned-from", "cards.churn_labels", "fit on `cards.churn_labels`"),
        ("churn-xgb-v2", "evaluated-on", "holdout-2025q4", "Evaluated on holdout-2025q4"),
        ("churn-xgb-v2", "writes", "cards.churn_scores", "Scores written nightly to `cards.churn_scores`")]},
    "q-tier-cutoffs": {"kind": "question"},
    "dec-risk-tiers": {"kind": "decision", "rel": [
        ("risk-tier-cuts", "uses", "churn-xgb-v2", "The risk-tier cuts are applied to churn-xgb-v2 scores"),
        ("risk-tier-cuts", "writes", "offers.tier_matrix", "written to `offers.tier_matrix` each night")]},
    "exp-015-tenure": {"kind": "experiment", "rel": [("churn-xgb-v2", "tested-on", "new-accounts", "AUC 0.69 on new accounts")]},
    "finding-new-accounts": {"kind": "finding"},
    "leak-hypothesis": {"kind": "question", "extra": [V2],
                        "rel": [("feat-velocity-v2", "related-to", "auc", "The velocity features use a window")]},
    "exp-017-leak-check": {"kind": "experiment", "refs": ["exp-014"]},
    "post-period-leak": {"kind": "finding", "extra": [V2], "summary":
                         "Post-period aggregation in velocity features leaks the target; AUC 0.81→0.74 without it on holdout-2025q4.",
                         "rel": [("feat-velocity-v2", "built-on", "cards.txn_daily", "velocity features built on `cards.txn_daily`")]},
    "feat-utilization-check": {"kind": "finding"},
    "dec-velocity-v3": {"kind": "decision", "extra": [("feat-velocity-v3", "feature", ["velocity features"])], "rel": [("feat-velocity-v3", "owned-by", "sam-lee", "Owner: Sam Lee")]},
    "feat-velocity-v3": {"kind": "feature", "rel": [
        ("feat-velocity-v3", "uses", "cards.txn_daily", "Reads `cards.txn_daily`"),
        ("feat-velocity-v3", "replaces", "feat-velocity-v2", "replaces feat-velocity-v2")]},
    "churn-xgb-v3": {"kind": "model", "rel": [
        ("churn-xgb-v3", "uses", "feat-velocity-v3", "churn-xgb-v3 uses feat-velocity-v3"),
        ("churn-xgb-v3", "uses", "feat-utilization-v1", "feat-velocity-v3 and feat-utilization-v1"),
        ("churn-xgb-v3", "learned-from", "cards.churn_labels", "Trained on `cards.churn_labels`"),
        ("churn-xgb-v3", "evaluated-on", "holdout-2025q4", "Evaluated on holdout-2025q4"),
        ("churn-xgb-v3", "replaces", "churn-xgb-v2", "replaces churn-xgb-v2")]},
    "exp-019-recall": {"kind": "experiment", "rel": [("churn-xgb-v3", "evaluated-on", "holdout-2025q4", "Re-scored holdout-2025q4")]},
    "txn-backfill": {"kind": "note", "exclude": ["cards.txn_daily"],
                     "extra": [("txn-table", "dataset", ["txn table", "cards.txn_daily"]), V2],
                     "rel": [("txn-table", "feeds", "feat-velocity-v2", "The txn table feeds the velocity features")]},
    "dec-retrain-cadence": {"kind": "decision", "refs": ["q-recalibrate-tiers"], "rel": [
        ("churn-xgb-v3", "learned-from", "cards.churn_labels", "Monthly retrain on the latest 9 observation months of")]},
    "q-recalibrate-tiers": {"kind": "question"},
}
REVIEW_TYPES = {"learned-from": "alias trained-on"}
SAME = {frozenset(("risk-tier-cuts", "risk-tier-cutoffs"))}


def occurs(surface, text):
    return re.search(r"(?<![\w-])" + re.escape(surface) + r"(?![\w-])", text, re.I)


def extraction(path, text):
    stem = path.rsplit("/", 1)[-1][:-3]
    o = NOTE.get(stem, {"kind": "log" if path.startswith("log/") else "note"})
    ents = {}
    for surface, (eid, etype) in GLOBAL.items():
        if eid not in o.get("exclude", []) and occurs(surface, text):
            ents.setdefault(eid, {"id": eid, "type": etype, "as": []})["as"].append(surface)
    for eid, etype, surfaces in o.get("extra", []):
        ents.setdefault(eid, {"id": eid, "type": etype, "as": []})["as"] += surfaces
    title = next((ln[2:] for ln in text.split("\n") if ln.startswith("# ")), stem)
    rels = []
    for r in o.get("rel", []):
        d = {"s": r[0], "type": r[1], "o": r[2], "quote": r[3]}
        if len(r) > 4:
            d["def"] = r[4]
        rels.append(d)
    ans = {"kind": o["kind"], "summary": o.get("summary", title), "entities": list(ents.values()),
           "relations": rels, "refs": o.get("refs", [])}
    extra = json.load(open(os.environ["FAKE_EXTRA"])) if os.environ.get("FAKE_EXTRA") else {}
    ans.update(extra.get(stem, {}))  # FAKE_EXTRA {stem: {"tags": [...], "kind": "other: …"}}: what a test wants read
    return ans


def review(prompt):
    over = json.load(open(os.environ["FAKE_REVIEW"])) if os.environ.get("FAKE_REVIEW") else {}
    sec = prompt.split("LABELS the indexer used", 1)[1].split("ENTITY PAIRS", 1)
    pairs_sec, conf_sec = (sec[1].split("LIVE NOTES", 1) + [""])[:2]
    types = {m: REVIEW_TYPES.get(m, "label") for m in re.findall(r"^- ([\w.-]+): ", sec[0], re.M)}
    ents = {}
    for a, b in re.findall(r"^- (\S+) / (\S+):", pairs_sec, re.M):
        ents[f"{a} / {b}"] = "same" if frozenset((a, b)) in SAME else "different"
    conf_only = conf_sec.split("THING TYPES", 1)[0]
    conflicts = {f"{a} / {b}": "unsure" for a, b in re.findall(r"^- (\S+) / (\S+):", conf_only, re.M)}
    words_sec = (prompt.split("TYPE WORDS the indexer used", 1) + [""])[1].split("NOTE KINDS", 1)[0].split("Reply with JSON", 1)[0]
    etypes = {m: "label" for m in re.findall(r"^- ([\w.-]+): ", words_sec, re.M)}
    kinds_sec = (prompt.split("KIND WORDS the indexer gave", 1) + [""])[1].split("TAGS, themes", 1)[0]
    kinds = {m: "label" for m in re.findall(r"^- ([\w.-]+): ", kinds_sec, re.M)}
    tags_sec = (prompt.split("TAG WORDS that notes", 1) + [""])[1].split("Reply with JSON", 1)[0]
    tags = {m: "label" for m in re.findall(r"^- ([\w.-]+): ", tags_sec, re.M)}
    types.update(over.get("types", {}))
    ents.update(over.get("entities", {}))
    conflicts.update(over.get("conflicts", {}))
    etypes.update(over.get("etypes", {}))
    kinds.update(over.get("kinds", {}))
    tags.update(over.get("tags", {}))
    return {"types": types, "entities": ents, "conflicts": conflicts, "etypes": etypes, "kinds": kinds, "tags": tags}


def main():
    prompt = sys.stdin.read()
    if prompt.startswith("Index this memory note"):
        m = re.search(r"^NOTE (\S+):\n", prompt, re.M)
        path, text = m.group(1), prompt[m.end():]
        kind, stem = "extract", path.rsplit("/", 1)[-1][:-3]
        inject = json.load(open(os.environ["FAKE_INJECT"])) if os.environ.get("FAKE_INJECT") else {}
        out = inject[stem] if stem in inject else json.dumps(extraction(path, text))
    elif prompt.startswith("Index each memory note"):
        parts = re.split(r"^NOTE ([0-9a-f]{12}) (\S+):\n", prompt, flags=re.M)  # rules, then (id, path, text) per note
        skip = set(filter(None, os.environ.get("FAKE_SKIP", "").split(",")))
        lines = [json.dumps({"note": parts[i], **extraction(parts[i + 1], parts[i + 2])}) for i in range(1, len(parts), 3)
                 if parts[i + 1].rsplit("/", 1)[-1][:-3] not in skip]
        if os.environ.get("FAKE_CUT") and lines:
            lines[-1] = lines[-1][:len(lines[-1]) // 2]
        kind, path, out = "packet", str((len(parts) - 1) // 3), "\n".join(lines)
    elif prompt.startswith("Notes of a work memory say in their own words"):
        # the second reading: every member of each line, with its own words; the note is the one of the folder whose
        # file name the words have, or whose first line shares two words of four letters with them
        folder = dict(re.findall(r"^(\S+): (.*)$", prompt.split("\nFOLDER", 1)[1].split("\nLINES", 1)[0], re.M))
        ans = {}
        for num, verb, text in re.findall(r"^(\d+) · \S+ · (builds on|replaces) · (.*)$", prompt.split("\nLINES", 1)[1], re.M):
            ans[num] = []
            for part in re.findall(r"(?i)\b" + verb + r"\s+(.+?)(?:\.(?:\s|$)|$)", text):
                for words in re.split(r",\s+|\s+and\s+", part):
                    words = words.strip()
                    said = set(re.findall(r"[a-z]{4,}", words.lower()))
                    exact = [f for f in folder if re.search(r"(?<![\w-])" + re.escape(f) + r"(?![\w-])", words)]
                    best = max(folder, key=lambda f: (len(said & set(re.findall(r"[a-z]{4,}", folder[f].lower()))), f), default=None)
                    hit = best and len(said & set(re.findall(r"[a-z]{4,}", folder[best].lower()))) >= 2
                    if words:
                        ans[num].append({"words": words, "note": exact[0] if exact else best if hit else None})
        kind, path, out = "place", "-", json.dumps(ans)
    elif prompt.startswith("A note of a work memory says, in a line of its own"):
        # the third reading: the candidate whose name and first lines share two words of four letters with the item's words
        ans = {}
        for block in re.split(r"\n(?=\d+ · )", prompt.split("ITEMS:\n", 1)[1].split("\nReply with JSON", 1)[0]):
            m = re.match(r"(\d+) · \S+ (?:builds on|replaces) «(.*?)»", block)
            if not m:
                continue
            said = set(re.findall(r"[a-z]{4,}", m.group(2).lower()))
            best = None
            for c in re.findall(r"^   - (\S+): (.*)$", block, re.M):
                if len(said & set(re.findall(r"[a-z]{4,}", c[1].lower()))) >= 2:
                    best = best or c[0]
            ans[m.group(1)] = best
        kind, path, out = "choose", "-", json.dumps(ans)
    elif prompt.startswith("You keep the names of things"):
        ids = set(re.findall(r"^- (\S+) \(", prompt, re.M))
        over = json.load(open(os.environ["FAKE_CURATE"])) if os.environ.get("FAKE_CURATE") else None
        same = over if over is not None else [{"ids": sorted(p), "why": "the notes use both for the cut-offs between risk tiers"}
                                              for p in SAME if p <= ids]
        kind, path, out = "curate", "-", json.dumps({"same": same})
    elif prompt.startswith("You keep the vocabulary"):
        kind, path, out = "review", "-", json.dumps(review(prompt))
    else:
        kind, path, out = "other", "-", "{}"
    if os.environ.get("FAKE_SAVE"):
        d = os.environ["FAKE_SAVE"]
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, f"{len(os.listdir(d)):04d}-{kind}.txt"), "w") as f:
            f.write(prompt)
    if os.environ.get("FAKE_LOG"):
        with open(os.environ["FAKE_LOG"], "a") as f:
            f.write(f"{kind} {path}\n")
    print(out)


if __name__ == "__main__":
    main()
