# 4. Give subagents bounded assignments

Subagents are useful when several questions can be answered independently. They can explore different parts of a repository, compare public sources, or review a change from different angles. The parent agent still needs to combine the results into one coherent decision.

The [official subagent documentation](../sources/README.md#official-subagents) describes parallel work and the collection of results in the main thread. It also notes the additional model and tool work involved. Parallelism has a cost, so choose it for independence and useful coverage.

## Define the handoff before spawning

A bounded assignment gives the child a question, the material it can inspect, the actions it can take, and the result it should return. Include what would count as an unresolved issue. For a read-only review, say so explicitly and keep the scope consistent with the tools and access actually provided.

The [delegation brief](../templates/delegation-brief.md) asks for evidence locations, conclusions, limitations, and coverage. That last part matters in a repository survey. A summary of the interesting findings does not tell you whether the quiet repositories were checked.

For a fictional survey of thirty repositories, divide the inventory into three disjoint groups of ten. Each reviewer returns a row for every assigned repository: overview inspected, empty, excluded, or failed. The parent reconciles those rows against the original inventory before describing the survey as complete. An inventory pass establishes breadth; it does not establish a deep audit of every implementation.

## Give writes an owner

Independent research can share a checkout when no one changes it. Implementation needs a clearer arrangement. Give each task separate files or a separate checkout and make one agent responsible for integration. Explain the shared contract before the children begin.

Parallel work becomes expensive when two children each redesign the same boundary. A short dependency map can show which questions must be settled first and which can proceed immediately. Keep tightly dependent steps in one thread when their handoffs would cost more than the parallelism saves.

## Review the synthesis

Several agents can repeat the same mistaken assumption. Agreement is useful only alongside the evidence each agent actually inspected. Ask the parent to preserve disagreements, missing coverage, and important differences in conditions.

## Reconcile two returns into one decision

Consider a **constructed delegation exercise** using the fictional [reading digest](../walkthroughs/brief-to-handoff.md). These assignments and returns are authored examples, not logs of subagent execution. The parent supplies the unread-only brief, the four-row CSV, and the illustrated baseline output. It keeps the program unchanged.

Give the reviewers different questions:

> **Reviewer A:** Inspect the brief and CSV. Return the eligible IDs, excluded IDs with their reasons, and any input ambiguity. Cover all four rows. Keep this pass read-only.
>
> **Reviewer B:** Compare the supplied baseline output with the brief and input. Return each inclusion mismatch and distinguish command completion from task acceptance. Keep this pass read-only; identify any behavior the supplied output cannot establish.

Suppose A returns: “Include `r1` and `r3`; exclude `r2` because it is read and `r4` because it is archived. All four rows accounted for.” B returns: “The command exited successfully and all four valid input records appear, so the digest passes.”

The parent can now reconcile the claims against the actual artifacts:

| Question | Evidence in the supplied packet | Integrated finding |
| --- | --- | --- |
| Which rows qualify? | Brief requests `unread`; CSV gives all four states | A's selection matches the requirement. |
| Does the baseline satisfy it? | Output includes `r2` and `r4` | It fails selection. B checked presence but used the wrong acceptance condition. |
| What happens with no unread rows? | This packet contains no such output | Uncovered in this split; neither return establishes it. |

Return a correction to B with the mismatched IDs and the governing rule. A second vote is unnecessary to establish what the supplied rows and output already show. If a source is ambiguous, preserve that ambiguity rather than resolving it by counting reviewers.

The parent's useful handoff is:

> Selection fails on the supplied mixed-state input: `r2` and `r4` should be excluded. All four input rows were classified. No-unread behavior remains outside these returns. Next, inspect the walkthrough's existing check record or execute that case, then give one implementation owner the selection correction and both acceptance conditions.

The [full digest walkthrough](../walkthroughs/brief-to-handoff.md#5-verify-against-the-original-expectation) already records the executed program checks. This exercise shows how to account for what a delegated pass actually covered before incorporating that additional evidence. It adds no new execution or speed comparison.

For a real split, write the integration question first: which conclusion will these returns let you make, and who will resolve a missing or contradictory result? If both reviewers must repeatedly ask each other for intermediate findings, keep those dependent steps together.

## Keep the publication boundary in the synthesis

For a public book, separate two jobs. Research may use authorized private material to discover general questions. Publication uses an explicitly selected set of public sources and original abstractions. A private reviewer should return patterns without private project identifiers in the publication candidate. The editor still reviews that candidate; an instruction to omit secrets is not a technical access boundary.

This edition used three read-only discovery assignments: public owned projects, narrow private overviews, and shared repositories. Each returned coverage and limits. The publication was then assembled in a fresh destination from selected public sources, with private notes kept elsewhere. A separate source review and private-boundary review checked the assembled result before publication. That is a description of this editorial workflow, with no controlled speedup or completeness-of-implementation-audit claim.

Use narrower permissions or isolated environments when access itself needs enforcement. A child prompt describes the assignment; the runtime determines what the child can actually reach.

## A practice to try

Delegate two independent read-only questions about the same public project. Ask one reviewer to explain its stated contract and the other to find the evidence for that contract. Have the parent compare the two and identify the smallest remaining experiment. This produces a useful synthesis without competing edits.
