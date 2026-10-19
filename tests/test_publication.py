"""Regression checks for the publication boundary, not for project claims."""

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate import allowed_files, scan_text, validate_tree


class PublicationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in allowed_files(ROOT):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def test_unlisted_file_is_rejected_before_publication(self):
        subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)
        (self.root / "unreviewed-draft.txt").write_text("Draft outside the publication set.\n")
        self.assertTrue(any("outside publication allowlist" in error for error in validate_tree(self.root)))

    def test_build_rejects_a_page_outside_the_publication_set(self):
        manifest = json.loads((self.root / "book.json").read_text())
        manifest["sections"][0]["pages"].append({"path": "unreviewed-draft.md", "title": "Draft"})
        (self.root / "book.json").write_text(json.dumps(manifest))
        (self.root / "unreviewed-draft.md").write_text("# Unreviewed draft\n")
        result = subprocess.run([sys.executable, str(self.root / "scripts/build.py")], text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not a declared Markdown file", result.stderr)
        self.assertFalse((self.root / "_site").exists())

    def test_paths_cannot_escape_the_book(self):
        manifest = json.loads((self.root / "book.json").read_text())
        manifest["sections"][0]["pages"].append({"path": "../unselected.md", "title": "Outside"})
        (self.root / "book.json").write_text(json.dumps(manifest))
        self.assertTrue(any("not a declared Markdown file" in error for error in validate_tree(self.root)))

    def test_historical_essay_changes_require_a_new_record(self):
        (self.root / "essays/player-two.md").write_text("# A silently changed historical essay\n")
        self.assertTrue(any("differs from its recorded capture" in error for error in validate_tree(self.root)))

    def test_common_disclosure_patterns_are_detected(self):
        examples = [
            "/" + "home" + "/someone/project/file.txt",
            "https://" + "10.23.4.5/service",
            "https://" + "private-host" + ".ts.net/service",
            "ghp_" + "a" * 35,
            "-----BEGIN " + "OPENSSH PRIVATE KEY-----",
        ]
        for example in examples:
            with self.subTest(example=example):
                self.assertTrue(scan_text(example, "candidate"))


if __name__ == "__main__":
    unittest.main()
