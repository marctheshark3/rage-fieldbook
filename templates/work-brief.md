# Work brief

Use this document to give an agent enough direction to choose useful implementation details.

- **Person and outcome:** Who needs what to happen?
- **Kind of help:** Exploration, understanding, implementation, repetition, or critique?
- **Relevant context:** Which prior decisions, accepted examples, and preferences should apply? Link a [context brief](context-brief.md) if useful.
- **Current behavior:** What happens now, and what evidence establishes it?
- **Important conditions:** Which failure, transition, or edge case matters?
- **Preserve:** Which existing behavior, data, or interfaces must survive?
- **Scope:** Which files, systems, tools, and actions are included?
- **Decision owner:** Which decisions can the agent make, and which need the person's judgment?
- **Acceptance:** What observation would show that the outcome was achieved?
- **Return:** What artifact, explanation, and remaining questions should come back?
- **Bound:** What limit on cost, time, actions, or uncertainty applies?

After reviewing the result, preserve the reason it worked or the correction that would help the next similar task. Put stable preferences in context and repeatable procedures in the appropriate workflow.

## Fictional example

People should be able to retry a saved reading-list entry after losing the server reply and still have one entry. Inspect the current Save path and reproduce the lost-reply condition in a local fixture. Preserve existing entries and the visible success/error states. Return the relevant source path, a bounded comparison, and any persistence or concurrency behavior the fixture leaves unmeasured. Keep this first pass read-only.
