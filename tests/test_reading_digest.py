"""Acceptance checks for the fictional digest, not a model or skill evaluation.

Run normally to check the revision. Pass --version baseline to reproduce the
two deliberate selection failures; that invocation should exit unsuccessfully.
"""

import argparse
import importlib.util
import io
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("reading_digest_fixture", ROOT / "examples/reading-digest/digest.py")
digest = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(digest)
VERSION = "revised"


class ReadingDigestTests(unittest.TestCase):
    def render(self, text):
        return digest.make_digest(digest.read_rows(io.StringIO(text)), VERSION)

    def test_mixed_states_select_only_unread(self):
        with digest.SOURCE.open(encoding="utf-8", newline="") as stream:
            actual = digest.make_digest(digest.read_rows(stream), VERSION)
        self.assertEqual(actual, "# Read next\n\n- The rain garden after the storm (r1)\n- A small seed library (r3)\n")

    def test_no_unread_entries_says_so(self):
        actual = self.render("id,title,state\nr2,Already read,read\nr4,Old proposal,archived\n")
        self.assertEqual(actual, "# Read next\n\nNothing unread.\n")

    def test_order_and_distinct_entries_survive(self):
        actual = self.render("id,title,state\nz,Same title,unread\na,Same title,unread\n")
        self.assertEqual(actual, "# Read next\n\n- Same title (z)\n- Same title (a)\n")

    def test_uses_the_supplied_title(self):
        actual = self.render("id,title,state\nr8,A changed heading,unread\n")
        self.assertEqual(actual, "# Read next\n\n- A changed heading (r8)\n")

    def test_unknown_state_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unknown reading state"):
            self.render("id,title,state\nr5,Uncertain,maybe\n")

    def test_missing_field_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "expected three fields"):
            self.render("id,title,state\nr5,Missing state\n")

    def test_duplicate_id_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "unique"):
            self.render("id,title,state\nr5,First,unread\nr5,Second,read\n")

    def test_source_file_is_unchanged(self):
        before = digest.SOURCE.read_bytes()
        with digest.SOURCE.open(encoding="utf-8", newline="") as stream:
            digest.make_digest(digest.read_rows(stream), VERSION)
        self.assertEqual(digest.SOURCE.read_bytes(), before)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--version", choices=["baseline", "revised"], default="revised")
    args, remaining = parser.parse_known_args()
    VERSION = args.version
    unittest.main(argv=[sys.argv[0], *remaining])
