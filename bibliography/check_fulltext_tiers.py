#!/usr/bin/env python3
"""Report full-text verification tier for every threatening paper, and refuse
to let a claim be held at high confidence when its closest threat has only
been read at title or abstract level.

Tier vocabulary (weakest to strongest):
    TITLE_ONLY < ABSTRACT_VERIFIED < FULL_TEXT_READ < METHODS_VERIFIED
    < RESULTS_VERIFIED

The rule this enforces: a paper can only be said to NOT occupy a claim on the
strength of what has actually been read. Concluding "it does not compute a
dispatch deadline" from an abstract is not a finding -- abstracts omit most of
what a paper does.

Usage:
    python3 bibliography/check_fulltext_tiers.py            # report
    python3 bibliography/check_fulltext_tiers.py --strict   # non-zero if any
                                                            # CRITICAL paper is
                                                            # below FULL_TEXT_READ
"""
import argparse
import collections
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
META = ROOT / "literature" / "metadata"
CLAIMS = ROOT / "docs" / "claims.yaml"

TIERS = ["TITLE_ONLY", "ABSTRACT_VERIFIED", "FULL_TEXT_READ",
         "METHODS_VERIFIED", "RESULTS_VERIFIED"]
RANK = {t: i for i, t in enumerate(TIERS)}
# Reading a claim's closest threat only at this level or below means the claim
# cannot be held at high confidence.
WEAK_CEILING = RANK["ABSTRACT_VERIFIED"]


def load_meta():
    out = []
    for p in sorted(META.glob("*.yaml")):
        try:
            d = yaml.safe_load(p.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  UNPARSEABLE {p.name}: {str(e)[:70]}", file=sys.stderr)
            continue
        if isinstance(d, dict) and d.get("paper_id"):
            out.append(d)
    return out


def tier_of(rec):
    t = str(rec.get("fulltext_status") or "").strip().upper()
    return t if t in RANK else "UNSPECIFIED"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    recs = load_meta()
    by_tier = collections.Counter(tier_of(r) for r in recs)

    print(f"{len(recs)} records\n")
    print("Full-text tier distribution")
    for t in TIERS + ["UNSPECIFIED"]:
        if by_tier[t]:
            print(f"  {t:<20} {by_tier[t]}")

    crit = [r for r in recs if str(r.get("threat_level", "")).upper() == "CRITICAL"]
    print(f"\nCRITICAL papers ({len(crit)}) — these gate every surviving claim")
    weak_crit = []
    for r in sorted(crit, key=lambda x: x["paper_id"]):
        t = tier_of(r)
        flag = ""
        if t == "UNSPECIFIED" or RANK.get(t, -1) <= WEAK_CEILING:
            flag = "   <-- below FULL_TEXT_READ"
            weak_crit.append(r["paper_id"])
        print(f"  {r['paper_id']:<32} {t}{flag}")

    # Which claims depend on a threat we have not really read?
    claims = yaml.safe_load(CLAIMS.read_text(encoding="utf-8"))["claims"]
    tiers = {r["paper_id"]: tier_of(r) for r in recs}
    print("\nConfidence ceiling by claim (from its weakest-read threat paper)")
    capped = []
    for c in sorted(claims, key=lambda x: x["claim_id"]):
        tp = c.get("threat_papers") or []
        if not tp:
            continue
        worst = min((RANK.get(tiers.get(p, "UNSPECIFIED"), -1) for p in tp), default=-1)
        label = TIERS[worst] if worst >= 0 else "UNSPECIFIED"
        cap = "HIGH_OK" if worst > WEAK_CEILING else "CAPPED: cannot hold high confidence"
        if worst <= WEAK_CEILING:
            capped.append(c["claim_id"])
        print(f"  {c['claim_id']}  status={c['status']:<20} weakest_threat_read={label:<18} {cap}")

    print(f"\n{len(weak_crit)} CRITICAL paper(s) below FULL_TEXT_READ: "
          + (", ".join(weak_crit) if weak_crit else "none"))
    print(f"{len(capped)} claim(s) confidence-capped by unread threats.")

    if args.strict and weak_crit:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
