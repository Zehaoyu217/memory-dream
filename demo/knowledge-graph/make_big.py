#!/usr/bin/env python3
"""A large graph to test the knowledge-graph page at scale, shaped like a big memory: projects of very different sizes,
a shared middle, ten families of things, links mostly inside a project with a few hubs, and some between projects.
Each node carries tags of every sort: categories (type, a path of family and kind with a long tail of kinds,
dataset/table, feature/window, …; team, one or two of fourteen, a list when two; status), a time (created), a number
for datasets and features (rows) and a text (definition, a sentence of its own). Each link carries tags too: status
(confirmed or proposed) and source_system (categories), observed (a time) and weight (a number); one in twenty is
related-to, a link with no direction.

  python3 demo/knowledge-graph/make_big.py out.json [--things 20000] [--links 45000] [--seed 7] [--no-groups]

Writes {"nodes": [...], "links": [...]} for skills/memory-dream/scripts/graph_page.py. Deterministic for a seed. --no-groups leaves
the nodes without a project, so the page must find its islands in the links (the communities path).
"""
import json
import random
import sys

FAMILIES = [("dataset", 18), ("feature", 17), ("model", 13), ("metric", 8), ("document", 9), ("decision", 8),
            ("term", 6), ("person", 5), ("team", 3), ("system", 13)]
EDGES = ["uses", "uses", "uses", "measured-by", "evaluated-on", "produces", "part-of", "owned-by", "replaces", "trained-on"]
KINDS = {"dataset": ["table", "view", "extract", "segment", "snapshot", "stream"], "feature": ["raw", "derived", "ratio", "flag", "window", "embedding"],
         "model": ["gbm", "logistic", "scorecard", "nn", "rules", "uplift"], "metric": ["kpi", "rate", "loss", "count"],
         "document": ["memo", "deck", "runbook", "spec", "dashboard"], "decision": ["policy", "threshold", "launch"],
         "term": ["definition", "acronym"], "person": ["analyst", "engineer", "owner"], "team": ["squad", "vendor"],
         "system": ["pipeline", "service", "job", "api", "repo", "cluster"]}
WHAT = {"dataset": "A table of {t} records", "feature": "A {t} signal built from account history", "model": "A model that scores {t}",
        "metric": "How {t} is measured", "document": "A write-up on {t}", "decision": "What was decided about {t}",
        "term": "What {t} means here", "person": "Who looks after {t}", "team": "The team behind {t}", "system": "The job that moves {t} data"}
TEAMS = ["fraud", "risk", "growth", "pricing", "collections", "platform", "data-eng", "ml-ops", "marketing", "finance",
         "servicing", "compliance", "research", "design"]
WORDS = ["churn", "fraud", "limit", "spend", "credit", "collections", "retention", "dispute", "merchant", "cashback",
         "nps", "chatbot", "aml", "bureau", "hardship", "travel", "promo", "income", "label", "routing", "segment",
         "velocity", "balance", "payment", "recovery", "uplift", "engagement", "forecast", "monitoring", "pricing"]


def main(argv):
    out = argv[1]
    n_things = int(argv[argv.index("--things") + 1]) if "--things" in argv else 20000
    n_links = int(argv[argv.index("--links") + 1]) if "--links" in argv else 45000
    rnd = random.Random(int(argv[argv.index("--seed") + 1]) if "--seed" in argv else 7)
    groups = "--no-groups" not in argv

    # projects of very different sizes (a long tail), and a shared middle of about 8%
    shared = int(n_things * 0.08)
    sizes, left = [], n_things - shared
    while left > 0:
        s = min(left, max(12, int(rnd.paretovariate(1.3) * 45)))
        sizes.append(s)
        left -= s
    names, seen = [], set()
    for i in range(len(sizes)):
        a, b = rnd.choice(WORDS), rnd.choice(WORDS)
        nm = f"{a}-{b}" if a != b else f"{a}-{i}"
        while nm in seen:
            nm += f"-{i}"
        seen.add(nm)
        names.append(nm)
    fam_names, fam_w = zip(*FAMILIES)
    team_w = [1 / (k + 1) ** 0.6 for k in range(len(TEAMS))]

    def tagged(n, f):                                     # its tag columns: type as family/kind, one team or two, a status
        ks = KINDS.get(f, [])
        n["type"] = f if not ks or rnd.random() < 0.25 else f"{f}/{rnd.choices(ks, [1 / (k + 1) ** 0.8 for k in range(len(ks))])[0]}"
        ts = list(dict.fromkeys(rnd.choices(TEAMS, team_w, k=2 if rnd.random() < 0.3 else 1)))
        n["team"] = ts if len(ts) > 1 else ts[0]
        n["status"] = rnd.choices(["live", "draft", "retired"], [70, 20, 10])[0]
        n["created"] = f"{rnd.randint(2019, 2026)}-{rnd.randint(1, 12):02d}-{rnd.randint(1, 28):02d}"   # a time tag
        if f in ("dataset", "feature"):
            n["rows"] = rnd.randint(1, 900) * 1000                                            # a number tag, for some
        topic = f"{rnd.choice(WORDS)} {rnd.choice(WORDS)}"
        n["definition"] = WHAT[f].format(t=topic) + ", " + rnd.choice([          # a text tag: shown and searched, not coloured
            f"about {rnd.randint(2, 900) * 1000:,} rows a day", f"kept since {rnd.randint(2018, 2026)}", f"reviewed every {rnd.choice(['month', 'quarter', 'year'])}",
            f"owned by the {ts[0]} team", f"used by {rnd.randint(2, 40)} models", f"last checked in {rnd.choice(['March', 'June', 'October'])} {rnd.randint(2024, 2026)}"])
        return n
    nodes, members = [], []
    for p, s in enumerate(sizes):
        ids = []
        for j in range(s):
            f = rnd.choices(fam_names, fam_w)[0]
            nid = f"{f[:2]}-{names[p]}-{j}"
            nodes.append(tagged({"id": nid, "label": nid, "group": names[p] if groups else ""}, f))
            ids.append(len(nodes) - 1)
        members.append(ids)
    middle = []
    for j in range(shared):
        f = rnd.choices(fam_names, fam_w)[0]
        nodes.append(tagged({"id": f"{f[:2]}-shared-{j}", "label": f"{f}-shared-{j}", "group": ""}, f))
        middle.append(len(nodes) - 1)

    links, have = [], set()

    def add(a, b):
        if a == b or (a, b) in have:
            return False
        have.add((a, b))
        ty = rnd.choice(EDGES) if rnd.random() > 0.05 else "related-to"   # related-to: a link with no direction
        links.append({"source": nodes[a]["id"], "target": nodes[b]["id"], "type": ty,
                      "text": f"{nodes[a]['label']} {ty.replace('-', ' ')} {nodes[b]['label']}, as note {rnd.randint(1, 9999)} says.",
                      "status": rnd.choices(["confirmed", "proposed"], [80, 20])[0],          # the link's tags: a category,
                      "source_system": rnd.choices(["lineage-scan", "catalog", "manual", "model"], [50, 25, 15, 10])[0],   # where it came from,
                      "observed": f"{rnd.randint(2024, 2026)}-{rnd.randint(1, 12):02d}-{rnd.randint(1, 28):02d}",          # when (a time),
                      "weight": min(8, int(rnd.paretovariate(1.6)))})                            # and how strong (a number)
        return True

    # inside each project: preferential attachment, so a few things in each are linked to most of the rest; each
    # thing is first tied to one before it, so none is left without a link (the page shows only linked things)
    inside = int(n_links * 0.82)
    per_node = inside / (n_things - shared)
    for ids in members:
        deg = [1] * len(ids)
        want = int(round(per_node * len(ids)))
        for j in range(1, len(ids)):
            b = rnd.choices(range(j), deg[:j])[0] if j < 400 else rnd.randrange(j)
            if add(ids[j], ids[b]):
                deg[j] += 1
                deg[b] += 1
                want -= 1
        for _ in range(want * 3):
            if want <= 0:
                break
            a = rnd.randrange(len(ids))
            b = rnd.choices(range(len(ids)), deg)[0] if len(ids) < 400 else rnd.randrange(len(ids))
            if add(ids[a], ids[b]):
                deg[a] += 1
                deg[b] += 1
                want -= 1
    # the middle: twenty hubs most projects use, and the rest each used by a few projects (each by one at least)
    hubs = middle[:20]
    for h in hubs:
        for _ in range(rnd.randint(150, 450)):
            p = rnd.randrange(len(members))
            add(rnd.choice(members[p]), h)
    for m in middle[20:]:
        add(rnd.choice(members[rnd.randrange(len(members))]), m)
    while len(links) < n_links:
        if rnd.random() < 0.55:
            m = rnd.choice(middle[20:])
            p = rnd.randrange(len(members))
            add(rnd.choice(members[p]), m) if rnd.random() < 0.7 else add(m, rnd.choice(members[p]))
        else:                                            # between two projects, mostly neighbours in the list
            p = rnd.randrange(len(members))
            q = min(len(members) - 1, max(0, p + rnd.randint(-6, 6)))
            add(rnd.choice(members[p]), rnd.choice(members[q]))
    json.dump({"nodes": nodes, "links": links}, open(out, "w"))
    print(f"{out}: {len(nodes):,} things in {len(sizes)} projects and a middle of {shared:,}; {len(links):,} links")


if __name__ == "__main__":
    main(sys.argv)
