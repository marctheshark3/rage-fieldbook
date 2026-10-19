# The Rage Fieldbook

**Working with AI, keeping the understanding.**

A living fieldbook by Marc / [@NeuralYogi](https://neuralyogi.com), from the work at Rage Industries. It brings together published essays, public projects, and practical ways to build with AI: define the outcome, give agents useful tools, make repeated work into skills, and keep the result inspectable.

**[Read the book](https://marctheshark3.github.io/rage-fieldbook/)** · [Start with a work brief](templates/work-brief.md) · [Public sources](sources/README.md) · [What to add next](ROADMAP.md)

The first edition is a working editorial synthesis, prepared with AI assistance. New chapters offer practices and interpretations; linked project results remain their authors' reported results. This book has not independently reproduced those experiments. The [publication note](docs/publication.md) explains the source boundary and checks.

## Why a fieldbook

The useful part of building with AI is the relationship between an intention, an action, and something we can inspect afterward. A working interface, a failed experiment, a clearer question, and a repeatable procedure can all be useful outcomes. This book follows those connections across software, research, games, and physical interfaces.

Read it as a set of methods to try and improve. Each chapter gives you a concrete way to use the idea, a public example where available, and a boundary on what that example establishes.

## Read in order

1. [Keep the direction](chapters/01-keep-the-direction.md) — what the person needs to own.
2. [Give the agent a feedback loop](chapters/02-the-agent-loop.md) — move from a request to observable progress.
3. [Turn repeated work into skills](chapters/03-skills.md) — preserve a procedure and the judgment around it.
4. [Give subagents bounded assignments](chapters/04-subagents.md) — parallel research, explicit handoffs, one integration owner.
5. [Keep context useful](chapters/05-context-and-memory.md) — separate sources, observations, decisions, and open questions.
6. [Make the interface tell the truth](chapters/06-honest-interfaces.md) — freshness, refusal, and evidence people can inspect.
7. [Keep the experiment honest](chapters/07-experiments.md) — baselines, complete cohorts, and negative results.
8. [Choose where the model runs](chapters/08-local-and-remote-ai.md) — compare complete workflows and their costs.
9. [Cross into the physical world carefully](chapters/09-from-screen-to-world.md) — carry the contract through simulation and observation.
10. [Publish the lesson](chapters/10-publish-the-lesson.md) — share useful knowledge while keeping private work private.

## Read from the essays

Three existing essays are included as text, with their original public URLs and capture records:

- [Outsource the thinking. Keep the understanding.](essays/keep-the-understanding.md)
- [I taught an AI agent to be Player Two](essays/player-two.md)
- [When the source goes quiet, the interface should say so.](essays/when-the-source-goes-quiet.md)

The [essay reading guide](essays/README.md) connects all fourteen essays available when this edition was prepared to the book's themes. Historical essays keep their original claims and limitations; the book does not silently update their results.

## Use it at your desk

Start with the [work brief](templates/work-brief.md), give a parallel reviewer the [delegation brief](templates/delegation-brief.md), and record the result with an [evidence note](templates/evidence-note.md). Before sharing an example, use the [publication note template](templates/publication-note.md).

These are plain documents. They work with whatever agent or editor you use. This repository describes and links existing public skills; it does not bundle a private skill collection.

## Inspiration and credit

The idea for maintaining our own public, evolving book was inspired by **[Corben Sorenson](https://github.com/corbensorenson)** and **[The ASI Stack](https://github.com/corbensorenson/asi-stack-book)**. His project showed a compelling way to keep a book, its sources, open questions, and evidence together as the work develops. Thank you, Corben, for the idea.

The Rage Fieldbook is an original companion to our own work. Corben's manuscript, code, figures, and book structure have not been copied into this repository. This acknowledgment does not imply his review or endorsement. Other projects and collaborators are credited in the [acknowledgments](ACKNOWLEDGMENTS.md) and [source catalog](sources/README.md).

## Build and contribute

The Markdown is the book's source and can be read directly on GitHub. To build the static reader with Python 3.11 or newer:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/validate.py
.venv/bin/python scripts/build.py
.venv/bin/python -m http.server 8000 --directory _site
```

Open the local server on port 8000. The reader has no remote fonts, analytics, or browser dependencies. Its build reads only pages explicitly listed in `book.json`; GitHub Pages receives only `_site/`.

See [contributing](CONTRIBUTING.md), [publication policy](docs/publication.md), and [rights](RIGHTS.md). Public availability of a source does not change its license.
