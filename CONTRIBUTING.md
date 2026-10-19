# Contributing

Useful contributions improve a method, correct a source, clarify a limitation, or add an already-public example with inspectable evidence.

Open an issue for a factual correction or a proposed chapter. Describe the question a reader could answer after the change. For a contribution to prose, use fresh writing and include the source and its actual support boundary. Do not paste private work, private repository links, confidential examples, credentials, customer information, or proprietary source into an issue or pull request.

Use the [Fieldbook skill](.agents/skills/rage-fieldbook/SKILL.md) for the recurring editorial workflow. For papers, proposals, and original reports, follow the [research guide](research/README.md) and keep publication status separate from reproduction status. A useful question or revised explanation can merit an addition before a complete chapter does.

When changing a chapter:

1. Check the relevant public sources and their revisions.
2. Keep reported results, your own observations, and recommendations distinguishable.
3. Add or update the source catalog when relying on a new source.
4. Add new reading pages to `book.json` and all new tracked files to `public-files.txt`.
5. Run `python scripts/source_catalog.py --check`, `python -m unittest discover -s tests -v`, `python scripts/validate.py`, `python scripts/build.py`, `python scripts/validate.py` again for the generated artifact, and `git diff --check`.
6. Inspect the final publication files and generated reader before merging.

The manifest and publication list are deliberate boundaries. Never solve a validation failure by broadly allowing a research directory or copying an entire source repository.

The source catalog is data in `sources/public-sources.json`; regenerate its readable page with `python scripts/source_catalog.py`. Public URLs should be anonymously accessible. Document a verification limit instead of treating an authenticated read as a public-access check.

Existing essays are historical publications. Preserve their original wording and date, or clearly identify an edited adaptation. New findings belong in a new note or an explicit correction.

Contributors retain rights in their contributions. Only submit material you may publicly share. This edition has no blanket reuse license; see [rights](RIGHTS.md).
