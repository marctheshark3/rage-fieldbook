# Choose how much freedom to give an agent

Give an agent enough authority to finish the assigned work, with a clear point for decisions that still belong to you. The useful boundary depends on the task, the evidence available, and the consequence of the next action.

The assignments below are fictional examples. They extend the [reading-digest walkthrough](brief-to-handoff.md) to show how an instruction changes as the work becomes clearer. They are editorial guidance, not a test of a host's permission controls.

## Ask for a proposal when direction is still open

Suppose you want a reading note but have not chosen its shape:

> Using only the supplied titles and states, show two short approaches: a plain unread list and a note inviting discussion. Explain the decision each makes about the reader's next action. Return drafts for review.

The agent has room to create useful differences. The person still chooses which direction serves the group. A checkpoint helps here because an unresolved preference determines the next substantial work.

Judge the alternatives by what they let someone do. A longer list of cosmetic variations may add review work without helping the choice. Once a direction is accepted, carry that choice into the implementation brief.

## Allow implementation when the result is inspectable

After choosing the plain list, the assignment can be more autonomous:

> Update the local digest program and its checks so only `unread` entries appear. Preserve input order, titles, IDs, and the original CSV. Handle the empty result explicitly. Choose the implementation details, run the relevant checks, and return the change and output. Keep the work within the program and its tests.

This permits the agent to edit, run checks, and repair failures within the assignment. It can decide the internal expression or organize a small helper without asking the person to approve each step. The expected output and preserved behavior make those decisions reviewable.

The current brief, project guidance, and earlier authorization all matter. Continue work already authorized within that scope. If an additional action needs a decision, name the change in consequence that makes the decision necessary.

For example, adding a missing empty-state check serves the assignment. Replacing the reading list with data from an external account introduces a different source, access question, and task. The existing local brief does not establish what that new work should do.

## Put review beside a consequential commitment

A checked local digest can still need a publishing decision. When publication has not been authorized, give the agent preparation work it can complete:

> Prepare the final note for the reading group's announcement space. Show the exact text, intended destination, and audience, with any missing facts identified. Return that reviewable candidate; publication will be a separate decision.

The checkpoint now has a concrete object. The person can assess what will be shared and where it will go. Preparing the draft and checking its facts should happen before asking for that decision.

If the person already authorized posting the reviewed note to the named destination, carry out that scope without reopening the same approval merely because drafting took several steps. A changed audience, new claim, or materially different action can require a new decision. Keep the reason visible.

A useful approval request identifies the artifact, the action, and the instruction that requires the decision. Vague requests such as “May I continue?” make it difficult to understand what remains unresolved.

## Give ongoing work an operating agreement

A repeating task needs more direction than a one-time request. If the reading group later wants an ongoing digest, establish:

- The authoritative input and how the agent can access it.
- The cadence or event that starts work.
- The permitted actions, including whether it may draft, publish, or notify.
- The check that establishes a useful result.
- The limit on work, retries, and cost.
- The condition that stops the loop and the place its state is reported.

For a fictional initial trial, the agreement could be: inspect one approved input on each of three scheduled runs, prepare a draft when unread entries exist, preserve the source, and report missing or unknown states instead of guessing. Posting remains a separate decision in that trial.

This is an example agreement, not an automation installed by the book. A real recurring task also needs runtime scheduling, access, and reporting that match the agreement. Prompt text can describe a boundary; the available tools and runtime determine which access controls can enforce it.

Review the first returned artifacts before expanding an ongoing job. A loop that repeatedly returns the wrong digest needs a better observation or procedure before more frequency will help.

## Use checkpoints to resolve something

A checkpoint earns its place when it lets the person choose an audience, settle a conflicting requirement, approve a commitment, or inspect an uncertainty before it becomes expensive to undo.

Routine details can stay with the agent when they fall inside the accepted brief. Too many checkpoints can turn the person into a relay for decisions the assignment already delegated. Too few can let an unresolved choice become an external action before anyone examines it.

For each checkpoint, name what the person will receive and what they will decide. “Choose between these two drafts” is actionable. “Review progress” needs a more specific artifact or question.

## Change the agreement when the work changes

If a missing source blocks the task, the agent should return what is unavailable and which next action would resolve it. If a tool fails, distinguish that execution failure from a decision the person has not made. The [recovery guide](when-the-agent-gets-stuck.md) shows how to bound the next investigation.

Record changed scope in the current [work brief](../templates/work-brief.md). Keep continuing preferences in [context](teach-taste.md), and keep the accepted outcome and evidence in the handoff. That lets the next session continue with the same authority and limits instead of reconstructing them from ambiguous progress updates.

For your next task, write one sentence for each: what the agent may decide, what observation will establish completion, and which remaining action needs your judgment. Then give it room to finish the work those sentences authorize.
