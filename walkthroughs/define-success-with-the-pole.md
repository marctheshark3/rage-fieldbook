# Give AI a finish line you can test

How do you tell whether an AI-assisted task is complete? Start by naming what you would need to observe before accepting its result. A pendulum makes the question visible: a pole can look upright in one frame while the task still needs time, valid actions, and a cart that stays on its rail.

**Evidence boundary:** This is an original teaching walkthrough using a public control protocol and its author's reported simulation result. The prompts and practice cases below are constructed teaching material. They are not a transcript of an agent session, a new controller experiment, or a measurement of how much AI improves the work. The control recording does not establish conversational-AI motor control.

## 1. Choose the outcome before asking for an implementation

“Make the pole balance” leaves room for an appealing demonstration that misses the actual task. The published sixteen-link protocol supplies a more precise contract. Every link's wrapped absolute angle must be strictly below 0.15 radians for 250 consecutive post-command samples. At the specified 50 Hz simulated cadence, that is five seconds. The cart must stay within the rail limit of ±3 metres, and the full 30-second episode must complete with valid finite states and permitted forces. The protocol contains the remaining model, reset, action and cohort requirements. [Pinned protocol](../sources/README.md#pendulum-sixteen-protocol).

The three visible questions are useful starting points:

1. Are all sixteen links inside the upright-angle limit together?
2. Does that condition continue for long enough?
3. Does the cart remain inside its permitted range throughout the episode?

These questions make different demands on the evidence. A still can show an arrangement. A time series can establish a consecutive interval. A complete episode record can reveal a rail crossing that a short crop leaves out. Meeting these three conditions alone does not replace the full protocol.

For your own task, write the equivalent conditions in a [work brief](../templates/work-brief.md). A generated report might need every claim tied to supplied sources. A repaired interface might need the intended behaviour after a refresh, on a phone, and with missing data. Choose conditions that would change your decision to accept the work.

## 2. Give AI a useful assignment

Here is a constructed prompt for inspecting the pole evidence:

> Read the supplied protocol before proposing a change. List the acceptance conditions and the evidence needed for each. Keep a rendered pose, an episode score, and a campaign result distinct. If I supply only a screenshot, say which conditions remain unknown. Return the rule, the observation, the source identity, and the remaining uncertainty. Leave controller execution outside this inspection pass.

This gives the assistant a bounded job: translate the contract into observations and identify missing evidence. The person still owns the intended outcome. Review the proposed checks before asking the assistant to change an implementation.

Keep the evaluator anchored to the agreed contract. An agent that proposes a change can also help write checks, but inspect whether those checks still represent your requirement. A test that only confirms the assistant's chosen output shape can miss the behaviour you needed.

## 3. Classify the evidence you actually have

The following rows are **fictional practice cases**, not outcomes from the public campaign. Assume that all other episode requirements are satisfied for A, B and C. Their upright streaks already mean that every absolute link angle is within the stated limit.

| Case | Longest upright streak | Largest absolute cart position | Decision |
| --- | --- | --- | --- |
| A | 4.2 seconds | 2.4 metres | Reject: the hold is too short. |
| B | 6.0 seconds | 3.2 metres | Reject: the cart leaves the permitted range. |
| C | 5.2 seconds | 2.7 metres | Accept this episode under the stated assumptions. |
| D | One upright-looking screenshot | No complete position record | Insufficient evidence: duration, rail history and episode completion remain unknown. |

Ask the assistant to explain its decision before showing it the last column. Then compare its explanation with the contract. This is a practice you can try; the Fieldbook has not run a model comparison on these questions.

Notice the distinction in case D. Missing evidence leaves the result unresolved. It does not establish either a successful episode or a failed controller. The next useful step is to obtain the missing record.

## 4. Read a reported result without enlarging the claim

The public sixteen-link release reports a 7.34-second upright hold and describes completed held-out episodes, original recordings and same-owner checks. It explicitly keeps the result author-attested. This walkthrough reads that published evidence; it does not independently reproduce the controller, establish hardware performance, or compare AI development methods. [Release and limits](../sources/README.md#pendulum-sixteen-result).

A selected replay can help you understand what success looks like. To make a reliability claim, return to the full attempted cohort and its exclusions. The selected clip alone cannot supply that denominator. [Keep the experiment honest](../chapters/07-experiments.md) develops that distinction.

The same discipline applies to AI-assisted work. Preserve the failing input and the accepted revision. Record what changed, what was checked, and what remains unknown. A later session should be able to find the acceptance decision without reconstructing the whole conversation.

## 5. Transfer the practice to your next AI task

Copy this brief and fill in the brackets:

> **Outcome:** [What the person needs to be true.]
>
> **Acceptance conditions:** [Observable conditions, including an important edge case.]
>
> **Evidence:** [The artifact, input and check that could establish each condition.]
>
> **First assignment:** Propose a bounded plan and identify missing inputs. Then produce one attempt within the agreed scope.
>
> **Review:** Compare the delivered artifact with each condition. Mark it met, failed or unverified, and cite the observation. Keep the failing evidence with the correction.
>
> **Handoff:** Return the current artifact, checks performed, remaining limits and next decision.

Start with a small task you can judge. Use the [evidence note](../templates/evidence-note.md) to preserve the result, and [the agent loop](../chapters/02-the-agent-loop.md) to choose the next action. The useful lesson from the pole is a habit: decide what completion requires, then ask AI to help produce and inspect the evidence for it.
