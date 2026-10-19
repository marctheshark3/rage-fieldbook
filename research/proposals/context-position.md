# Where does the current decision sit?

*Research proposal · Not executed, frozen, or preregistered · No results.*

## Question and intended claim

Does the position of one explicit, fictional decision record affect a model's ability to retrieve it from a supplied brief under a fixed task and runtime? The intended outcome is a bounded account of retrieval under those conditions. It would not establish the value of a months-long collaboration, persistent product memory, personal taste, or performance on a complete building task.

The [context reading note](../notes/context-retrieval.md) motivates examining placement. This is an original Fieldbook proposal, not a reproduction of that paper's data or protocol.

## Task packet

Prepare twelve fictional cases. Each contains thirteen short, clearly separated records with unique IDs, one task question, and a known answer. One record gives the current decision for the requested project; the twelve distractors describe other projects with different IDs. Keep every title, decision, and explanation invented and publishable.

For example, the target record could be:

```text
Record D7
Project: garden-reading-list
Decision: include unread entries only
Reason: read and archived entries should not appear in the next-reading list
```

The question asks for the project's decision, its record ID, and the supporting sentence. It contains the project identity but does not reveal the decision or target record ID.

Before running, construct the actual twelve-case packet and expected answers, review them independently of model outputs, and record their hashes and revision. The example above is an illustration; the complete task packet does not exist yet.

## Conditions and comparison

For each case, place the target record first, seventh, or thirteenth. Preserve the exact records, distractor order, question, and formatting across its three variants; move only the target record. Keep the question after the records in every condition. Record the complete serialized input and its length so accidental changes remain visible.

Use the same chosen model version and exposed settings, tool availability, output budget, and task instructions in all conditions. Run each attempt in a new session without earlier task history. Record the runtime's visible configuration and mark unobservable state as unknown. Do not publish private or hidden host instructions.

Randomize and save the run order before execution so conditions are interleaved. If the provider or runtime changes materially mid-study, pause and document it; restart a separately identified cohort rather than silently combining configurations.

## Planned cohort and limits

The proposed main cohort is twelve cases × three positions × three fresh attempts: **108 attempts per selected model**, or 36 attempts per position. These are repeated observations on twelve cases, not 108 independent tasks. Choose the actual environment and a total cost/time cap before authorizing execution. No provider calls are started by preparing this document.

Keep the packet size fixed for this first study. If all positions succeed, that result applies to these short packets; it would not establish robustness at larger context lengths. Investigating length, conflicting decisions, tools, or downstream task quality needs another protocol or an explicitly revised design before execution.

## Scoring and failure accounting

Ask for a short structured answer with the decision, record ID, and supporting sentence. Freeze the output schema and scorer before the first scored attempt. Score exact expected decision and ID separately from whether the cited sentence occurs in the target record. Keep raw outputs available to review semantic or formatting disagreements.

Count invalid outputs, refusals, timeouts, and transport failures in the attempt ledger. Report them separately from incorrect retrieved answers and from the total scheduled cohort. Do not silently replace failures with successful retries. If a retry policy is later chosen, retain the first attempt and report initial and recovered outcomes separately.

Report counts per condition and per case before choosing a statistical summary. A reviewer should be able to see whether an apparent effect comes from one difficult case. Any uncertainty estimate must respect repeated attempts on the same cases; do not treat them as independent case samples.

## Evidence to retain

Keep the frozen protocol, case and expected-answer identities, run order, model/runtime identifiers, supplied prompts, returned outputs, timestamps, usage/cost records when available, scorer version, attempt ledger, and exclusions with reasons. Publish only reviewed, synthetic task material and permitted outputs. Separate a paper's quoted material from our own fictional records.

Capture a failed or aborted run as a result of executing the protocol, with its limit. If no completed cohort is available, say so rather than presenting a favorable example as the study.

## Results and next decision

**Results: none.** The packet, scorer, execution environment, and budget remain to be prepared and approved for a future study. No effect size, success rate, model ranking, or causal explanation is claimed.

If the study is requested, first review whether this retrieval question is worth the planned work. Complete and freeze the missing artifacts, execute the bounded cohort, and write a report using the [research template](../../templates/research-note.md). Connect any resulting practice back to the actual conditions and unresolved questions.
