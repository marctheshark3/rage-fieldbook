# 5. Keep context useful

Useful context lets an agent locate the next relevant fact without rereading everything that happened before. A collection of documents helps when it explains what is current, where a statement came from, and which decisions are still open.

Marc's [Rage gear account](../field-notes/rage-gear-context.md) raises the question of carrying taste and earlier judgment alongside technical facts. This chapter develops the practical record a continuing task needs; the field note retains the account and its limits.

Start with a small map. Give the reader the project's purpose, the current working state, the entry points into the implementation, and the next consequential question. Link to the supporting material. A summary should help the reader reach the evidence when detail matters.

## Make taste specific enough to use

An approved example shows an outcome. A reason explains which feature should guide the next one. Keep both when you can. A rejected example can help too, particularly when its failure explains a boundary that an abstract description leaves vague.

Distinguish a lasting preference from a choice made for one occasion. Keep a date and scope with the record. Someone may like a direction for one project and want a different one for the next. Give the current brief a way to override an old preference.

Use the [context brief](../templates/context-brief.md) to collect a few relevant examples and decisions. It should help the agent choose what to inspect, without turning every past exchange into required reading.

[Teach taste through corrections](../walkthroughs/teach-taste.md) follows a fictional editor from a rejected draft to a scoped preference, another input, and a later brief that changes the audience. Its constructed examples keep preference guidance separate from factual support.

## Check what the next agent can actually see

Continuing to use AI for months does not guarantee that a particular run can access earlier work. Context may come from the current conversation, selected files, returned tool results, project guidance, or supported memory features. Different products and sessions can expose different material. The [official customization overview](../sources/README.md#official-context) describes several distinct layers in Codex; other environments have their own mechanisms.

For an important continuing task, identify the brief, references, and current decisions the agent will use. Ask it to report unavailable material. You can check this with a narrow retrieval question before relying on a long task: which approved reference supports this choice, and can the agent actually open it?

The [context research note](../research/notes/context-retrieval.md) connects a published paper to that retrieval question. Its paper results remain historical, source-inspected evidence. A [separate proposal](../research/proposals/context-position.md) describes a possible placement study; no such experiment has been run for this book.

Retaining context also differs from changing the model's trained parameters. In this fieldbook, the practical method is to preserve useful records and make them available for the task. The gear account does not establish which persistence mechanism carried any particular detail.

## Keep different kinds of knowledge distinguishable

A practical notebook separates four things:

- A source records what a document or person said, with its identity and date.
- An observation records what an inspection or experiment established under specified conditions.
- A decision records what was chosen, why, and which alternatives were considered.
- An open question records what would change the next decision and how to investigate it.

These can live in plain files. The distinction matters more than the storage technology. An agent can otherwise turn a proposed design into an established fact by repeatedly summarizing it without its original qualification.

The [System Observatory examples](../sources/README.md#system-observatory) make similar distinctions between documented intent, inferred explanations, observed behavior, and proposed designs. Use those labels when they help someone assess an explanation.

## Build a small notebook with a current decision

Here is a **constructed notebook for a fictional workshop**. The source excerpts, times, inspection, and decisions are authored teaching material. No booking was checked and no agent retrieval trial was run. The exercise shows what each kind of record contributes when a plan changes.

At 09:00, the available booking and draft agree:

```text
S1 — Source — Booking revision 1, received 09:00
Excerpt: "Workshop welcome: Room A, 18:00."

O1 — Observation — Illustrated inspection of invitation draft 1
The draft says "Room A, 18:00". It makes no equipment claim.
This observation concerns draft 1 only.

D1 — Decision — Accepted at 09:10, based on S1
Use Room A and 18:00 in the attendee invitation.
Reason: these are the details in the supplied booking.

Q1 — Open question
Is a projector included? S1 does not say.
Next check: obtain an equipment confirmation for this booking.
```

At 11:00, a correction arrives. Preserve the old records and add the change:

```text
S2 — Source — Booking revision 2, received 11:00; replaces S1
Excerpt: "Room B replaces Room A. The welcome remains at 18:00.
Projector availability still needs confirmation."

D2 — Decision — Accepted at 11:05; supersedes D1
Use Room B and 18:00 in the attendee invitation, based on S2.
Reason: the corrected booking explicitly changes the room.
Scope: this workshop's attendee invitation.
Revisit if: another booking correction arrives.
```

The current index now points to **S2 and D2**. Mark D1 as superseded by D2; keep it available as history. O1 still accurately describes the old draft. It supplies no evidence that the invitation has been corrected. Q1 remains open: a room correction did not confirm the equipment.

That is the job of the notebook. A source can change, an old observation can remain true about its artifact, a decision can be replaced, and a question can survive all three. Flattening them into “the workshop is ready” would lose the next useful action.

A small current-state packet can now say:

> Use D2, supported by booking S2: Room B at 18:00. D1 and S1 are historical. The last inspected invitation, draft 1, still names Room A; revise it and inspect the new draft. Projector availability remains Q1. The available packet contains S1, S2, O1, D1, D2, Q1, and draft 1.

The record labels can be headings in one document. Separate files become useful when records grow or different people own them. Give a real source an exact location and revision or capture identity, and give an observation the identity of the artifact inspected. The labels above identify only this fictional exercise.

Before a new assignment, try this retrieval question:

> Which room should the invitation use, what supports that choice, which existing artifact still needs correction, and what equipment fact remains unconfirmed?

The expected answer is Room B from D2/S2, a correction to draft 1 from O1, and the unresolved projector question Q1. An answer citing D1 as current exposes a retrieval or guidance problem. A correct answer still needs a suitable revised invitation; retrieving the decision does not establish that the work was done.

For your own notebook, choose one changing decision and make its replacement explicit. Use the [context brief](../templates/context-brief.md#keep-one-decision-current) for the active record. Retain enough history to explain the change while making the current path easy to find.

## Give a handoff a current state

A useful handoff says what changed, what evidence supports the change, what remains uncertain, and what to do next. Include the revision or artifact identity when continuing against a moving source. A branch name alone does not preserve the exact state that was inspected.

Preserve a contradiction until it is resolved. If a new measurement disagrees with an old note, record the conditions of both. A cleaner summary that silently discards the disagreement can make future work harder.

## Leave the next session better informed

At the end of useful work, record what was accepted, why it worked, the correction that should persist, and the next unresolved question. Link to the artifact rather than repeating it. Then choose where the correction belongs: the current brief, a preference record, project guidance, or an existing skill.

Keep context relevant and selective. More material can introduce contradictions, distract from the task, or carry information into a setting where it does not belong. A brief built for a private task and a public teaching example can use different source sets. Access to a record does not establish permission to publish it.

If later work keeps missing the same preference, inspect the reference and whether it was actually available. If it keeps repeating the same procedural mistake, inspect the workflow. Those failures call for different repairs.

## Treat training data as a separate artifact

The shared community project [SharkNet](../sources/README.md#sharknet) documents domain examples, model training, inference, and experiment tracking. It is a useful prompt for a broader distinction: notes that help a person or agent navigate a project are not automatically suitable training data.

Dataset work needs its own account of origin, permission, labeling, exclusions, and evaluation. The public README explains the project's intended workflow; this book has not verified its dataset quality or trained a model from it. Shared projects retain shared authorship.

## A practice to try

Take a long project summary and mark each sentence as source, observation, decision, or open question. Find one statement whose basis is unclear. Replace it with a link, an explicit inference, or a question to investigate. Then write a handoff that would let a fresh reader take the next useful step.
