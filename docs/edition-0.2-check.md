# Context edition check record

Checked on 19 October 2026 UTC before publishing the context edition.

## What changed

The book now opens with choosing when to use AI and the kind of help to ask for. The skills chapter adds criteria for creating or improving a skill and a guide to where different lessons belong. The context chapter covers taste, earlier decisions, actual access, and corrections. A new context brief supports those practices.

The Rage gear field note records only the account Marc supplied for the book: after about two months of building, he described a first attempt that worked for him and attributed it to accumulated context. It is labeled as an owner account. No private gear source, artwork, original prompt, conversation archive, or production record was imported or inspected for the addition.

## Checks performed

- Source-catalog synchronization, publication allowlist, internal links and anchors, essay capture digests, and common disclosure-pattern checks pass.
- All five existing publication-boundary regression tests pass. No new test fixture was needed for the editorial additions.
- The static reader builds 30 declared pages. The artifact contains 33 files: those pages, two reader assets, and the static-host marker.
- The publication allowlist contains 44 source files. The existing essays remain unchanged, and Corben's attribution remains in the README and acknowledgments.
- The final publication and reader were compared against the separately held private repository identifiers and previously collected narrow overviews. No private full repository identifiers or twelve-word overview matches were found. That inventory and the detailed scan report remain outside the publication.
- The new field note, skills decision guide, edition marker, navigation, and mobile opening page were checked through the collaborative browser at desktop and mobile widths. No horizontal overflow was observed in the checked views.
- The official guidance linked for skill choice, working practices, and customization was opened and its relevant sections read. These pages do not establish the cause of the gear result.

Commands:

```bash
python scripts/source_catalog.py --check
python -m unittest discover -s tests -v
python scripts/validate.py
python scripts/build.py
python scripts/validate.py
git diff --check
```

This revision adds editorial guidance and an owner account. It does not add a new skill package or independently reproduce a project's reported results. Hosted validation and deployment results are available in the repository's Actions tab.
