# 5. Keep context useful

Useful context lets an agent locate the next relevant fact without rereading everything that happened before. A collection of documents helps when it explains what is current, where a statement came from, and which decisions are still open.

Start with a small map. Give the reader the project's purpose, the current working state, the entry points into the implementation, and the next consequential question. Link to the supporting material. A summary should help the reader reach the evidence when detail matters.

## Keep different kinds of knowledge distinguishable

A practical notebook separates four things:

- A source records what a document or person said, with its identity and date.
- An observation records what an inspection or experiment established under specified conditions.
- A decision records what was chosen, why, and which alternatives were considered.
- An open question records what would change the next decision and how to investigate it.

These can live in plain files. The distinction matters more than the storage technology. An agent can otherwise turn a proposed design into an established fact by repeatedly summarizing it without its original qualification.

The [System Observatory examples](../sources/README.md#system-observatory) make similar distinctions between documented intent, inferred explanations, observed behavior, and proposed designs. Use those labels when they help someone assess an explanation.

## Give a handoff a current state

A useful handoff says what changed, what evidence supports the change, what remains uncertain, and what to do next. Include the revision or artifact identity when continuing against a moving source. A branch name alone does not preserve the exact state that was inspected.

Preserve a contradiction until it is resolved. If a new measurement disagrees with an old note, record the conditions of both. A cleaner summary that silently discards the disagreement can make future work harder.

## Treat training data as a separate artifact

The shared community project [SharkNet](../sources/README.md#sharknet) documents domain examples, model training, inference, and experiment tracking. It is a useful prompt for a broader distinction: notes that help a person or agent navigate a project are not automatically suitable training data.

Dataset work needs its own account of origin, permission, labeling, exclusions, and evaluation. The public README explains the project's intended workflow; this book has not verified its dataset quality or trained a model from it. Shared projects retain shared authorship.

## A practice to try

Take a long project summary and mark each sentence as source, observation, decision, or open question. Find one statement whose basis is unclear. Replace it with a link, an explicit inference, or a question to investigate. Then write a handoff that would let a fresh reader take the next useful step.
