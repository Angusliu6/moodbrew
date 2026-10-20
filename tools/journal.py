#!/usr/bin/env python3
"""MoodBrew private JSON tasting journal. Standard library only. Nothing uploads.

Usage:
  python tools/journal.py init my-coffee.json
  python tools/journal.py add my-coffee.json entry.json
  python tools/journal.py list my-coffee.json
  python tools/journal.py summary my-coffee.json
  python tools/journal.py export my-coffee.json backup.json
  python tools/journal.py validate my-coffee.json
"""
from __future__ import annotations

import argparse
from collections import Counter
from datetime import date
import json
import os
from pathlib import Path
import tempfile

AXES = {"sweetness", "acidity", "bitterness", "body", "finish", "after_sweetness", "aroma", "overall"}
STATUSES = {"planned", "ordered", "tasted"}


def empty_journal():
    return {"schema_version": "1.0.0", "profile": {"display_name": None, "preferences": {}, "updated_at": None}, "entries": []}


def validate_entry(entry):
    if not isinstance(entry, dict):
        raise ValueError("entry must be a JSON object")
    for f in ("entry_id", "date", "status", "coffee"):
        if f not in entry:
            raise ValueError(f"missing entry field: {f}")
    if not isinstance(entry["entry_id"], str) or not entry["entry_id"].strip():
        raise ValueError("entry_id must be nonempty string")
    if not isinstance(entry["date"], str):
        raise ValueError("date must be YYYY-MM-DD string")
    try:
        if date.fromisoformat(entry["date"]).isoformat() != entry["date"]:
            raise ValueError("date must be YYYY-MM-DD")
    except (TypeError, ValueError) as e:
        raise ValueError("date must be valid YYYY-MM-DD") from e
    if entry["status"] not in STATUSES:
        raise ValueError("status must be planned, ordered, or tasted")
    coffee = entry["coffee"]
    if not isinstance(coffee, dict) or not isinstance(coffee.get("name"), str) or not coffee["name"].strip():
        raise ValueError("coffee.name must be a nonempty string")
    if "ratings" in entry:
        r = entry["ratings"]
        if not isinstance(r, dict):
            raise ValueError("ratings must be object")
        for key, value in r.items():
            if key not in AXES:
                raise ValueError(f"unknown rating axis: {key}")
            if value is not None and (type(value) is not int or not 1 <= value <= 5):
                raise ValueError(f"rating {key} must be integer 1..5 or null")
    for field in ("brew", "mood"):
        if field in entry and not isinstance(entry[field], dict):
            raise ValueError(f"{field} must be object")
    return entry


def validate_journal(data):
    if not isinstance(data, dict) or data.get("schema_version") != "1.0.0":
        raise ValueError("unsupported or missing schema_version (expected 1.0.0)")
    if not isinstance(data.get("entries"), list):
        raise ValueError("entries must be an array")
    seen = set()
    for entry in data["entries"]:
        validate_entry(entry)
        if entry["entry_id"] in seen:
            raise ValueError("duplicate entry_id: " + entry["entry_id"])
        seen.add(entry["entry_id"])
    return data


def load(path):
    with Path(path).open("r", encoding="utf-8") as f:
        return validate_journal(json.load(f))


def atomic_write(path, data):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".moodbrew-", suffix=".json", dir=str(p.parent))
    try:
        if os.name == "posix":
            os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        os.replace(tmp, p)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def add_entry(journal_path, entry_path):
    journal = load(journal_path)
    with Path(entry_path).open("r", encoding="utf-8") as f:
        entry = validate_entry(json.load(f))
    if any(item["entry_id"] == entry["entry_id"] for item in journal["entries"]):
        raise ValueError("entry_id already exists; no data changed")
    journal["entries"].append(entry)
    validate_journal(journal)
    atomic_write(journal_path, journal)
    return entry


def profile_summary(journal):
    tasted = [e for e in journal["entries"] if e["status"] == "tasted"]
    axes = {}
    for axis in sorted(AXES):
        values = [e.get("ratings", {}).get(axis) for e in tasted]
        values = [v for v in values if v is not None]
        if values:
            axes[axis] = {"mean": round(sum(values) / len(values), 2), "sample_size": len(values)}
    origins = Counter(e.get("coffee", {}).get("origin_country") for e in tasted)
    origins.pop(None, None)
    return {"total_entries": len(journal["entries"]), "tasted_entries": len(tasted), "rated_axes": axes, "origin_counts": dict(origins)}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)
    for cmd in ("init", "list", "summary", "validate"):
        sub.add_parser(cmd).add_argument("journal")
    sub.add_parser("add").add_argument("journal")
    sub.choices["add"].add_argument("entry")
    sub.add_parser("export").add_argument("journal")
    sub.choices["export"].add_argument("backup")
    args = p.parse_args(argv)
    if args.command == "init":
        if Path(args.journal).exists():
            p.error("refusing to overwrite existing journal")
        atomic_write(args.journal, empty_journal())
        print(f"Created local journal: {args.journal}")
        return
    journal = load(args.journal)
    if args.command == "add":
        entry = add_entry(args.journal, args.entry)
        print(f"Added {entry['entry_id']} (local file only)")
    elif args.command == "list":
        for e in sorted(journal["entries"], key=lambda x: (x["date"], x["entry_id"]), reverse=True):
            mood = e.get("mood", {}).get("before", "?")
            print(f"{e['date']} [{e['status']}] {e['coffee']['name']} | mood: {mood}")
        print(f"Total: {len(journal['entries'])}")
    elif args.command == "summary":
        print(json.dumps(profile_summary(journal), ensure_ascii=False, indent=2))
    elif args.command == "validate":
        print(f"Valid journal with {len(journal['entries'])} entries")
    elif args.command == "export":
        src, dst = Path(args.journal).resolve(), Path(args.backup).resolve()
        if src == dst:
            p.error("backup path must be different from journal path")
        if dst.exists():
            p.error("refusing to overwrite existing backup")
        atomic_write(dst, journal)
        print(f"Backup exported to: {dst}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        raise SystemExit(f"MoodBrew journal error: {exc}") from exc
