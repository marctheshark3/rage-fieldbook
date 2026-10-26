# The Rage Fieldbook

**Working with AI, keeping the understanding.**

Marc is an independent builder working across AI systems, software, and physical interfaces under the name [Rage Industries](https://neuralyogi.com/work/). He writes as [@NeuralYogi](https://neuralyogi.com/). This fieldbook turns decisions from that work into methods you can try: choose a useful job for AI, give it enough context and freedom, inspect the result, and preserve what you learn.

**[Read the book](https://marctheshark3.github.io/rage-fieldbook/)** · [When to use AI](chapters/00-when-to-use-ai.md) · [Start with a work brief](templates/work-brief.md) · [Sources and accounts](sources/README.md) · [What to add next](ROADMAP.md)

This is a working editorial synthesis, prepared with AI assistance. Chapters offer practices and interpretations; linked project results and owner accounts keep their evidence boundaries. This book has not independently reproduced those experiments. The [publication note](docs/publication.md) explains the source boundary and checks.

## Who this is for

Start here if you can ask an AI assistant for help but want a more reliable way to direct and judge its work. You might be writing, comparing documents, building software, or investigating a prototype. You need a task and a way to inspect an attempt. The [opening chapter](chapters/00-when-to-use-ai.md) explains the terms used here; [everyday examples](walkthroughs/everyday-work.md) need no code. The runnable reading-list example uses basic Python, and the later hardware and infrastructure chapters assume more domain knowledge.

By the end of a first pass, you should be able to write an inspectable work brief, review an artifact against it, correct a specific miss, and leave a current handoff. Skills, subagents, experiments, and physical interfaces extend that basic loop when the work needs them. Product setup and installation belong in the linked tools' own documentation.

## Why Marc is writing a fieldbook

NeuralYogi is Marc's public writing identity; Rage Industries names the engineering work presented on the same site. His [public project pages](https://neuralyogi.com/work/) include control simulations, interfaces that expose missing evidence, and a protocol connecting coding-agent events to simulated light and movement. Their stages matter: a concept, a simulator, and a physical product carry different evidence. The [author source records](sources/README.md#marc-public-site) ground this introduction in his public pages.

In [What a week of building with agents actually looks like](https://neuralyogi.com/essays/2026-10-10-what-a-week-of-building-with-agents-actually-looks-like/), Marc connects a game screenshot, a CAD revision, and a code investigation through the question of what result someone can inspect. That gives this book its working perspective: direct a build, look at what happened, and make the next decision from the evidence. The essays supply his first-person account; the chapters develop practices from it.

The reason for a fieldbook is to make that judgment reusable. A project update records what happened once. A fieldbook can explain how to write the next brief, recognize a failure, or carry a useful decision into another session. Marc's [Rage gear account](field-notes/rage-gear-context.md) adds the question of accumulated context: he reported a first attempt that fit his taste after about two months of building with agents. The practical question is how to preserve earlier judgment and make it available when it matters again.

Read these methods as practices to try and improve. A working interface, a failed experiment, a clearer question, and a repeatable procedure can all be useful outcomes. Each needs a record that lets someone assess what it establishes.

## Finish one small task first

1. **Choose and brief it.** Read [When to use AI](chapters/00-when-to-use-ai.md) and [Keep the direction](chapters/01-keep-the-direction.md). Leave with a few sentences naming the outcome, an important condition, and the evidence you want back.
2. **Make and review an attempt.** Follow [One task, from brief to handoff](walkthroughs/brief-to-handoff.md), or choose a [task without code](walkthroughs/everyday-work.md). Use [the agent loop](chapters/02-the-agent-loop.md) to compare the artifact with the brief. Leave with an acceptance decision and any correction it needs. The [pole exercise](walkthroughs/define-success-with-the-pole.md) helps distinguish failure from missing evidence.
3. **Carry the useful part forward.** Use [the notebook example](chapters/05-context-and-memory.md#build-a-small-notebook-with-a-current-decision) and [context brief](templates/context-brief.md). Leave with the current decision, its supporting source, and the next open question.

You have completed the basic learning loop when another person can assess the artifact and find the current state without reading the conversation. The book does not claim that a particular model or prompt will reliably achieve that for you.

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
- [Give AI a finish line you can test](walkthroughs/define-success-with-the-pole.md) — turn a public pole protocol into an acceptance brief, then classify constructed evidence cases.

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
