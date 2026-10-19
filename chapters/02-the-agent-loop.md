# 2. Give the agent a feedback loop

A useful agent loop has an outcome, a way to act, and a way to notice what happened. The quality of the loop depends on the connection between those parts. A tool can report success while the thing a person receives is broken.

The [Player Two essay](../essays/player-two.md) describes a concrete example. A remote trainer remained present in game state after a save resumed, but its sprite appeared black. State checks and image inspection answered different questions. The screenshot found a failure that a player count could miss.

## Make the next action small enough to explain

For an unfamiliar problem, start with a bounded pass:

1. State the expectation and inspect the relevant starting state.
2. Choose one action or a short reproducible sequence.
3. Capture the result through the same surface a user receives.
4. Compare it with the expectation and name the remaining uncertainty.
5. Decide whether to change the implementation, change the experiment, or stop.

The bound can be time, actions, scope, or cost. For a game, it could be one transition and a screenshot. For a code change, it could be one failing case and a candidate correction. For a research idea, it could be one comparison against an existing baseline. Choose the bound according to the question.

Keep the starting state with the result. A successful sequence from a fresh session may say little about recovery from an old one. Recovery deserves its own scenario when user progress or stored work matters.

## Measure two kinds of waiting

[Option Flow](../sources/README.md#option-flow) separates time to useful experimental feedback from time to an accepted or delivered change. Both matter. A shortcut can make local feedback arrive sooner while creating more rework before the change is accepted.

Record the two times separately when iteration speed is the problem. Also record what the feedback contained. A quick result that cannot distinguish the competing explanations has little value for the next decision.

The project's published evaluations concern bounded synthetic tasks. They are useful examples of the method and its limitations; this book does not turn them into a general productivity estimate.

## Make stopping a useful outcome

An agent should be able to return that the current evidence does not support an action. Missing access, an incomplete scene, a costly experiment, or an ambiguous requirement can change the right next step. Name the missing fact and the cheapest way to resolve it.

This is especially valuable for autonomous work. A persistent loop needs a visible state, a limit, and a way to report why it stopped. Adding another iteration without changing the information available can repeat the same mistake at greater cost.

## A practice to try

Choose a task that currently produces vague progress updates. Ask the agent to return one before-and-after artifact, the command or sequence that produced it, and the next decision it supports. Use the [evidence note](../templates/evidence-note.md). Expand the loop once the small version gives useful feedback.
