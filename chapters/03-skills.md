# 3. Turn repeated work into skills

A repeated task accumulates knowledge: how to recognize it, what to inspect first, which tools help, what tends to go wrong, and what a useful result looks like. A skill gives that knowledge a durable home that an agent can load when the task fits.

The [official skill documentation](../sources/README.md#official-skills) describes a skill as a directory with a `SKILL.md` file and optional scripts, references, and assets. Agents start from the skill's name and description and load fuller instructions when using it. That makes the description a consequential part of the interface: it needs to say when the procedure applies.

The procedural detail belongs in the skill. The live fact belongs in a tool or current source. A skill can explain how to inspect a printer; it should not pretend that last week's status is the printer's state now.

## When to make a new skill

Make a skill when you can name a recognizable job, describe a procedure worth repeating, and tell whether its result is useful. Reusing the same long prompt or correcting the same sequence repeatedly is a signal to examine the workflow. Extract the part that should survive the next task.

Before creating one, ask:

- **Will this job recur?** There should be a reason to preserve the procedure beyond the current conversation.
- **Is the useful process known?** Keep exploring while you are still changing what the job means. An accepted example gives the first version something concrete to explain.
- **Are there decisions to preserve?** Capture which inputs to inspect, how to choose the next step, and when the evidence is insufficient.
- **Can the result be checked?** Define what comes back and how a reader or tool can assess it.
- **Does an existing skill already own the job?** Improve its instructions or references when the trigger and outcome are the same. Create another skill when it serves a distinct task.

These are editorial criteria for deciding where to invest effort. They are not a rule that every task must become a skill after a fixed number of repetitions. The [official workflow guidance](../sources/README.md#official-practice) likewise recommends starting from a representative task and keeping a skill focused. The [official skills cookbook](../sources/README.md#official-skill-choice) discusses stable procedures, one-time work, and live tools as different needs.

## Put the learning in the right place

| What you learned | A useful home |
| --- | --- |
| What this assignment needs | The work brief or current request |
| What the person likes, with examples and reasons | A dated context brief and selected references |
| What applies throughout one repository | Its project guidance, such as `AGENTS.md` |
| How to complete a recurring kind of job | A focused skill |
| How to perform an exact calculation or operation | A script or tool used by the workflow |
| What is true in a changing external system | A current source or tool result |

For example, the [Rage gear account](../field-notes/rage-gear-context.md) concerns context about Marc and his taste. That information can inform the next brief. A reusable procedure for preparing a deliverable would have its own entry conditions, steps, and checks. Keeping the two distinguishable makes the procedure useful when the references or person change.

## Start with a small version

Take one representative attempt that worked and identify the essential decisions. Describe the trigger, required inputs, next steps, stopping conditions, and expected output. Include one realistic failure or missing input. Add a script when exact execution would improve reliability; add references when detail serves only some cases.

Try the procedure on a similar task with different inputs and on a request outside its scope. Use the failures to refine it. A skill that only succeeds when given its original example may have preserved that example too literally.

Keep a skill local to the work while its procedure is changing. Review private context separately before sharing a reusable package. The public lesson here is the method of finding and checking a procedure; this repository does not create or distribute a new skill package.

## Preserve the useful judgment

A good procedure carries more than a happy path. It explains the inputs it needs, the limits of its evidence, how to handle a missing prerequisite, and what the reader should receive at the end. Keep stable rules close to the main instructions. Move detail that serves only some tasks into references.

Use deterministic helpers when an operation needs exactness. Geometry calculations, file identity capture, format validation, and artifact construction are good candidates. The agent can concentrate on selecting the right question and interpreting the output.

## Three public examples

[System Observatory](../sources/README.md#system-observatory) teaches an agent how to understand an existing system, investigate a behavior, or shape a design. Its helpers support evidence capture and report construction; selecting the meaningful question remains part of the investigation.

[Spatial Tools](../sources/README.md#spatial-tools) combines an agent procedure with a geometry runtime. It requires an explicit scene with units, a frame, observation time, and uncertainty. A result can remain unknown when the scene cannot support the answer. A valid calculation still applies only to the scene supplied.

[Option Flow](../sources/README.md#option-flow) addresses slow feedback and constrained implementation choices. It asks for evidence about the limiting mechanism, a proportionate intervention, and a comparison that includes cost. Its formula organizes questions about options; the project does not present it as a calibrated productivity score.

These examples show different ways to divide work between instructions, references, and code. Follow their public packages for installation and exact behavior; this book carries no copies of the packages.

## Put them into a session

For a public teaching application with a Save-and-retry problem, a session could begin with this assignment:

> Use $system-observatory to trace a repeated Save through this teaching app. Return the requirement, the relevant boundaries, and one experiment that distinguishes a duplicate write from a misleading display.

Once the uncertainty is specific, give an implementation agent the [work brief](../templates/work-brief.md). If the experiment is too slow to inform a decision, use Option Flow to investigate the limiting step. If the next question is about an explicit two-dimensional placement, use Spatial Tools with the required scene rather than asking the code-investigation procedure to guess geometry.

Each skill enters when its question becomes useful. The session can use one skill or several; the work determines the sequence. Keep the brief, returned evidence, accepted change, and next question as the handoff.

## Evaluate the procedure through outcomes

Try the skill on a task that fits, a task that should not trigger it, and a case with a missing prerequisite. Check whether it asks for the right inputs, keeps its scope, and returns something useful. An evaluation that only checks whether the output repeats the instructions can miss whether the work helped.

Record changes to the procedure with the failures that motivated them. A growing skill can become harder to use when every past incident becomes a permanent instruction. Keep the main path readable and retire rules that no longer serve the task.

## A practice to try

Pick one existing public skill and read its description before reading the full instructions. Predict the tasks it should handle. Then compare that prediction with the actual procedure and its examples. The gap tells you where discovery or scope needs clearer language.
