# 1. Keep the direction

AI can carry a large share of the work between a question and a useful result. Someone still needs to decide who the result serves, what it must preserve, and which observation would justify the next step. That is the responsibility this fieldbook keeps with the person directing the work.

Start by deciding [what kind of help you need](00-when-to-use-ai.md). Then give the agent the context and autonomy appropriate to that job. A useful collaboration can alternate between asking questions, comparing directions, making something, and judging the result.

## Give it direction and room to work

A practical assignment includes the outcome, relevant material, constraints, and the artifact you want back. Add the decisions the agent can make and any action that changes the sharing or operational scope. The [work brief](../templates/work-brief.md) can hold the assignment, while a [context brief](../templates/context-brief.md) carries relevant examples and earlier choices.

For creative work, show a reference and explain what you value in it. The explanation helps the agent distinguish a preference for the composition from a preference for one incidental feature. Include an example that misses when it gives the boundary useful shape.

For an established kind of work, give the agent room to make the decisions the procedure already covers. For an uncertain direction, ask for a small artifact you can react to. A request for options should produce useful differences; a request for implementation should produce something you can inspect.

The [Rage gear account](../field-notes/rage-gear-context.md) shows why the brief does not always start from zero. Relevant prior context can carry earlier decisions into a new assignment. Check that the material is available and still applies.

## Turn a request into an expectation

Consider a small request: make saving reliable when the connection drops. The implementation could involve a button, a request handler, a database constraint, or several of them. The useful expectation comes first: after the user retries, one intended record exists and the interface explains its state.

An agent can investigate the relevant path and propose a change. Your brief gives that investigation a reason to prefer one outcome over another. Without the expectation, a successful command can look like a successful product.

## Write an outcome you can inspect

A good work brief answers four connected questions:

- Who is trying to do something, and what should happen for them?
- What conditions make the problem interesting, such as a lost response or a resumed session?
- What must survive the change, including existing data and behavior?
- What artifact or observation would let someone judge the result?

For the Save example, the artifact might be a small comparison: normal completion, a response lost after storage, and the user's retry. Keep the stored record and the visible interface in view. Passing the storage check leaves the display question open until someone inspects it.

Use the [work brief](../templates/work-brief.md) to make those choices explicit. The brief can be short. Its value is that it lets the agent choose implementation details while preserving the outcome you care about.

## Understanding is an output

[System Observatory](../sources/README.md#system-observatory) connects intent, architecture, behavior, and design choices. Its public examples include a small Save-and-retry fixture with captured results. The fixture establishes behavior under its own conditions; it does not establish the behavior of another application's storage or concurrency.

That boundary is useful. It gives you an explanation you can inspect, a test you can repeat, and a question you still need to answer. Ask for those alongside the implementation when the change has enough complexity to warrant them.

The [essay about keeping the understanding](../essays/keep-the-understanding.md) approaches the same issue through a physical interface. High-level intent and low-level movement belong in different places. Moving some work into a tool or a lower layer can make the whole system easier to understand when the contract stays visible.

## Make feedback worth keeping

When an attempt misses, identify the decision that needs to change. Point to the relevant part of the output and explain why it does not serve the goal. If it works, explain what should survive the next revision. Specific feedback improves the current artifact and supplies context for later work.

Before adding a permanent rule, ask whether the correction concerns this task, a stable preference, a project convention, or a reusable procedure. Put it in the narrowest useful place. Repeating a temporary constraint everywhere can make future tasks inherit the wrong brief.

## A practice to try

Before starting a task, write a three-sentence brief: the desired outcome, the condition that could break it, and the evidence you expect back. When the agent finishes, read those sentences again. If you can assess the outcome from the returned artifacts, the brief did its job. If you still need a long explanation to discover what changed, improve the brief or the evidence before expanding the task.
