# One task, from brief to handoff

The useful parts of an AI session should fit together: the request explains the outcome, context narrows the choices, an attempt gives you something to inspect, and a handoff preserves what the next session needs. This walkthrough makes those connections with a small reading-list digest.

**This is an original fictional teaching project.** The assignment, dialogue, and review decisions below are constructed examples. The baseline and revised Python programs were executed against the included checks. Those executions establish fixture behavior; they are not a recorded agent session, a fresh-session trial, or a measurement of AI productivity. No articles or people in the fixture are real sources.

## 1. Turn the request into an outcome

The initial request is short:

> Make a digest of what I still have to read.

That leaves consequential choices open. Does “still have to read” include archived entries? Should the program summarize articles? May it change the reading list? A short [work brief](../templates/work-brief.md) makes the intended outcome inspectable:

> Read the supplied CSV and return a Markdown list containing only entries whose state is `unread`. Keep their input order, titles, and IDs. Say “Nothing unread.” when no entries qualify. Reject unknown states, incomplete rows, and duplicate IDs. Read the input without changing it. Return the output, checks, and remaining limits. Work locally; fetching articles and publishing a digest are outside this assignment.

The person has chosen the meaning of completion. The agent can choose how to implement the small transformation. A script is appropriate for executing a stable selection rule; AI can help write and inspect it without remaining in the execution path.

## 2. Give context a job

A compact [context brief](../templates/context-brief.md) adds the fictional editor's presentation choices:

> **Purpose:** A personal list to open before choosing something to read.
>
> **Accepted shape:** A heading and plain bullets. Keep the original titles so the entries remain recognizable.
>
> **Avoid:** Invented descriptions or an introduction suggesting the articles were read.
>
> **Current constraint:** The CSV supplies titles and states, not article bodies. Missing source text cannot support a summary.
>
> **Available material:** The included CSV, program, checks, and this page. Earlier conversations are unnecessary.

This context explains a choice that tests alone might leave open: the digest should preserve titles instead of making up inviting summaries. The current task supplies the selection rule; the context supplies presentation and evidence limits.

## 3. Inspect the first attempt

The teaching files are [the input CSV](../examples/reading-digest/reading-list.csv), [the program](../examples/reading-digest/digest.py), and [the acceptance checks](../tests/test_reading_digest.py). Use Python 3.11 or newer and run these commands from the repository root. The fixture uses only the standard library and prints to the terminal.

```bash
python3 examples/reading-digest/digest.py --version baseline
```

The deliberately flawed baseline produces:

```text
# Read next

- The rain garden after the storm (r1)
- Repair notes from the courtyard (r2)
- A small seed library (r3)
- The abandoned fountain proposal (r4)
```

The program exits successfully. The artifact violates the brief: `r2` is already read and `r4` is archived. This is the difference between a command completing and the desired outcome occurring.

The baseline tests whether the state field contains text. Every permitted state does. It therefore selects all four records. The source makes that explanation inspectable; the output establishes the failure under this input.

```bash
python3 tests/test_reading_digest.py --version baseline -v
```

This command is expected to fail. In the recorded execution, eight checks ran: the mixed-state selection and no-unread checks failed, and six others passed. A reader repeating the baseline should see those two failures. Do not interpret its unsuccessful exit as a setup problem.

## 4. Correct the decision that missed

A useful review identifies the failed expectation:

> The output includes `r2` and `r4`. Select the explicit state `unread`; keep the current ordering and title-preservation behavior. Recheck the case with no unread entries as well as the supplied list.

“Make it better” would leave the selection problem open. This correction names the output evidence, the required decision, and what should survive.

The revision changes one selection expression:

```python
# Baseline: every valid state contains text.
selected = [row for row in rows if row["state"]]

# Revision: only the requested state qualifies.
selected = [row for row in rows if row["state"] == "unread"]
```

The fixture keeps both versions so the failure remains reproducible. A real application would normally remove the incorrect path after preserving the regression case.

## 5. Verify against the original expectation

```bash
python3 examples/reading-digest/digest.py --version revised
python3 tests/test_reading_digest.py --version revised -v
```

The revised digest is:

```text
# Read next

- The rain garden after the storm (r1)
- A small seed library (r3)
```

All eight checks passed in the recorded execution. They cover selection from mixed states, an explicit empty result, input order and distinct IDs with the same title, use of a changed title, rejection of an unknown state, an incomplete row, and a duplicate ID, and preservation of the supplied source file. The expectations are written from the brief; they do not use the selection expression to calculate the answer.

An [evidence note](../templates/evidence-note.md) for this attempt can stay short:

- **Question:** Does the digest select exactly the unread entries while preserving the supplied input?
- **Conditions:** Python 3.12.3; the included fictional CSV and acceptance cases; local execution with no network or model call.
- **Procedure:** The four commands above, plus visual inspection of the two digest outputs.
- **Observation:** The baseline included two ineligible entries and failed two of eight checks. The revision returned `r1` and `r3` and passed all eight.
- **Decision:** Accept the revision for the stated local teaching task.
- **Limits:** These checks do not cover a live reading service, concurrent edits, arbitrary Markdown in titles, article accuracy, or a publishing interface. No AI performance comparison was run.

The scope matters. A correct local list does not establish that a different service saved anything or that an announcement reached its readers.

## 6. Leave a handoff a fresh session can use

The next session should be able to locate the accepted behavior without reconstructing the dialogue:

> **Current outcome:** The revised digest includes only unread rows, keeps input order and source titles, and prints an explicit empty state.
>
> **Entry points:** `examples/reading-digest/digest.py`, `examples/reading-digest/reading-list.csv`, and `tests/test_reading_digest.py` in this checkout. Record the commit or file identity when sharing a particular revision.
>
> **Evidence:** The revised eight-case check passed under Python 3.12.3. The retained baseline fails the two selection cases intentionally.
>
> **Keep:** Original titles and IDs; no invented summaries; read-only input handling.
>
> **Open question:** Whether readers need links. The current CSV has none. Do not invent destinations or add fetching without a new brief.
>
> **Next useful check:** Before extending the program, run the revised checks and inspect the actual output. If they differ from this note, preserve that discrepancy and establish which source changed.

This packet supports a future handoff; no independent fresh-agent retrieval trial was performed for the walkthrough. To try one, open a fresh session with only the named files and ask which evidence supports the selection rule and which desired feature remains unspecified.

## 7. Decide what deserves to persist

The selection requirement belongs with this program and its checks. The preference for recognizable titles belongs in the relevant context. The working commands belong in the handoff.

One completed digest does not require a new skill. If similar tasks recur, examine which decisions repeat across different inputs: locating the authoritative list, interpreting its states, preserving supplied facts, checking exclusions, and returning evidence. That might justify improving an existing workflow. The [skills chapter](../chapters/03-skills.md) explains that decision.

Try the sequence on your own task: write the outcome, provide only relevant context, inspect the first artifact, correct a specific decision, check the result, and leave the next session enough information to continue.
