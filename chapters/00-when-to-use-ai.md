# When to use AI

Start with the job you want help doing. Sometimes you need possibilities. Sometimes you need a careful explanation, an implementation, or a repeated operation. Sometimes you need a question that helps you decide what you actually want.

## Know which part is doing the work

You can begin with an assistant that accepts text and returns a draft. More capable environments can also read files, use tools, and take several actions. This book uses a few terms to keep those parts distinguishable:

| Term | What it means here | A reading-list example |
| --- | --- | --- |
| Model | The system generating an answer or proposed action from its input | Suggests how to select unread entries |
| Agent | A working loop around a model that can use available tools and inspect their results | Opens the list, edits a program, runs it, and reviews the output |
| Tool | A specific operation the environment exposes | Reads a file or runs a command |
| Context | Material available for the current work | The list, brief, accepted example, and returned tool results |
| Skill | Saved instructions for a recurring kind of job | A procedure for preparing and checking a digest |
| Artifact | Something returned for you to inspect | A draft list, a program change, or a check record |

These are working definitions, not a product feature list. Check what your session can actually access and do. Asking for a screenshot does not give a text-only assistant browser access. Saving a preference does not establish that a future session receives it.

In the [fictional digest walkthrough](../walkthroughs/brief-to-handoff.md), AI can help make the program; the accepted program can then select entries without a model. The person still decides what counts as unread and judges whether the returned list serves the task.

## Choose the kind of help

**Use AI to explore when you can recognize a useful direction before you can describe one precisely.** Ask for a few meaningfully different possibilities and the decisions behind them. React to specific features. That feedback makes the next attempt better informed than a request to make everything better.

**Use AI to understand when it can reach the material that matters.** Ask it to trace a behavior, compare explanations, or define unfamiliar terms beside a concrete example. Keep inspected sources and inferred explanations distinguishable. An explanation becomes more useful when you can follow it back to the relevant material.

**Use AI to build when the desired result can be inspected.** Give it an outcome, useful references, constraints, and room to choose the implementation. A draft, a working interface, or a small experiment gives you something to evaluate. Ask for the artifact that answers the question.

**Use AI for repeated work when the procedure is understood.** Stable transformations, familiar investigations, and consistent deliverables are candidates for a [skill](03-skills.md). First find the procedure that works. Repetition alone does not make an ineffective method worth preserving.

**Use AI to challenge a decision when it can examine the reasons.** Ask which assumption is least supported, which simpler alternative remains viable, and what observation would change the choice. The critique should help you decide what to inspect next.

These are working modes you can switch between. Exploration can become implementation once a direction is clear. A failed implementation can reveal a question that needs an investigation.

[Everyday work beyond code](../walkthroughs/everyday-work.md) applies those modes to an invitation, a document comparison, a setup plan, and a research question. [One task, from brief to handoff](../walkthroughs/brief-to-handoff.md) connects them through a small executable teaching project.

## Notice when another step would help more

A task already handled reliably by a direct tool may need no language model in the execution path. Let a calculator calculate, a search locate a known file, or a script perform an exact transformation. AI can help choose or build the tool when that is the uncertain part.

If the missing input is an observation, collect it. More confident prose will not establish a physical fit or reveal a screen the agent has never seen. If taste is the missing input, make a choice or provide a reference with an explanation.

Some activities are valuable because you want to do the thinking or making yourself. Use the agent to ask questions, explain a difficulty, or review an attempt while leaving that part of the work with you. Finishing the artifact is only one possible purpose for the session.

## Start with enough context to judge an attempt

Before spending time on an elaborate prompt, identify the result you want, the material the agent can use, and how you will judge what comes back. If those are unclear, ask for help making them concrete.

When you have relevant prior work, reuse it deliberately. Point to a few accepted examples and say why they fit. Include a rejected direction if it explains a boundary. Add the current task and any new constraint. The [context brief](../templates/context-brief.md) keeps that information small enough to review.

Marc's [Rage gear account](../field-notes/rage-gear-context.md) motivates this continuing-work question: a short new request may depend on earlier judgment. The record you supply and the access the next session actually has are things you can inspect; time spent using an assistant alone does not establish either.

## A practice to try

Pick one task from today. Decide whether you want exploration, understanding, implementation, repetition, or critique. Give the agent that role and one useful artifact to return. Afterward, ask what made the attempt useful and what information it lacked. Preserve the lesson that would help the next related task.
