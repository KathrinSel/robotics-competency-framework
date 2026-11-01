"""
Build tool for the Robotics Competency Framework.

framework.yaml is the single source of truth. This script:
  1. validates it (ids, references, levels, requirement tiers, interview gates)
  2. generates competency_matrix.csv (human-friendly table)
  3. generates framework.json (for tools and integrations)

Usage (from the repository root):
    pip install pyyaml
    python tools/build.py
"""

import csv
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "framework.yaml"
CSV_OUT = ROOT / "competency_matrix.csv"
JSON_OUT = ROOT / "framework.json"
SEARCH_STATUSES = {"open", "closed"}


def validate(doc: dict) -> list[str]:
    errors = []
    domain_ids = [d["id"] for d in doc["domains"]]
    comp_ids = [c["id"] for c in doc["competencies"]]
    comp_by_id = {c["id"]: c for c in doc["competencies"]}
    statuses = set(doc["calibration_statuses"])
    gates = doc.get("interview_gates", {}).get("gates", [])

    for kind, ids in (("domain", domain_ids), ("competency", comp_ids), ("role", [r["id"] for r in doc["roles"]])):
        dupes = {i for i in ids if ids.count(i) > 1}
        if dupes:
            errors.append(f"duplicate {kind} ids: {sorted(dupes)}")

    for c in doc["competencies"]:
        if c["domain"] not in domain_ids:
            errors.append(f"competency '{c['id']}' references unknown domain '{c['domain']}'")

    for g in gates:
        if g not in comp_by_id:
            errors.append(f"interview gate '{g}' is not a defined competency")
        elif comp_by_id[g].get("assessed_in") != "interview":
            errors.append(f"interview gate '{g}' must have assessed_in: interview")

    for r in doc["roles"]:
        rid, req = r["id"], r["requirements"]
        must, ideal = r.get("must_have", []), r.get("ideal_profile", [])
        if r["calibration"]["status"] not in statuses:
            errors.append(f"role '{rid}': unknown calibration status '{r['calibration']['status']}'")
        if "search_status" in r and r["search_status"] not in SEARCH_STATUSES:
            errors.append(f"role '{rid}': search_status must be one of {sorted(SEARCH_STATUSES)}")
        for cid, lvl in req.items():
            if cid not in comp_ids:
                errors.append(f"role '{rid}': unknown competency '{cid}'")
            elif cid in gates:
                errors.append(f"role '{rid}': '{cid}' is an interview gate — it applies to all roles, do not list it per role")
            if lvl not in (1, 2, 3):
                errors.append(f"role '{rid}': '{cid}' has level {lvl!r} (use 1-3, omit for 0)")
        for tier, ids in (("must-have", must), ("ideal-profile", ideal)):
            for cid in ids:
                if req.get(cid, 0) < 2:
                    errors.append(f"role '{rid}': {tier} '{cid}' needs level 2 or 3")
        overlap = set(must) & set(ideal)
        if overlap:
            errors.append(f"role '{rid}': {sorted(overlap)} cannot be both must-have and ideal-profile")
        if not must:
            errors.append(f"role '{rid}': has no must-have competencies")
    return errors


def write_csv(doc: dict) -> None:
    domains = {d["id"]: d for d in doc["domains"]}
    roles = doc["roles"]
    gates = doc.get("interview_gates", {})
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Domain", "Competency"] + [r["name"] for r in roles])
        w.writerow(["", "★ = must-have (stop-factor) · ◆ = ideal profile · 0=not required · 1=Aware · 2=Practitioner · 3=Expert"]
                   + [""] * len(roles))
        w.writerow(["", "Calibration"] + [r["calibration"]["status"] + (" (search closed)" if r.get("search_status") == "closed" else "")
                                          for r in roles])
        for c in doc["competencies"]:
            d = domains[c["domain"]]
            if c["id"] in gates.get("gates", []):
                cells = [f"{gates['required_level']} (gate, interview)"] * len(roles)
            else:
                cells = []
                for r in roles:
                    lvl = r["requirements"].get(c["id"], 0)
                    mark = "★" if c["id"] in r.get("must_have", []) else "◆" if c["id"] in r.get("ideal_profile", []) else ""
                    cells.append(f"{lvl}{mark}")
            w.writerow([f"{d['code']} · {d['name']}", c["name"]] + cells)


def write_json(doc: dict) -> None:
    out = json.loads(json.dumps(doc))  # deep copy with string keys
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")


def main() -> int:
    doc = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    errors = validate(doc)
    if errors:
        print("framework.yaml has errors — nothing was generated:\n")
        for e in errors:
            print("  ✗", e)
        return 1
    write_csv(doc)
    write_json(doc)
    print(f"✓ framework.yaml v{doc['framework']['version']} is valid: {len(doc['roles'])} roles, "
          f"{len(doc['competencies'])} competencies, {len(doc['domains'])} domains")
    print(f"✓ generated {CSV_OUT.name} and {JSON_OUT.name}")
    for r in doc["roles"]:
        closed = " (search closed)" if r.get("search_status") == "closed" else ""
        print(f"  {r['id']:<28} {r['calibration']['status']:<22} ★ {len(r['must_have'])}  ◆ {len(r.get('ideal_profile', []))}{closed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
