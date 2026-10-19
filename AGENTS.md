# Fieldbook maintenance

This is a public book repository. Treat the checked-in files and full Git history as publishable.

- Keep private research, inventories, checkouts, conversations, endpoints, credentials, and unpublished project details outside this repository.
- Write original explanations. Use anonymous-accessible public sources for concrete project claims; label fictional fixtures.
- An owner-supplied account may be published within the scope authorized for the book. Label it as reported experience, keep its limits visible, and publish no private transcript or inferred implementation details.
- Preserve authorship and evidence limits. A source check is not a runtime test; an author's reported result is not independent reproduction.
- Keep Corben Sorenson and The ASI Stack credited in the README and acknowledgments.
- New reading pages belong in `book.json`; new tracked files require an explicit entry in `public-files.txt`.
- Run `python scripts/source_catalog.py --check`, `python scripts/validate.py`, `python scripts/build.py`, and `git diff --check` before publishing changes.
- Check the exact diff and generated artifact. Pattern scans supplement editorial review.
- This repository describes existing skills. It does not maintain or distribute a private skill collection.
