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

For a public book, separate two jobs. Research may use authorized private material to discover general questions. Publication uses an explicitly selected set of public sources and original abstractions. A private reviewer should return patterns without private project identifiers in the publication candidate. The editor still reviews that candidate; an instruction to omit secrets is not a technical access boundary.

This edition used three read-only discovery assignments: public owned projects, narrow private overviews, and shared repositories. Each returned coverage and limits. The publication was then assembled in a fresh destination from selected public sources, with private notes kept elsewhere. A separate source review and private-boundary review checked the assembled result before publication. That is a description of this editorial workflow, with no controlled speedup or completeness-of-implementation-audit claim.

Use narrower permissions or isolated environments when access itself needs enforcement. A child prompt describes the assignment; the runtime determines what the child can actually reach.

## A practice to try

Delegate two independent read-only questions about the same public project. Ask one reviewer to explain its stated contract and the other to find the evidence for that contract. Have the parent compare the two and identify the smallest remaining experiment. This produces a useful synthesis without competing edits.
