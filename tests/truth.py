"""Ground truth for the churn-2026 fixture: the real entities and the names that identify them (A18)."""
import re

TRUE = {
    "cards.txn_daily": ["cards.txn_daily", "txn_daily", "txn table", "txn-table", "cards-txn-daily", "transactions table"],
    "cards.churn_labels": ["cards.churn_labels", "churn_labels", "churn labels"],
    "cards.churn_scores": ["cards.churn_scores", "churn_scores"],
    "holdout-2025q4": ["holdout-2025q4", "holdout 2025q4", "holdout"],
    "offers.tier_matrix": ["offers.tier_matrix", "tier_matrix"],
    "recall-at-10": ["recall@10", "recall-at-10", "recall at 10", "recall-at-k", "recall_at_10"],
    "auc": ["auc", "roc-auc", "roc auc"],
    "feat-velocity-v2": ["feat-velocity-v2", "velocity v2", "velocity-v2", "velocity_v2"],
    "feat-velocity-v3": ["feat-velocity-v3", "velocity v3", "velocity-v3", "velocity_v3"],
    "feat-utilization-v1": ["feat-utilization-v1", "utilization features", "credit utilization features",
                            "utilization-v1", "utilization_v1"],
    "logreg-baseline": ["logreg-baseline", "logistic baseline", "logistic-baseline"],
    "churn-xgb-v2": ["churn-xgb-v2"],
    "churn-xgb-v3": ["churn-xgb-v3"],
    "xgboost": ["xgboost", "xgb"],
    "risk-tier-cuts": ["risk-tier cuts", "risk-tier-cuts", "risk tier cutoffs", "risk-tier-cutoffs", "risk tiers",
                       "risk-tiers"],
    "new-accounts": ["new accounts", "new-accounts"],
    "data-eng-cards": ["data-eng-cards"],
    "maya-ortiz": ["maya ortiz", "maya-ortiz"],
    "priya-nair": ["priya nair", "priya-nair"],
    "sam-lee": ["sam lee", "sam-lee"],
}


def fold(s):
    return re.sub(r"[\s_]+", "-", str(s).strip().lower())


def convergence(graph):
    """Distinct graph ids per true entity. ratio = ids that map to a true entity / true entities found."""
    pats = {t: {fold(p) for p in ps} for t, ps in TRUE.items()}
    per, ambiguous, other = {}, [], []
    for e in graph["entities"]:
        names = {fold(e["id"])} | {fold(a) for a in e["aka"]} | {fold(n["name"]) for n in e["names"]}
        hit = [t for t, ps in pats.items() if ps & names]
        if len(hit) == 1:
            per.setdefault(hit[0], []).append(e["id"])
        elif hit:
            ambiguous.append((e["id"], hit))
        else:
            other.append(e["id"])
    found = len(per)
    ids = sum(len(v) for v in per.values())
    return {"true_total": len(TRUE), "true_found": found, "ids_for_true": ids,
            "ratio": round(ids / found, 2) if found else None,
            "split": {t: v for t, v in per.items() if len(v) > 1}, "ambiguous": ambiguous, "other": sorted(other)}
