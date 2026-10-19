# Publication boundary

The first edition was prepared on 18 October 2026 in Marc's timezone; source capture records use UTC on 19 October. Marc requested a public living book, credit to Corben Sorenson, and subagent discovery across the repository estate while keeping private work private. The name The Rage Fieldbook was selected by Marc.

## What enters this repository

- Original editorial chapters and practical document templates.
- Explicitly fictional teaching fixtures and documented local checks.
- Three Marc-authored essays captured from the anonymously accessible live site.
- Independently written descriptions and links to selected public repositories and official documentation.
- The source catalog, publication allowlist, validation scripts, and static-reader build.

The broader repository inventory, private discovery notes, source caches, and draft material remain outside this repository. Discovery covered repository metadata and selected narrow overview documents. It was not an implementation, security, performance, or scientific audit of every repository. Some overviews were sparse or absent, and forks or external vendor/classroom repositories received metadata classification where a content review would add little to this book.

Private discovery informed general questions and editorial priorities. No private source excerpts, private repository identifiers or URLs, internal release process, unpublished measurements, or operational topology were selected for publication. Concrete project claims point to already-public evidence. Owner-supplied accounts are labeled separately and limited to what the owner supplied for the book.

## Evidence language

New chapters are an AI-assisted editorial synthesis. They include original recommendations, fictional examples explicitly marked as such, and descriptions of public sources. They are not a claim that Marc separately line-reviewed every new sentence.

Published essays retain their original first-person voice and historical state. Reproduction preserves their body text, with HTML converted to Markdown and links made absolute. Their public capture records identify the source and body digest. The book does not independently reproduce the scientific, operational, or performance claims in linked projects or essays.

## Owner account in the context edition

Marc asked for a stronger focus on how and when to use AI, when to make skills, and the value of context accumulated through regular work. He supplied the Rage gear experience as his example: after about two months of building, an agent produced a first attempt that worked for him, which he attributed to its context about him and his preferences.

[Two months behind a first attempt](../field-notes/rage-gear-context.md) publishes only that account and original general guidance drawn from it. No private artwork, original prompt, conversation transcript, production records, or implementation was inspected or imported for the note. The account is not independent evidence of causation, a measured success rate, or completion of a wider merchandise operation. The source catalog identifies it as an owner account and links to the published note.

## Practice walkthroughs

The six pages under `walkthroughs/` are original teaching material. The reading-digest example includes a fictional CSV, an authored baseline with a deliberate selection error, a revision, and executable acceptance checks. Its recorded execution establishes the local program behavior under those inputs. It is not a captured agent session, an independently tested skill, a fresh-session context comparison, or a productivity result.

The taste, recovery, skill-revision, autonomy, and everyday-work examples use constructed assignments and editorial decisions. They do not reconstruct Marc's private work or extend the scope of the Rage gear account. The skill-revision exercise describes a fictional procedure in prose. Proposed evaluations remain labeled as proposed.

The fixture source files belong to the explicit publication allowlist. The static reader links to those source files; it does not copy the example directory into the reader artifact.

## Research and the maintenance skill

The [research section](../research/README.md) distinguishes reading notes, proposed protocols, executed reports, and research papers. The first paper note identifies a primary published source inspected for the book. Its experiments have not been independently reproduced here. The context-position proposal has no executed cohort or results. Original commentary and proposed methods do not extend the evidence behind the gear account.

At Marc's request, this repository also ships one public [Fieldbook maintenance skill](../.agents/skills/rage-fieldbook/SKILL.md). It covers editorial intake, research evidence, and repository checks. It contains portable task guidance and agent metadata, with no private context or skill collection. The reader links to its source; the build does not copy the package into the site artifact.

## Checks and their limits

`scripts/validate.py` checks the declared publication files, book navigation, local links, source records, and common accidental disclosure patterns. It also checks tracked files against `public-files.txt` once Git is initialized. The build emits only pages listed in `book.json` and local reader assets. Raw notes and repository inventories are not build inputs.

An additional first-publication review compares the publication tree with a private inventory outside the repository, verifies selected public source access anonymously, and inspects the initial tracked files and history. That inventory is not a public denylist and is never bundled into CI.

Automatic patterns cannot establish that every sentence is free of confidential information. Human-readable source boundaries and an inspection of the exact artifact remain part of publication. Future changes need the same review; these checks do not grant permission to publish new private material.

The initial validation record is in [the first-edition check note](release-check.md). The context edition has a [separate check record](edition-0.2-check.md). Update these only with checks actually performed.
