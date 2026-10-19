# First-edition check record

Checked on 19 October 2026 UTC for the initial publication. These are checks of this book and its publication boundary; no linked project's benchmarks or hardware were independently rerun.

- **Publication set:** 40 explicitly admitted source files, prepared in a fresh Git repository with no imported project history. Private inventories, caches, overviews, and discovery notes remained outside it.
- **Reader artifact:** 26 declared reading pages, two local reader assets, and a static-host marker. The generated site's 29 files contain no copied source directories.
- **Sources:** 36 selected public records: 20 pinned repository files, 14 live essays, and two official documentation pages. All 20 exact repository files were fetched anonymously and matched their recorded SHA-256 digests. The live essays were fetched in an incognito browser with credentials omitted and returned HTTP 200.
- **Essays:** Three selected public article bodies were converted to Markdown and recorded with file digests. A static capture of an interactive example is explicitly labeled and links to its original controls.
- **Validation:** Source-catalog synchronization, publication allowlist, local navigation and anchors, source-record checks, essay digests, common accidental-disclosure scans, and Git whitespace checks pass.
- **Boundary regressions:** Five tests pass, covering an undeclared draft, a page outside the publication set, a path outside the book, a silently changed historical essay, and representative disclosure patterns.
- **Browser:** Desktop at 1280 × 800 and mobile at 390 × 844 inspected. Chapter search, navigation, current-page state, and mobile menu behavior checked; no horizontal overflow observed at those widths.
- **Independent editorial checks:** Separate agents reviewed source/claim boundaries and private-information exposure. No publication blockers remained after labeling the static essay demo. The private comparison inventory and detailed reports are not part of this repository.

Commands run from the repository:

```bash
python scripts/source_catalog.py --check
python -m unittest discover -s tests -v
python scripts/validate.py
python scripts/build.py
python scripts/validate.py
python scripts/verify_public_sources.py
git diff --cached --check
```

Pattern scans and source-access checks have limited scope. They supplement an editorial inspection; they do not certify the absence of every possible disclosure or validate the scientific claims in referenced work. Hosted build/deployment status is available in the repository's Actions tab.
