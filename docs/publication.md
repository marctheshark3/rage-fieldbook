# Publication boundary and first-edition note

The first edition was prepared on 18 October 2026 in Marc's timezone; source capture records use UTC on 19 October. Marc requested a public living book, credit to Corben Sorenson, and subagent discovery across the repository estate while keeping private work private. The name The Rage Fieldbook was selected by Marc.

## What enters this repository

- Original editorial chapters and practical document templates.
- Three Marc-authored essays captured from the anonymously accessible live site.
- Independently written descriptions and links to selected public repositories and official documentation.
- The source catalog, publication allowlist, validation scripts, and static-reader build.

The broader repository inventory, private discovery notes, source caches, and draft material remain outside this repository. Discovery covered repository metadata and selected narrow overview documents. It was not an implementation, security, performance, or scientific audit of every repository. Some overviews were sparse or absent, and forks or external vendor/classroom repositories received metadata classification where a content review would add little to this book.

Private discovery informed general questions and editorial priorities. No private source excerpts, private repository identifiers or URLs, internal release process, unpublished measurements, or operational topology were selected for publication. Concrete project examples in the book point to already-public evidence.

## Evidence language

New chapters are an AI-assisted editorial synthesis. They include original recommendations, fictional examples explicitly marked as such, and descriptions of public sources. They are not a claim that Marc separately line-reviewed every new sentence.

Published essays retain their original first-person voice and historical state. Reproduction preserves their body text, with HTML converted to Markdown and links made absolute. Their public capture records identify the source and body digest. The book does not independently reproduce the scientific, operational, or performance claims in linked projects or essays.

## Checks and their limits

`scripts/validate.py` checks the declared publication files, book navigation, local links, source records, and common accidental disclosure patterns. It also checks tracked files against `public-files.txt` once Git is initialized. The build emits only pages listed in `book.json` and local reader assets. Raw notes and repository inventories are not build inputs.

An additional first-publication review compares the publication tree with a private inventory outside the repository, verifies selected public source access anonymously, and inspects the initial tracked files and history. That inventory is not a public denylist and is never bundled into CI.

Automatic patterns cannot establish that every sentence is free of confidential information. Human-readable source boundaries and an inspection of the exact artifact remain part of publication. Future changes need the same review; these checks do not grant permission to publish new private material.

The initial validation record is recorded in [the release check note](release-check.md). Update it only with checks actually performed.
