import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from journal import add_entry, atomic_write, empty_journal, load, profile_summary, validate_entry, validate_journal


def sample(status="tasted", rating=4):
    return {"entry_id": "demo-one", "date": "2026-01-10", "status": status,
            "coffee": {"name": "Demo Guji", "origin_country": "Ethiopia"},
            "mood": {"before": "curious"}, "ratings": {"acidity": rating}}


class JournalTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(profile_summary(validate_journal(empty_journal()))["tasted_entries"], 0)

    def test_add_and_reload(self):
        with tempfile.TemporaryDirectory() as d:
            path, entryfile = Path(d) / "journal.json", Path(d) / "entry.json"
            atomic_write(path, empty_journal())
            entryfile.write_text(json.dumps(sample()), encoding="utf-8")
            add_entry(path, entryfile)
            self.assertEqual(len(load(path)["entries"]), 1)
            self.assertEqual(profile_summary(load(path))["rated_axes"]["acidity"]["mean"], 4)
            with self.assertRaisesRegex(ValueError, "already exists"):
                add_entry(path, entryfile)
            self.assertEqual(len(load(path)["entries"]), 1)

    def test_only_tasted_affects_profile(self):
        journal = empty_journal()
        journal["entries"] = [sample(status="ordered")]
        self.assertEqual(profile_summary(journal)["tasted_entries"], 0)

    def test_invalid_date_and_rating(self):
        with self.assertRaises(ValueError):
            validate_entry({**sample(), "date": "2026-02-30"})
        with self.assertRaises(ValueError):
            validate_entry(sample(rating=6))
        with self.assertRaises(ValueError):
            validate_entry(sample(rating=True))

    def test_duplicate_id_rejected(self):
        doc = empty_journal()
        doc["entries"] = [sample(), sample()]
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_journal(doc)

    def test_unknown_not_conjured(self):
        doc = empty_journal()
        doc["entries"].append({"entry_id": "x", "date": "2026-01-11", "status": "tasted", "coffee": {"name": "Unknown roast"}})
        s = profile_summary(validate_journal(doc))
        self.assertEqual(s["rated_axes"], {})
        self.assertEqual(s["origin_counts"], {})


if __name__ == "__main__":
    unittest.main()
