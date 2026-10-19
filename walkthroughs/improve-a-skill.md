# Improve a skill after a miss

When a workflow repeats a mistake, first locate the decision that needs repair. The fix may belong in the current brief, a reference, the implementation, a check, or the skill's procedure. Put it where a future task can use it without inheriting unrelated instructions.

This is a fictional revision exercise built around the [reading digest](brief-to-handoff.md). It describes an imagined existing skill in prose. The procedure excerpts are teaching material, not an installable package or a change to a public skill. The executable checks test the digest program; no before-and-after agent or skill evaluation was performed.

## Establish what actually failed

The digest baseline includes read and archived entries because it selects every nonempty state. Its executed checks also expose a second consequence: when no unread entries remain, the baseline still prints ineligible items.

That establishes a program error under the fixture conditions. By itself, it does not show that a skill was responsible. An agent could have had adequate instructions and still implemented the rule incorrectly.

Fix the program's selection rule and retain the regression cases. Then inspect the procedural question separately: did the workflow require the agent to establish what qualifies and check what should be excluded?

For this exercise, suppose the existing skill's relevant guidance is:

> Prepare a short Markdown reading digest from the supplied entries. Keep it readable, check the result, and return it.

This instruction leaves the qualifying state and the meaning of “check” implicit. If repeated review records showed those omissions causing misses across tasks, a focused procedural revision would be worth trying. That repeated skill behavior is an assumption of the exercise, not an observed history from the program tests.

## Keep the job recognizable

The fictional skill still owns one job: preparing a digest from a supplied reading list with explicit states. The desired outcome has not expanded to article research, reading-service administration, or publication. That continuity is a reason to improve the existing procedure rather than create a second overlapping skill.

Give each proposed change a failure it addresses:

- **State meanings were assumed:** Establish the input's state field and the task's inclusion rule before selecting entries.
- **A readable list was mistaken for a checked list:** Compare included and excluded IDs against the requirement, including a case with no qualifying entries.
- **Missing source was filled in by generation:** Return the missing input or route the task to a workflow with the required source access.

The editor's preference for a direct invitation belongs in [context](teach-taste.md). Adding that voice preference to a general selection procedure would make unrelated users inherit this fictional group's taste.

## Revise the consequential steps

A proposed replacement for the relevant procedural passage is:

> Use this procedure for a digest selected from supplied reading-list records. Establish the input location, the state meanings, and which state the current task requests. Preserve the supplied titles, IDs, and order unless the brief changes those requirements.
>
> Check an eligible record and an excluded record against the selection rule. Include a no-qualifying-records case and return an explicit empty result. Use the existing parser's errors for missing or unknown states; obtain corrected input before continuing.
>
> Return the digest, the check performed, and any missing information. A request for article findings needs article source text and a different investigation; a title-only list cannot supply those findings.

This passage names a decision, a check, a missing prerequisite, and a boundary. A real revision should fit the skill's existing structure and avoid repeating instructions already expressed clearly elsewhere.

It also leaves implementation decisions open. Different input formats may need different parsing. The stable judgment is to establish eligibility and check exclusions; the exact CSV expression belongs to this particular program.

## Review a task that fits, one that does not, and a missing input

Use a small set of cases whose expectations are written before judging the revision:

| Case | Expected result | Evidence available here |
| --- | --- | --- |
| Supplied mixed-state list; request unread entries | Only `r1` and `r3`, in input order | Executed program check and printed output |
| Valid list with no unread entries | Explicit “Nothing unread.” | Executed program check |
| A record lacks its state field | Reject incomplete input | Executed parser check; no agent clarification trial |
| Request findings from an article title | Identify the need for article text or another workflow | Proposed skill-scope case; not executed |
| Request publication to a reading service | Establish service access and authority in a new brief | Proposed boundary case; not executed |

The revised digest program passed all eight acceptance checks, as recorded in the [walkthrough](brief-to-handoff.md#5-verify-against-the-original-expectation). That evidence covers the code's behavior. It does not establish that an agent will discover the proposed skill at the right time, follow its procedure, or handle the last two cases appropriately.

For a real skill evaluation, run the representative tasks with the relevant skill versions in the intended environment. Record the loaded instructions, source access, returned artifacts, checks, and failures. Keep the task packet and review criteria comparable between attempts. Discovery and execution are separate things to examine.

## Decide whether to keep the revision

Inspect whether the new passage helps with different inputs and leaves unrelated tasks alone. A revision that succeeds only on the original four records may have preserved the example too literally. A procedure that invokes a large investigation for every small list may add more work than the task needs.

Review the new instruction beside the old one. Remove superseded guidance so future agents do not receive two competing procedures. Keep the motivating failure and a short account of what the change is intended to prevent.

For this exercise, the resulting record is limited:

> **Observed:** The program's explicit-state revision passes the included acceptance cases.
>
> **Proposed:** Make eligibility, exclusions, missing inputs, and scope explicit in the fictional procedure.
>
> **Still to evaluate:** Whether an agent using that revision behaves better on tasks that fit, tasks outside its scope, and tasks missing prerequisites.

The [skills chapter](../chapters/03-skills.md) gives the broader criteria for deciding when recurring work deserves a skill. A complete execution study of an existing public skill remains a separate item on the [roadmap](../ROADMAP.md#ready-for-a-focused-writing-pass).
