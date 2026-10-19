"""Verify pinned public repository files by anonymous HTTPS, without credentials."""

import concurrent.futures
import hashlib
import json
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]


def verify(source):
    parsed = urlsplit(source["url"])
    if parsed.scheme != "https" or parsed.hostname != "github.com" or "/blob/" not in parsed.path:
        raise ValueError("Expected a pinned GitHub file URL")
    url = "https://raw.githubusercontent.com" + parsed.path.replace("/blob/", "/", 1)
    request = urllib.request.Request(url, headers={"User-Agent": "RageFieldbookPublicSourceCheck/0.1"})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
        if response.status != 200:
            raise ValueError("Non-success response")
    if hashlib.sha256(data).hexdigest() != source["source_sha256"]:
        raise ValueError("Pinned source digest differs")
    return source["id"]


def main():
    data = json.loads((ROOT / "sources/public-sources.json").read_text())
    sources = [source for source in data["sources"] if source["kind"] == "repository"]
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(verify, source): source for source in sources}
        for future in concurrent.futures.as_completed(futures):
            source = futures[future]
            try:
                future.result()
            except Exception as error:
                failures.append(f'{source["id"]}: {type(error).__name__}: {error}')
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"All {len(sources)} pinned repository source files match their recorded hashes through anonymous HTTPS.")
    print("Essay and official documentation access checks are recorded separately in the source catalog.")


if __name__ == "__main__":
    main()
