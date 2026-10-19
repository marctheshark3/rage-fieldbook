"""An original fictional fixture: turn an explicit reading list into a digest.

The baseline deliberately includes a selection mistake for the walkthrough.
Neither version calls a model, fetches articles, or writes files.
"""

import argparse
import csv
import sys
from pathlib import Path

SOURCE = Path(__file__).with_name("reading-list.csv")


def read_rows(stream):
    reader = csv.DictReader(stream)
    if reader.fieldnames != ["id", "title", "state"]:
        raise ValueError("Expected the header id,title,state")
    rows = []
    seen = set()
    for number, row in enumerate(reader, start=2):
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"Row {number}: expected three fields")
        identity, title, state = row["id"], row["title"], row["state"]
        if not identity.strip() or identity in seen:
            raise ValueError(f"Row {number}: IDs must be present and unique")
        if not title.strip() or "\n" in title or "\r" in title:
            raise ValueError(f"Row {number}: expected a nonempty single-line title")
        if state not in {"unread", "read", "archived"}:
            raise ValueError(f"Row {number}: unknown reading state {state!r}")
        seen.add(identity)
        rows.append(row)
    return rows


def make_digest(rows, version="revised"):
    if version == "baseline":
        selected = [row for row in rows if row["state"]]
    elif version == "revised":
        selected = [row for row in rows if row["state"] == "unread"]
    else:
        raise ValueError(f"Unknown version: {version}")
    if not selected:
        return "# Read next\n\nNothing unread.\n"
    return "# Read next\n\n" + "".join(f'- {row["title"]} ({row["id"]})\n' for row in selected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", choices=["baseline", "revised"], default="revised")
    parser.add_argument("--source", type=Path, default=SOURCE)
    args = parser.parse_args()
    try:
        with args.source.open(encoding="utf-8", newline="") as stream:
            output = make_digest(read_rows(stream), args.version)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    sys.stdout.write(output)


if __name__ == "__main__":
    main()
