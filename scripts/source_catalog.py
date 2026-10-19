"""Generate the human-readable source catalog from public-only records."""

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render():
    data = json.loads((ROOT / "sources/public-sources.json").read_text())
    lines = [
        "# Sources and accounts", "",
        "This catalog contains selected public sources used by the fieldbook. It is not a repository inventory. Pinned README access establishes that the cited file was publicly readable; it does not establish runtime behavior or independent reproduction of its results.", "",
        "Source records distinguish support, limits, authorship, rights, and the actual source check. New chapter recommendations are editorial synthesis. Essays retain their historical author-reported state. Owner accounts are labeled separately; publishing an account does not make it independent evidence.", "",
    ]
    for source in data["sources"]:
        lines.extend([
            f'<h2 id="{html.escape(source["id"], quote=True)}">{html.escape(source["title"])}</h2>', "",
            f'**Source:** [{source["title"]}]({source["url"]})', "",
            f'**Authors:** {source["authors"]}', "",
            f'**Kind:** {source["kind"]}', "",
            f'**Used for:** {source["supports"]}', "",
            f'**Limits:** {source["limits"]}', "",
            f'**Rights:** {source["rights"]}', "",
        ])
        if source.get("revision"):
            lines.extend([f'Revision: `{source["revision"]}`.', ""])
        lines.extend([f'Source check: {source["verification"]} Recorded `{source["verified_at"]}`.', ""])
        if source.get("source_sha256"):
            lines.extend([f'Source body SHA-256: `{source["source_sha256"]}`.', ""])
        if source.get("reprint_path"):
            path = source["reprint_path"]
            lines.extend([f'Included text: [{path}](../{path}). Its file digest is recorded in `public-sources.json`.', ""])
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    target = ROOT / "sources/README.md"
    expected = render()
    if args.check:
        if not target.exists() or target.read_text() != expected:
            raise SystemExit("Source catalog is stale; run python scripts/source_catalog.py")
        print("Source catalog matches its public records.")
    else:
        target.write_text(expected)
        print("Wrote sources/README.md")


if __name__ == "__main__":
    main()
