"""Build a static reader from the explicitly declared Markdown pages."""

import html
import json
import posixpath
import re
import shutil
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit, urlunsplit

import markdown

from validate import validate_tree

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"


def route(path):
    source = PurePosixPath(path)
    if source.name == "README.md":
        return str(source.with_name("index.html"))
    return str(source.with_suffix(".html"))


def relative(target, current):
    return posixpath.relpath(target, posixpath.dirname(current) or ".")


def rewrite_links(body, source, current, pages, repository):
    def replace(match):
        url = html.unescape(match.group(2))
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match.group(0)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(source), unquote(parsed.path)))
        if target in pages:
            path = relative(route(target), current)
            new_url = urlunsplit(("", "", path, parsed.query, parsed.fragment))
        else:
            new_url = repository + "/blob/main/" + target
            if parsed.fragment:
                new_url += "#" + parsed.fragment
        return 'href="' + html.escape(new_url, quote=True) + '"'
    return re.sub(r'''href=(["'])(.*?)\1''', replace, body)


def main():
    errors = validate_tree(ROOT)
    if errors:
        raise SystemExit("\n".join(errors))
    manifest = json.loads((ROOT / "book.json").read_text())
    pages = [page for section in manifest["sections"] for page in section["pages"]]
    by_path = {page["path"]: page for page in pages}
    # The output location is fixed; no user-supplied path can broaden deletion.
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    shutil.copyfile(ROOT / "assets/reader.css", OUTPUT / "reader.css")
    shutil.copyfile(ROOT / "assets/reader.js", OUTPUT / "reader.js")
    (OUTPUT / ".nojekyll").touch()
    for index, page in enumerate(pages):
        source = page["path"]
        current = route(source)
        raw = (ROOT / source).read_text()
        body = markdown.markdown(raw, extensions=["fenced_code", "tables", "toc", "sane_lists"])
        body = rewrite_links(body, source, current, by_path, manifest["repository"])
        navigation = []
        for section in manifest["sections"]:
            items = []
            for item in section["pages"]:
                active = ' aria-current="page"' if item["path"] == source else ""
                items.append(f'<li><a href="{relative(route(item["path"]), current)}"{active}>{html.escape(item["title"])}</a></li>')
            navigation.append(f'<div class="nav-group"><h2>{html.escape(section["title"])}</h2><ul>{"".join(items)}</ul></div>')
        previous = pages[index - 1] if index else None
        following = pages[index + 1] if index + 1 < len(pages) else None
        pager = []
        for label, item in [("Previous", previous), ("Next", following)]:
            if item:
                pager.append(f'<a href="{relative(route(item["path"]), current)}"><small>{label}</small>{html.escape(item["title"])}</a>')
        words = len(re.findall(r"\b[\w’-]+\b", raw))
        minutes = max(1, round(words / 220))
        title = html.escape(page["title"])
        document_title = title if page["title"] == manifest["title"] else title + " · The Rage Fieldbook"
        output = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="Practical methods for working with AI, skills, and building systems. A living fieldbook from Marc / NeuralYogi and Rage Industries.">
  <title>{document_title}</title>
  <link rel="canonical" href="{manifest['site_url']}{current}">
  <link rel="stylesheet" href="{relative('reader.css', current)}">
  <script defer src="{relative('reader.js', current)}"></script>
</head>
<body>
<a class="skip" href="#main">Skip to reading</a>
<header class="masthead"><a class="wordmark" href="{relative('index.html', current)}"><span class="stamp" aria-hidden="true">R</span><span>The Rage Fieldbook<small>Working with AI, keeping the understanding.</small></span></a><a class="repo" href="{manifest['repository']}">Source on GitHub ↗</a></header>
<div class="layout">
<aside><details class="contents" open><summary>Browse the fieldbook</summary><div class="nav-inner"><label for="chapter-search">Find a chapter</label><input id="chapter-search" type="search" placeholder="Skills, evidence, interfaces…" autocomplete="off"><nav aria-label="Book contents">{''.join(navigation)}</nav><p class="nav-note">By Marc / @NeuralYogi<br>From Rage Industries</p></div></details></aside>
<main id="main" tabindex="-1"><div class="reading-meta"><span>Living edition · 0.1</span><span>{minutes} min read</span></div><article>{body}</article><nav class="pager" aria-label="Reading sequence">{''.join(pager)}</nav><footer>Written from the work. Kept open to correction.<br><a href="{relative(route('ACKNOWLEDGMENTS.md'), current)}">Inspiration &amp; credit</a> · <a href="{relative(route('docs/publication.md'), current)}">Publication boundary</a> · <a href="{manifest['repository']}/blob/main/{source}">Read this page on GitHub</a></footer></main>
</div>
</body></html>'''
        target = OUTPUT / current
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output)
    print(f"Built {len(pages)} declared pages into _site/; no source directories were copied.")


if __name__ == "__main__":
    main()
