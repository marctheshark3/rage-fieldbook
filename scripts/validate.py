"""Check the explicit publication set, sources, navigation, and common leaks."""

import hashlib
import html
import json
import posixpath
import re
import subprocess
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
LEAK_PATTERNS = [
    ("local user path", re.compile(r"/(?:home|Users)/[A-Za-z0-9_.-]+/")),
    ("private key", re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{30,}\b")),
    ("service token", re.compile(r"\bsk-[A-Za-z0-9_-]{24,}\b|\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("private or local URL", re.compile(r"https?://(?:localhost|127\.\d+\.\d+\.\d+|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+|100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7])\.\d+\.\d+)(?=[:/\s]|$)", re.I)),
    ("private host URL", re.compile(r"https?://[^\s/]+\.(?:ts\.net|local|internal)(?=[:/\s]|$)", re.I)),
    ("credential in URL", re.compile(r"https?://[^\s/@:]+:[^\s/@]+@", re.I)),
]


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.anchors = set()

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.anchors.add(attributes["id"])
        if tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"])
        if tag in {"img", "script", "link"}:
            value = attributes.get("src") or attributes.get("href")
            if value:
                self.links.append(value)


def safe_path(value):
    path = PurePosixPath(value)
    return bool(value) and "\\" not in value and not path.is_absolute() and ".." not in path.parts and str(path) == value


def allowed_files(root):
    return [line.strip() for line in (root / "public-files.txt").read_text().splitlines() if line.strip() and not line.startswith("#")]


def scan_text(text, name):
    return [f"{name}: possible {label}" for label, pattern in LEAK_PATTERNS if pattern.search(text)]


def validate_tree(root):
    errors = []
    allowed = allowed_files(root)
    if len(allowed) != len(set(allowed)):
        errors.append("Publication allowlist contains duplicates")
    documents = {}
    for name in allowed:
        if not safe_path(name):
            errors.append(f"Unsafe publication path: {name}")
            continue
        path = root / name
        if not path.is_file() or path.is_symlink() or path.resolve() != root.resolve() / name:
            errors.append(f"Missing or indirect publication file: {name}")
            continue
        if name.rsplit("/", 1)[-1].startswith(".env") or path.stat().st_size > 1_000_000:
            errors.append(f"Disallowed publication file: {name}")
            continue
        text = path.read_text()
        errors.extend(scan_text(text, name))
        if name.endswith(".md"):
            if re.search(r"<(?:script|iframe)\b", text, re.I):
                errors.append(f"Active HTML in Markdown: {name}")
            document = Document()
            document.feed(markdown.markdown(text, extensions=["fenced_code", "tables", "toc", "sane_lists"]))
            documents[name] = document
    manifest = json.loads((root / "book.json").read_text())
    pages = [page["path"] for section in manifest["sections"] for page in section["pages"]]
    if len(pages) != len(set(pages)):
        errors.append("Book contains duplicate pages")
    for name in pages:
        if not safe_path(name) or name not in documents:
            errors.append(f"Book page is not a declared Markdown file: {name}")
    for name, document in documents.items():
        for link in document.links:
            parsed = urlsplit(html.unescape(link))
            if parsed.scheme or parsed.netloc:
                if parsed.scheme not in {"https", "mailto"} or parsed.username or parsed.password:
                    errors.append(f"Disallowed link in {name}: {link}")
                continue
            path = unquote(parsed.path)
            target = posixpath.normpath(posixpath.join(posixpath.dirname(name), path)) if path else name
            if not safe_path(target) or target not in allowed:
                errors.append(f"Undeclared local link in {name}: {link}")
            elif parsed.fragment and target in documents and unquote(parsed.fragment) not in documents[target].anchors:
                errors.append(f"Missing local anchor in {name}: {link}")
    sources = json.loads((root / "sources/public-sources.json").read_text())["sources"]
    ids = [source["id"] for source in sources]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate public source IDs")
    for source in sources:
        sid = source["id"]
        for required in ["id", "title", "kind", "url", "authors", "supports", "limits", "rights", "verified_at", "verification"]:
            if not source.get(required):
                errors.append(f"Source {sid}: missing {required}")
        url = urlsplit(source["url"])
        if url.scheme != "https" or not url.hostname or url.username or url.password:
            errors.append(f"Source {sid}: requires an HTTPS public URL without credentials")
        if source["kind"] == "repository":
            revision = source.get("revision", "")
            repo = source.get("repository", "")
            if not re.fullmatch(r"[a-f0-9]{40}", revision) or url.hostname != "github.com" or not url.path.startswith(f"/{repo}/blob/{revision}/"):
                errors.append(f"Source {sid}: repository source must pin an exact file revision")
            if not re.fullmatch(r"[a-f0-9]{64}", source.get("source_sha256", "")):
                errors.append(f"Source {sid}: missing pinned file digest")
        if source.get("reprint_path"):
            path = source["reprint_path"]
            if path not in allowed or not safe_path(path):
                errors.append(f"Source {sid}: undeclared reprint")
            elif hashlib.sha256((root / path).read_bytes()).hexdigest() != source.get("reprint_sha256"):
                errors.append(f"Source {sid}: essay reprint differs from its recorded capture")
    # Check both tracked and untracked candidates when this is the repository root.
    identity = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=root, text=True, capture_output=True)
    if identity.returncode == 0 and Path(identity.stdout.strip()).resolve() == root.resolve():
        result = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=root)
        actual = {name.decode() for name in result.split(b"\0") if name}
        for name in sorted(actual - set(allowed)):
            errors.append(f"File outside publication allowlist: {name}")
    return errors


def validate_site(root):
    output = root / "_site"
    if not output.exists():
        return []
    errors = []
    for path in output.rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text()
        errors.extend(scan_text(text, str(path.relative_to(output))))
        if path.suffix != ".html":
            continue
        document = Document()
        document.feed(text)
        for link in document.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path.resolve()
            if not target.is_relative_to(output.resolve()) or not target.is_file():
                errors.append(f"Broken generated link in {path.relative_to(output)}: {link}")
            elif parsed.fragment and target.suffix == ".html":
                linked_document = Document()
                linked_document.feed(target.read_text())
                if unquote(parsed.fragment) not in linked_document.anchors:
                    errors.append(f"Missing generated anchor in {path.relative_to(output)}: {link}")
    return errors


def main():
    errors = validate_tree(ROOT) + validate_site(ROOT)
    if errors:
        raise SystemExit("\n".join(errors))
    print("Publication allowlist, navigation, source records, essay captures, and common-leak checks pass.")
    print("Pattern checks supplement editorial review; they do not certify absence of private information.")


if __name__ == "__main__":
    main()
