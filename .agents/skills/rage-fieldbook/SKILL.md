---
name: rage-fieldbook
description: "Maintain The Rage Fieldbook: choose, write, source, and validate additions to its chapters, walkthroughs, field notes, and research. Use for this book's editorial and release work; unrelated essays and general research use their own workflows."
---

# Rage Fieldbook

Work in the Fieldbook checkout identified by the session. Confirm its identity
from `README.md` and `book.json`, inspect Git status, and read `AGENTS.md` before
editing. Preserve work already in progress. Paths below are relative to that
checkout, including when this skill is installed elsewhere.

## Decide whether and where to add something

Read the relevant existing pages and `ROADMAP.md`. Name the reader's next useful
decision, the evidence available, and the smallest addition that would help.

| Material | A useful destination |
| --- | --- |
| A correction or clearer explanation of an existing decision | Revise its current page; preserve historical reprint wording. |
| A reusable practice missing from the book | A chapter, with an inspectable outcome and a practice to try. |
| A bounded task with inputs, attempts, review, and artifacts | A walkthrough; distinguish constructed dialogue from executed behavior. |
| An owner-supplied experience | A field note within the supplied publication scope, labeled as reported. |
| A published paper that informs a practical question | A research reading note, after inspecting its primary source. |
| A promising question without executed evidence | A research proposal or roadmap item, with results explicitly pending. |
| An executed study with an auditable protocol and outcomes | A research report with methods, comparisons, all attempts, and limits. |
| A useful one-off project update | An essay or project link; add a book treatment when it teaches a reusable decision. |

Prefer improving an existing page when its question and audience are the same.
A new tool, release, or impressive result alone is not a reason for a chapter.
Keep unsupported ideas as questions. Routine maintenance does not authorize
new recurring work, provider experiments, or changes to another repository.

## Match the claim to the evidence

Use `docs/publication.md` and the source catalog as the publication boundary.
Read primary public sources for concrete claims. Record exact versions and what
was actually inspected. Keep source access, program execution, reported
experience, independent reproduction, and interpretation distinct.

For paper notes and original studies, read `research/README.md` and use
`templates/research-note.md`. Preserve authors, publication/review status,
methods, comparison, negative results, and the limit on transfer to our work.
A proposed experiment has no results. A source-backed summary is not a rerun.
Keep research materials outside the public tree until deliberately selected;
add only the approved explanation and publishable artifacts.

Keep Marc's gear account within its recorded scope. Preserve Corben Sorenson
and The ASI Stack's README and acknowledgment credit. This skill maintains the
book; it does not package private project context or another skill collection.

## Integrate a reviewable change

Write original prose in the book's practical voice. Start from the question,
connect evidence to the decision it supports, and give the reader an action to
try. Label fictional inputs and authored dialogue at the page's entry point.
Keep measured results next to their conditions and limitations.

Add every new file explicitly to `public-files.txt` and every new reading page
to `book.json`. Link it from the relevant chapter or README. Update the roadmap
to distinguish completed writing from unperformed investigations. When adding
a source, edit `sources/public-sources.json` and regenerate its readable catalog
with `python scripts/source_catalog.py`.

Run the repository's required checks using its Python environment:

```bash
python scripts/source_catalog.py --check
python -m unittest discover -s tests -v
python scripts/validate.py
python scripts/build.py
python scripts/validate.py
git diff --check
```

Inspect the exact diff, including new files, and the generated reader. For a new
page or changed navigation, check the relevant desktop and phone-width views.
Never broaden the allowlist to silence an error or import a research directory.

Return the changed pages, the evidence and checks actually obtained, unresolved
questions, and the Git/publication state. Use the repository's current review
workflow for an authorized release; otherwise leave a concrete reviewable
candidate. A book-edit request alone does not authorize deployment to another
site. If a site link is requested, inspect that site's own source and rules and
use the reader URL declared in `book.json`.
