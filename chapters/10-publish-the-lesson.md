# 10. Publish the lesson

A useful public explanation gives someone enough context to understand an idea, assess its evidence, and try a related method. That can often be done with public examples and original teaching fixtures while private source, operations, and conversations stay private.

## Build a fresh publication set

Start a new destination with an explicit list of allowed files. Bring in the prose and artifacts chosen for publication. Keep research notes, inventories, source checkouts, logs, and private drafts outside that destination.

This matters for Git history as well as the current file tree. Removing a file from the latest revision does not remove it from earlier commits. A fresh repository makes the publication history easier to inspect from its first commit.

Use public sources as the evidence for concrete examples. Check anonymous access to the exact page or file you intend to cite. If a private example suggests a good question, find a public analogue or construct a fictional teaching case and label it accordingly. A fictional fixture can explain a mechanism without claiming that it reproduces a private system.

## Generalize the question, then write anew

Suppose authorized research reveals a recurring problem with stale information. The public lesson can explain observation time, expiry behavior, and a small fictional interface. It does not need the private repository name, service address, user data, or incident transcript.

Removing identifiers from a distinctive story may still disclose the underlying work. Prefer a new example that carries the general mechanism. Do not publish private metrics as unattributed evidence for a public claim.

The [public essay about a week of building](../essays/README.md#weekly-practice) connects observations and next checks across several domains. It offers a model for writing from the decisions and evidence, with the remaining questions visible.

## Review authorship and rights

Credit the person who inspired the format, the authors of ideas you build on, and the contributors to shared projects. A fork is evidence of interest and perhaps a place of contribution; it does not establish authorship of the upstream work.

The [acknowledgments](../ACKNOWLEDGMENTS.md) credit Corben Sorenson's living-book idea. The [source catalog](../sources/README.md) identifies public project snapshots. Linked repositories retain their own rights and limitations. This book does not copy their implementation or grant new rights over it.

## Use checks that match the publication

Before publishing, inspect the exact tracked files and history. Check links, local paths, credentials, private URLs, source identity, and whether a sentence overstates its evidence. A pattern scanner can catch common accidents; it cannot decide whether a paragraph reveals confidential work.

This repository's reader builds from `book.json`, and its validator checks the declared publication files. The initial publication also used a separate private inventory scan outside the repository. That private inventory is intentionally absent from both the source and generated site.

## A practice to try

Write one page from an already-public project: the question, a consequential decision, the observation, the limit, and the next experiment. Use the [publication note](../templates/publication-note.md) to record where every concrete example came from. Publish the explanation when a reader can follow it without needing access to private evidence.
