# What to add next

The book teaches a basic working loop: choose a useful task, brief it, inspect an attempt, correct a miss, and carry the current decision forward. Seven walkthroughs and worked chapter examples make that loop concrete. The author introduction connects Marc's public writing identity, NeuralYogi, with the engineering work at Rage Industries. The next investigations should add evidence that these teaching exercises cannot supply on their own.

## What the editorial review changed

The opening needed to explain its author and audience before asking readers to follow unfamiliar projects. The [README](README.md) now introduces Marc from his public site and writing, states what a first pass should teach, and gives a short route through one complete task. That reading route helps navigation; the additions below develop missing substance in the existing chapters.

- **Starting knowledge:** [When to use AI](chapters/00-when-to-use-ai.md#know-which-part-is-doing-the-work) now distinguishes a model, agent, tool, context, skill, and artifact through one reading-list example. A reader can identify what their session needs before asking it to act.
- **Delegation into a decision:** [Subagents](chapters/04-subagents.md#reconcile-two-returns-into-one-decision) now includes two constructed returns, an acceptance error, uncovered behavior, and a parent handoff. The reader can reconcile evidence rather than count agreeing reviewers.
- **A current context record:** [Context and memory](chapters/05-context-and-memory.md#build-a-small-notebook-with-a-current-decision) now supplies a fictional notebook with sources, an observation, decisions, an open question, and a superseded room choice. The [context brief](templates/context-brief.md#keep-one-decision-current) adds a reusable decision record. The reader can distinguish a changed plan from evidence that a draft was actually changed.
- **Freshness through recovery:** [Honest interfaces](chapters/06-honest-interfaces.md#write-the-state-changes-before-drawing-the-screen) now follows a fictional count through expiry, an old response, failure, and a fresh zero. It specifies the human and agent returns and identifies checks a real implementation still needs.
- **Complete work in a comparison:** [Local and remote AI](chapters/08-local-and-remote-ai.md#read-a-comparison-through-to-acceptance) now works through invented setup, draft, review, repair, and acceptance times. The reader can account for the whole task and exclude a route that violates the data boundary before comparing speed.

The gear story remains in its field note, with shorter references from the opening and context chapter. Repeating that account does less teaching work than showing how to preserve and retrieve a current decision. Existing historical essays retain their wording.

## Where substance is still thin

[Skills](chapters/03-skills.md) and [Improve a skill after a miss](walkthroughs/improve-a-skill.md) teach procedural design, but there is no executed agent study showing discovery and use across fitting, wrong-trigger, and missing-input cases. The new delegation and notebook examples are also authored exercises. A reader can practice the decisions; the book cannot yet show measured transfer to a new agent session.

[Experiments](chapters/07-experiments.md) and the [research desk](research/README.md) explain how to judge and plan evidence. The pole walkthrough adds a concrete acceptance contract, but there is still no independently executed research comparison in the research section. [From screen to world](chapters/09-from-screen-to-world.md) distinguishes evidence stages without carrying one already-public artifact through an actual physical fit. The local-versus-hosted table supplies arithmetic, not adoption evidence.

Many exercises reuse the small digest or a fictional group plan. That continuity helps a first pass, but it leaves larger, changing tasks underrepresented. The most useful next example would follow a real public task through conflicting inputs, failed attempts, a revised artifact, and a fresh-session handoff, with actual access and execution recorded. More tool descriptions would not fill that gap.

## The direction to keep

- **Explain a decision before cataloging a tool.** Start from what a person needs help doing, when AI is useful, and what an attempt should return.
- **Show how useful context develops.** Include why an example was accepted, what a correction changed, and how the next task can find the current decision.
- **Distinguish taste from procedure.** Put preferences in a relevant brief; turn stable recurring methods into skills when that investment serves the work.
- **Carry the limits with the story.** A reported first-attempt success can teach a method without becoming a claim that all future work will succeed that way.

## Practical additions

The practical additions were developed in this order:

1. **A complete worked example:** [One task, from brief to handoff](walkthroughs/brief-to-handoff.md) includes an original fictional reading-list fixture, an executed baseline failure, and passing revised checks. The session dialogue is constructed.
2. **Recovering when an agent gets stuck:** [When the agent gets stuck](walkthroughs/when-the-agent-gets-stuck.md) explains how to diagnose missing information, choose a bounded next attempt, and preserve a useful restart packet.
3. **Teaching taste through corrections:** [Teach taste through corrections](walkthroughs/teach-taste.md) follows constructed drafts and a scoped preference into another assignment and a new audience. It does not claim a measured context benefit.
4. **Improving an existing skill:** [Improve a skill after a miss](walkthroughs/improve-a-skill.md) offers a fictional revision exercise with cases inside and outside its scope. Its program checks do not substitute for an agent or skill evaluation.
5. **Choosing agent autonomy:** [Choose how much freedom to give an agent](walkthroughs/choose-autonomy.md) provides concrete assignments with useful checkpoints and explicit authority for consequential actions.
6. **Everyday work beyond code:** [Everyday work beyond code](walkthroughs/everyday-work.md) works through fictional writing, document comparison, planning, and research examples with inspectable inputs and limits.
7. **An acceptance brief from the pole:** [Give AI a finish line you can test](walkthroughs/define-success-with-the-pole.md) connects a pinned public sixteen-link protocol and an author-reported release to a constructed AI assignment and fictional evidence cases. The writing is complete; no new controller run or AI-method comparison was performed.

The chapter examples listed above complete the small-notebook writing task and add integration, freshness, and comparison exercises. They add no executed model, subagent, monitoring, or infrastructure study.

## Ready for a focused writing pass

The [research desk](research/README.md) now provides reading notes, a report template, and a [proposed context-position protocol](research/proposals/context-position.md). The [public maintenance skill](.agents/skills/rage-fieldbook/SKILL.md) carries the intake and evidence decisions into future editing sessions. Neither writing a protocol nor checking the skill package executes a research study.

The remaining investigations below need their own source work or execution; the digest fixture and constructed skill revision do not complete them.

- **A complete skill case study.** Follow one public skill from its trigger to an actual task and returned artifact. Include a wrong-trigger case and a missing-prerequisite case. Start with [Option Flow](sources/README.md#option-flow) or [System Observatory](sources/README.md#system-observatory).
- **One bounded subagent investigation.** Execute a split on a public teaching fixture and publish the actual assignments, returns, coverage, disagreements, and integrated answer. The chapter's constructed reconciliation exercise supplies a teaching example; actual delegated behavior and any speed comparison remain untested.
- **A fresh-session context exercise.** The narrower [context-position proposal](research/proposals/context-position.md) is written but unexecuted. A separate packet-versus-no-packet comparison would need its own matched task and review criteria, actual context-access records, conditions, and outputs. The Rage gear account ran neither comparison.
- **A monitor that recovers.** Use a synthetic event feed to examine duplicates, notification failures, and restart behavior. The shared [Nurse Shark Bot](sources/README.md#nurse-shark-bot) offers a documented architecture to learn from; proposed tests need their own execution.

## Needs a new experiment

- **Local and remote task comparison.** Measure complete work, review effort, cost, and recovery alongside latency. The chapter's invented comparison is a worksheet for interpreting the result. [LLM Benchmark](sources/README.md#llm-benchmark) supplies serving measurements, which need a separate task-quality evaluation.
- **A reproducible research walkthrough.** Select one small [Rage JEPA](sources/README.md#rage-jepa) comparison, freeze the protocol, and publish the actual independent rerun. Keep failed predictor gates and the classical baseline visible.
- **A real boundary from design to physical fit.** Use an already-public artifact, a narrow fit question, and photographs or measurements from that check. CAD and simulation remain separate evidence until then.

## Worth exploring from earlier work

- **Data and labeling choices.** The collaborative [NLP bullying-detection project](sources/README.md#nlp-course-project) documents class imbalance and labeling choices. A retrospective could explain how a dataset changes the question, with shared authorship and historical limits preserved.
- **Task prompts and evaluators.** [VHDLGenAI](sources/README.md#vhdlgenai) suggests a case about keeping a generation prompt separate from the test that judges its result. Historical model outputs need fresh evaluation before current comparisons.
- **From a starter prompt to a project brief.** [AI Project Starter Kit](sources/README.md#ai-project-starter-kit) offers an earlier artifact for discussing how product context becomes an implementation assignment.
- **Community data and model interpretation.** The shared [BLUE](sources/README.md#blue) and [SharkNet](sources/README.md#sharknet) projects can inform a chapter on keeping retrieved facts, generated explanations, and training data distinguishable.

## Editorial upkeep

Keep links and source snapshots current without rewriting historical essays. Invite corrections on evidence and attribution. Add an owner-selected prose and code reuse license if broader reuse is desired. Keep new chapters small enough that a person can review their claims and source boundaries.
