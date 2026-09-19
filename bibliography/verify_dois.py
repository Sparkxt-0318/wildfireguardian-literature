#!/usr/bin/env python3
"""Citation auditor: resolve every DOI in literature/metadata/*.yaml against
Crossref/DataCite and compare the returned record with what we wrote down.

This exists because the single worst failure this repository can commit is a
fabricated or subtly-wrong citation (AGENTS.md section 3). A DOI that does not
resolve, or that resolves to a different title or year than our metadata
claims, is caught here rather than by a judge.

Usage:
    python3 bibliography/verify_dois.py                 # audit all
    python3 bibliography/verify_dois.py --write-registry  # also refresh doi_registry.csv

Exit code is non-zero if any DOI fails to resolve, so this can gate a commit.
"""
import argparse
import csv
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
META = ROOT / "literature" / "metadata"
REGISTRY = ROOT / "bibliography" / "doi_registry.csv"
UA = "WildfireGuardianLiteratureAudit/1.0 (mailto:noreply@anthropic.com)"

# Deliberately tiny YAML reader: our metadata files are flat key: value plus a
# one-level 'matrix:' block. Avoiding a PyYAML dependency keeps the audit
# runnable anywhere, which matters more here than generality.
SCALAR = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")


def read_meta(path):
    data, cur = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            if cur:
                m = SCALAR.match(line.strip())
                if m:
                    data.setdefault(cur, {})[m.group(1)] = m.group(2).strip()
            continue
        m = SCALAR.match(line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val == "":
            cur = key
            data.setdefault(key, {})
        else:
            cur = None
            data[key] = val.strip('"').strip("'")
    return data


def fetch(url, attempts=4):
    """Fetch with backoff. Crossref rate-limits bursts, and a transient
    URLError must never be reported as a DOI that does not resolve -- that
    would be the audit crying wolf about fabrication."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    last = None
    for i in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError:
            raise                                    # 404 etc. are real answers
        except Exception as e:                       # network/transient only
            last = e
            time.sleep(2 ** i)
    raise last


def resolve_datacite(doi):
    """arXiv and Zenodo register DOIs with DataCite, not Crossref, so a
    Crossref 404 alone does not mean the DOI is fake."""
    d = fetch("https://api.datacite.org/dois/" + urllib.parse.quote(doi, safe=""))["data"]["attributes"]
    titles = d.get("titles") or [{}]
    return ("RESOLVED_DATACITE", titles[0].get("title", ""), d.get("publicationYear"),
            d.get("publisher") if isinstance(d.get("publisher"), str)
            else (d.get("publisher") or {}).get("name", ""))


def resolve(doi):
    """Return (status, title, year, container) for a DOI.

    Crossref first, DataCite second. Only a failure at BOTH registries counts
    as a DOI that does not resolve.
    """
    doi = doi.strip().replace("https://doi.org/", "").rstrip(".")
    try:
        m = fetch("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
        title = (m.get("title") or [""])[0]
        parts = m.get("issued", {}).get("date-parts") or [[None]]
        return "RESOLVED", title, parts[0][0], (m.get("container-title") or [""])[0]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            try:
                return resolve_datacite(doi)
            except Exception:
                return "NOT_FOUND", "", None, ""
        return f"HTTP_{e.code}", "", None, ""
    except Exception as e:                                  # network, parse, etc.
        return f"ERROR:{type(e).__name__}", "", None, ""


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write-registry", action="store_true")
    args = ap.parse_args()

    rows, failures = [], []
    files = sorted(META.glob("*.yaml"))
    if not files:
        print("no metadata files found", file=sys.stderr)
        return 0

    for path in files:
        meta = read_meta(path)
        pid = meta.get("paper_id", path.stem)
        doi = (meta.get("doi") or "").strip()
        claimed_title = meta.get("title", "")
        claimed_year = meta.get("year", "")

        if not doi or doi.upper() in {"UNVERIFIED", "NONE", "N/A", "-"}:
            rows.append([pid, "", "NO_DOI", "", "", "", meta.get("publication_status", "")])
            continue

        status, title, year, container = resolve(doi)
        time.sleep(0.5)                                     # be polite to Crossref

        agree = ""
        if status.startswith("RESOLVED"):
            t_ok = norm(title)[:60] == norm(claimed_title)[:60] or norm(claimed_title)[:40] in norm(title)
            y_ok = str(year) == str(claimed_year).strip()
            agree = "MATCH" if (t_ok and y_ok) else ("TITLE_MISMATCH" if not t_ok else "YEAR_MISMATCH")
            if agree != "MATCH":
                failures.append((pid, doi, agree, f"registry={claimed_title!r}/{claimed_year} crossref={title!r}/{year}"))
        else:
            failures.append((pid, doi, status, "DOI did not resolve"))

        rows.append([pid, doi, status, agree, title, str(year or ""), container])

    if args.write_registry:
        REGISTRY.parent.mkdir(parents=True, exist_ok=True)
        with REGISTRY.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["paper_id", "doi", "resolution_status", "metadata_agreement",
                        "resolved_title", "resolved_year", "resolved_container"])
            w.writerows(rows)
        print(f"wrote {REGISTRY.relative_to(ROOT)} ({len(rows)} rows)")

    print(f"\naudited {len(rows)} records")
    print(f"  no DOI recorded : {sum(1 for r in rows if r[2] == 'NO_DOI')}")
    print(f"  resolved        : {sum(1 for r in rows if r[2].startswith('RESOLVED'))}")
    print(f"  failures        : {len(failures)}")
    for pid, doi, why, detail in failures:
        print(f"    FAIL {pid} [{doi}] {why} -- {detail}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
