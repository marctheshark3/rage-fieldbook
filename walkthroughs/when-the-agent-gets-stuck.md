# When the agent gets stuck

When another attempt repeats the same failure, make the next action answer a smaller question. The useful signal is a change in what you know: a reproduced failure, a located source, a rejected explanation, or a decision the person needs to make.

This guide uses the fictional [reading-digest walkthrough](brief-to-handoff.md) and constructed recovery prompts. Its advice is an editorial method to try. The digest's executed checks establish the local failure; they do not establish how often a particular recovery prompt will help an agent.

## Keep the failure visible

Start with the desired behavior and the artifact that misses it. Save the relevant input, the current file or revision, the command or action sequence, and the observed result. Leave unrelated work intact.

For the digest, the expectation is that only unread entries appear. The baseline prints `r2`, whose state is `read`, and `r4`, whose state is `archived`. That is a much more useful starting point than “the digest is wrong.”

If the output is from an earlier revision, reproduce it against the current one before changing the implementation. A stale screenshot, a different input file, or an old build can send a competent investigation toward the wrong cause.

## Find which part needs repair

Several different problems can look like an agent failing to understand:

| What you can observe | A useful next move |
| --- | --- |
| Success criteria keep changing between attempts | Choose the outcome and update the brief before another implementation. |
| The agent refers to material it cannot identify or open | Supply the relevant source or narrow the task to available material. |
| The command passes but the artifact misses the requirement | Inspect the artifact beside the acceptance condition. |
| Explanations change without a new observation | Ask for one check that distinguishes the remaining explanations. |
| A previous choice keeps resurfacing after it was replaced | Locate the competing guidance and mark which decision is current. |
| The same procedural mistake recurs on different inputs | Examine the existing workflow and its checks. |

Treat these as starting questions. One symptom does not prove a cause. For instance, a missing fact may reflect unavailable access, a retrieval miss, or a source that never contained it.

## Ask for a bounded investigation

Suppose the digest has been repeatedly reformatted while continuing to include already-read entries. Give the next pass a narrow question:

> Keep the current output for comparison. Trace `r2` from the supplied CSV to the selection step. Identify the condition that includes it and compare that condition with the brief. Return the relevant expression and the smallest check that would distinguish a selection error from a rendering error. Keep this pass read-only.

The baseline's selection expression tests whether the state contains text. `read` does, so `r2` enters the selected rows before rendering. The mixed-state acceptance case can expose that failure. The next implementation can now target an identified decision.

This sequence works because each step returns something that changes the next choice. A request to “think harder” supplies no comparable observation.

Choose a bound that fits the work: one input record, one transition, a small source set, or a time budget. For this teaching task, tracing one unwanted entry is enough to examine the suspected mechanism. A larger system may require a different boundary.

## Make another attempt earn its place

Before continuing, state what changed since the last attempt. It might be a new input, a narrower hypothesis, corrected access, a clarified preference, or an implementation change that can be checked.

If the same command returns the same failure under the same conditions, repeating it may add no useful evidence. Explain what the next attempt could distinguish. When the information needed to proceed belongs to the person, return the concrete choice and its consequences.

For example, a request to add article summaries to this digest needs article text or a different output expectation. The fixture only supplies titles. Further generation cannot resolve that missing source.

Keep the bound proportionate. “Two short investigations before reassessing” can be a useful agreement for a small task, but it is an example limit, not a universal retry count.

## Restart with a current-state packet

A fresh session can help when the active context is dominated by abandoned approaches or conflicting instructions. Make the restart useful by preserving:

- The current outcome and the specific failure still observed.
- The exact files, input, and revision or artifact identity to inspect.
- The checks already performed and what each established.
- Rejected explanations, with the evidence that ruled them out.
- The next unanswered question and the scope of the next action.

The [walkthrough's handoff](brief-to-handoff.md#6-leave-a-handoff-a-fresh-session-can-use) gives a concrete packet for the digest. A restart should make the accepted state and unresolved question easy to find. Carry forward the useful evidence from failed attempts without making the next agent reread the whole conversation.

A fresh session still needs access to the packet. Ask it to identify the current selection rule and the supporting check before relying on an extended continuation. That is a proposed retrieval exercise; this guide did not run a fresh-agent comparison.

## Keep the correction in the right place

An unavailable CSV calls for repaired access or a revised assignment. A changed selection requirement belongs in the brief and checks. A repeated mistake in how a procedure handles missing inputs may warrant [improving that procedure](../chapters/03-skills.md#evaluate-the-procedure-through-outcomes).

Once the immediate failure is resolved, record the useful correction and remove superseded guidance from the active path. Keeping every frustrated instruction as a permanent rule can make the next task inherit the confusion.

For a task that feels stuck today, ask for this compact return:

> Show the expected outcome, the current failing artifact, the strongest supported explanation, the remaining uncertainty, and one bounded action that would reduce it. Identify any missing input or decision that prevents that action.
