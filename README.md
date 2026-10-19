# The Rage Fieldbook

**Working with AI, keeping the understanding.**

A living fieldbook by Marc / [@NeuralYogi](https://neuralyogi.com), from the work at Rage Industries. How to decide when AI will help, work with it effectively, build useful context over time, and recognize when a repeated procedure deserves a skill. Published essays and projects give those practices concrete examples.

**[Read the book](https://marctheshark3.github.io/rage-fieldbook/)** · [When to use AI](chapters/00-when-to-use-ai.md) · [Start with a work brief](templates/work-brief.md) · [Sources and accounts](sources/README.md) · [What to add next](ROADMAP.md)

This is a working editorial synthesis, prepared with AI assistance. Chapters offer practices and interpretations; linked project results and owner accounts keep their evidence boundaries. This book has not independently reproduced those experiments. The [publication note](docs/publication.md) explains the source boundary and checks.

## Why a fieldbook

After about two months of building with agents, Marc described asking one to make Rage gear and getting a first attempt that worked for him. He attributed the fit to the context it already had about him and what he liked. [Two months behind a first attempt](field-notes/rage-gear-context.md) records that account and turns it into a practical question: how do you preserve the judgment from today's work so it can help the next task?

The useful part of building with AI is the relationship between an intention, an action, and something we can inspect afterward. A working interface, a failed experiment, a clearer question, and a repeatable procedure can all be useful outcomes. This book follows those connections across software, research, games, and physical interfaces.

Read it as a set of methods to try and improve. Each chapter gives you a concrete way to use the idea, a public example where available, and a boundary on what that example establishes.

## Read in order

Start with [When to use AI](chapters/00-when-to-use-ai.md): choose the kind of help, recognize when another step would serve the task better, and prepare enough context to evaluate an attempt.

1. [Keep the direction](chapters/01-keep-the-direction.md) — what the person needs to own.
2. [Give the agent a feedback loop](chapters/02-the-agent-loop.md) — move from a request to observable progress.
3. [Turn repeated work into skills](chapters/03-skills.md) — decide when to create one, improve an existing one, or keep a lesson in context.
4. [Give subagents bounded assignments](chapters/04-subagents.md) — parallel research, explicit handoffs, one integration owner.
5. [Keep context useful](chapters/05-context-and-memory.md) — carry taste and decisions forward, check what the agent can access, and keep guidance current.
6. [Make the interface tell the truth](chapters/06-honest-interfaces.md) — freshness, refusal, and evidence people can inspect.
7. [Keep the experiment honest](chapters/07-experiments.md) — baselines, complete cohorts, and negative results.
8. [Choose where the model runs](chapters/08-local-and-remote-ai.md) — compare complete workflows and their costs.
9. [Cross into the physical world carefully](chapters/09-from-screen-to-world.md) — carry the contract through simulation and observation.
10. [Publish the lesson](chapters/10-publish-the-lesson.md) — share useful knowledge while keeping private work private.

## Work through an example

[One task, from brief to handoff](walkthroughs/brief-to-handoff.md) connects a request, context, a flawed attempt, a correction, executable checks, and a packet for the next session. The reading-list project is fictional; its baseline failure and revised checks were actually executed. The teaching dialogue is constructed, and no agent productivity comparison is claimed.

Continue with the question that fits your work:

- [When the agent gets stuck](walkthroughs/when-the-agent-gets-stuck.md) — find what the next attempt needs to establish.
- [Teach taste through corrections](walkthroughs/teach-taste.md) — preserve the reason for a preference and its scope.
- [Improve a skill after a miss](walkthroughs/improve-a-skill.md) — separate a code failure from a proposed procedural repair.
- [Choose agent autonomy](walkthroughs/choose-autonomy.md) — give useful freedom and make checkpoints concrete.
- [Everyday work beyond code](walkthroughs/everyday-work.md) — try writing, comparison, planning, and research without running code.

These are original teaching exercises. Constructed drafts and proposed agent evaluations are labeled separately from the digest's executed program checks.

## Read and investigate research

The [research desk](research/README.md) connects published papers and original investigations to practical questions. Start with [A long brief still needs a retrieval check](research/notes/context-retrieval.md), then inspect [a proposed context-position study](research/proposals/context-position.md). The paper was read; no context experiment has been run for these pages. Use the [research note template](templates/research-note.md) for a reading note, proposal, or executed report.

## Read from the essays

Three existing essays are included as text, with their original public URLs and capture records:

- [Outsource the thinking. Keep the understanding.](essays/keep-the-understanding.md)
- [I taught an AI agent to be Player Two](essays/player-two.md)
- [When the source goes quiet, the interface should say so.](essays/when-the-source-goes-quiet.md)

The [essay reading guide](essays/README.md) connects all fourteen essays available when this edition was prepared to the book's themes. Historical essays keep their original claims and limitations; the book does not silently update their results.

## Use it at your desk

Start with the [work brief](templates/work-brief.md) and a [context brief](templates/context-brief.md) when earlier decisions or taste matter. Give a parallel reviewer the [delegation brief](templates/delegation-brief.md), and record the result with an [evidence note](templates/evidence-note.md). Before sharing an example, use the [publication note template](templates/publication-note.md).

These are plain documents. They work with whatever agent or editor you use. This repository describes and links existing public skills; it does not bundle a private skill collection.

For agents maintaining this book, the public [Rage Fieldbook skill](.agents/skills/rage-fieldbook/SKILL.md) helps decide what belongs here, choose a format, retain evidence limits, and check the reader. Invoke it as `$rage-fieldbook` in a compatible agent with the repository available. The package lives in the repo's `.agents/skills/` directory; the [official skills reference](https://learn.chatgpt.com/docs/build-skills) describes discovery support.

## Inspiration and credit

The idea for maintaining our own public, evolving book was inspired by **[Corben Sorenson](https://github.com/corbensorenson)** and **[The ASI Stack](https://github.com/corbensorenson/asi-stack-book)**. His project showed a compelling way to keep a book, its sources, open questions, and evidence together as the work develops. Thank you, Corben, for the idea.

The Rage Fieldbook is an original companion to our own work. Corben's manuscript, code, figures, and book structure have not been copied into this repository. This acknowledgment does not imply his review or endorsement. Other projects and collaborators are credited in the [acknowledgments](ACKNOWLEDGMENTS.md) and [source catalog](sources/README.md).

## Build and contribute

The Markdown is the book's source and can be read directly on GitHub. To build the static reader with Python 3.11 or newer:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/source_catalog.py --check
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m http.server 8000 --directory _site
```

Open the local server on port 8000. The reader has no remote fonts, analytics, or browser dependencies. Its build reads only pages explicitly listed in `book.json`; GitHub Pages receives only `_site/`.

See [contributing](CONTRIBUTING.md), [publication policy](docs/publication.md), and [rights](RIGHTS.md). Public availability of a source does not change its license.
