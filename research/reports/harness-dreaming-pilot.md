# Can a coding setup learn from its own history?

**Engineering case study and pilot report · 9 November 2026**

Research executed 7–8 November 2026. Prepared for The Rage Fieldbook by Marc / @NeuralYogi with AI assistance. Not peer reviewed or independently reproduced. Selected aggregates are reported below; the original private inputs are not a public reproduction package.

## The decision this report can help you make

When an agent repeats a mistake, should you add an instruction, improve a skill, repair a tool, or leave the setup alone?

We investigated a broader version of that question: could a coding-agent setup examine its usage history and propose changes that make later work better? We called the idea “dreaming.” Here, learning means changing external instructions, reusable procedures, tools or project records. It does not mean changing model weights.

The useful result was narrower than the original ambition. We found concrete collection and reliability defects. We did not demonstrate added value from model-driven reflection over the deterministic controls used here, or an improvement in general coding productivity. The final pilot's planned six-pair comparison was inconclusive. We stopped the campaign without adopting an automated loop.

**The practical lesson is to establish what failed, repair the relevant layer, and test whether the next task actually benefits. A correct tool and a correct answer are not enough to establish that connection.**

## What kind of evidence this is

This is an original, AI-assisted account of locally executed engineering experiments. Marc directed and authorized the work. AI assistants prepared designs, fixtures, scripts, model assignments, collection, analysis and this writing. The coordinating assistant authored the task contracts and graders and reviewed the results. There was no independent human adjudication of the pilot and no independent reproduction for the book.

The work had four parts with different evidence:

| Part | Material | What it can establish |
| --- | --- | --- |
| Architecture survey | Three model-assisted design surveys and source inspection | Design questions and candidate safeguards, not measured effectiveness |
| Cumulative-evidence fixture | Authored cases, fixed decisions and six solver batches | Behavior on that constructed decision problem |
| Component experiments | Selected real session metadata and disposable runtime/file fixtures | Specific collection, lookup and checkpoint mechanisms |
| Final pilot | Six paired metadata-audit jobs and one constrained proposal task | Behavior under those particular tasks and contracts, subject to the limitations below |

Do not pool their denominators into an overall accuracy or productivity score. An authored case, a file-integrity scenario, a unit-test method and a real audit job are different units.

## 1. Preserve the evidence, not necessarily the whole prompt

The first fixture contained nine constructed cases. Its policy asked for a scoped proposal or no change, with supporting event identities. Cases included older supporting evidence, one task repeated through delegates and retries, untrusted text, a newer explicit preference, an obsolete-version failure and an already-proposed change.

The parent supplied both the action catalog and decision policy. This was not open-ended discovery of useful improvements from arbitrary history. The independent-root threshold was a fixture rule, not a policy adopted for other work.

We compared two representations of the same normalized cumulative evidence: full event history and a lossless index that reused repeated observations. Three model families each received one batch per representation. There was no favorable-result retry.

| Recorded Pi model label | Full cumulative history | Lossless indexed history |
| --- | ---: | ---: |
| GPT-6.1 Sol | 9/9 qualified decisions | 9/9 qualified decisions |
| Claude Opus 5.5 | 9/9 qualified decisions | 9/9 qualified decisions |
| Grok 4.7 | 9/9 qualified decisions | 9/9 qualified decisions |

Each cell is one batch of nine cases, not nine independent experiments. All final JSON answers were identical. Grok also emitted prohibited intermediate commentary in both conditions: final-payload correctness and whole-stream compliance were separate outcomes.

A hand-authored, fixture-specific no-model reference also returned 9/9 qualified decisions. Restricting that reference to the preceding six hours returned 6/9, missing three cases requiring older support. No model was run on the window-only condition.

This negative control illustrates the consequence of deleting needed evidence from this fixture. It does not establish a production accuracy gain, a best model or an optimal schedule. A process running every six hours can consult cumulative evidence; six hours describes a possible processing cadence, not a required memory horizon.

The index reduced this deliberately repetitive packet from 11,819 to 9,185 UTF-8 bytes while round-tripping to the same event fields. Those are bytes, not provider tokens, billing or inference time. Lossy summaries and semantic retrieval were not qualified by this comparison.

An accompanying in-memory ingestion benchmark used eight virtual checkpoints and three repeats. At 16,384 synthetic events, median processing was 147.956 ms for repeated full-history ingestion and 35.312 ms for incremental ingestion, with matching retained states. Disk I/O, serialization, inference, review and delivery were excluded. The later file experiments show why that component timing cannot stand in for production collector performance.

## 2. Check whether the history reader can see the work

The next experiment explicitly selected the six completed Pi sessions from the first round. Each was known from its separate activity record to contain one completed read call. These were closely related discovery-campaign tasks, not six diverse production workflows.

The captured analyzer did not support their native Pi message format. It reported zero calls and zero paired results on every selected source. A reference adapter recovered all six calls and their results.

Three projections were calibration inputs and three were withheld. Projections removed prose, reasoning, arguments, tool outputs and account metadata; they pseudonymized identities and shifted clocks. Each model received a fixed declarative mapping contract rather than permission to write executable parser code.

All three returned the same mapping as the no-model reference. Each passed the three withheld traces and eleven mapping tests. The parent-supplied interpreter—not the model—provided bounds, validation, deduplication, conflict rejection and privacy controls. Two incumbent-format smoke controls passed; they were not comprehensive legacy regression coverage. Grok again emitted one prohibited intermediate sentence despite a valid final payload.

The concrete finding is missing format support. The component result does not show that model reflection was necessary to repair it.

A future reader should distinguish at least three outcomes:

- **Supported zero:** the input format is understood and contains no qualifying work.
- **Unsupported:** the reader cannot interpret this format or version.
- **Incomplete:** the selected input or capture is not sufficient to report complete coverage.

Treat those as requirements motivated by the failure, not a claim that the prototype already implements a complete production collection service. Compaction and context edits also do not erase recorded tool execution. A tool-call inventory is not a reconstruction of everything the model could see at a particular moment.

## 3. Test the infrastructure without inventing a working backend

Two deterministic experiments examined prerequisites for reliable cumulative processing.

### Runtime ownership

An inspected memory-query helper failed at its fixed legacy directory because that directory was absent. It exited before querying a backend. We did not repair or test the actual retrieval system.

Disposable on-disk runtimes then compared location policies under eleven authored contracts. Choosing the first valid location met eight contracts; requiring an explicit selected root met all eleven. The former could choose an unrelated runtime, accept an unselected runtime or silently bypass a broken override.

Other cases exercised literal arguments, spaces, quotes, shell punctuation, missing files and invalid input through actual subprocess stubs. Refusing unselected discovery was an author-chosen safety contract, not proof of the best possible user experience. An authoritative project/account manifest could supply an explicit default. Stub argument behavior did not establish compatibility with the absent real query program or retrieval quality.

### Checkpoint integrity

Nine scenarios manipulated temporary JSONL files and reopened persisted state. They covered append/replay, partial-tail completion, rotation, truncation, same-size rewriting, conflicting rewriting, atomic batch rejection, interrupted state replacement and source changes during capture.

| Reader policy | Controlled scenarios passed |
| --- | ---: |
| Full rescan into an additive cumulative ledger | 9/9 |
| Naive byte offset | 3/9 |
| Validated checkpoint | 9/9 |

Before this comparison was frozen, a test exposed a metadata-only guard missing a same-size rewrite with restored modification time. The failed prototype and receipt were retained. The corrected prototype added a second full-content read and full-prefix hashing before the final freeze.

It therefore did not demonstrate delta-only I/O or an end-to-end speed advantage. The prototype was single-writer and did not qualify locking, power-loss recovery, archive rebuild, deletion propagation or a complete concurrent-writer protocol. Successful fixture checks are not a production logging guarantee.

## 4. Ask whether the repair changes the next task

The final pilot selected six completed root threads, excluding discovery-campaign descendants and duplicate roots sharing worktrees. The selected material was four Pi session files, one native Codex file and a fixed 21-item application-activity window. These were separate real metadata-audit deliverables drawn from one project context, not representative feature-development tasks. Some selected files began in later runs of their source roots; file scope was not the entire source-project history.

Task contracts, metadata projections, golden labels, baseline, bounded compiler and prompts were frozen before the proposal task. The parent checked original-versus-projected call/result counts. Independent labeler code did not make the adjudication independent of the parent. Worktree and read-scope separation was not OS-enforced inaccessible holdout isolation.

The proposal task received seven curated cumulative findings and calibration material. It could select the known Pi v3 mapping or no change. It selected the mapping; the parent compiler produced source identical to the deterministic reference. This was constrained promotion, not autonomous evidence mining or novel repair discovery.

The retained initial-plan SHA-256 was `22b6dc054d1f60ccbe3366bc983ea470ff9e8da3ee4323b115806ade8ec3208c`. Candidate source SHA-256 was `9df5dbbc0362c9571003d1514b147ba7920a5b95d65b71b464baba3d4beb1221`. These identify private retained artifacts; they do not make those artifacts publicly available.

Exactly thirteen model jobs completed: one proposal task and twelve auditors. All used the recorded Pi model label `openai/gpt-6.1-sol`; native records showed `xhigh` before each assistant generation. Backend-internal reasoning comparability was not verified. One model task ran at a time, with no retries, replacements or extra reviewers. Auditors had the same advertised settings, an eight-tool-call ceiling and a five-minute target.

For pairs T1–T6, execution order was unchanged/candidate, candidate/unchanged, unchanged/candidate, candidate/unchanged, unchanged/candidate, candidate/unchanged. Both conditions were retained.

### Correct reports did not establish benefit from the helper

Five unambiguous pairs returned correct exact reports in both conditions. All ten native-log auditors read their supplied analyzer source but then wrote one-off parsers; none executed the helper. Only the two application-activity auditors executed it.

Separate deterministic CLI probes exercised the repaired branch. On the four Pi inputs, the unchanged CLI returned zero; the candidate returned 46, 101, 92 and 184 calls with matching results, agreeing with the frozen labels. The Codex control remained 50 paired calls and application-activity metadata was unchanged.

That is component-repair evidence. It is not evidence that the repaired branch caused better solver delivery. Source availability was the intervention the native auditors actually encountered; executable branch benefit was not exercised in those jobs.

### The sixth pair had a protocol defect

The frozen activity task listed six fields but requested exactly seven listed fields. The helper emitted a seventh `scope` field, while the golden omitted it. Both auditors included that field with the same correct metadata counts.

The original strict grades remain 5/6 per condition. The sixth pair is protocol-ambiguous, not a candidate regression or a qualified success. The planned six-pair primary comparison is inconclusive. The five unambiguous paired jobs tie; they do not establish statistical equivalence on other tasks.

The contradiction was discovered after the candidate's sixth job. The unchanged condition still ran under the original wording. We did not repair the prompt, golden or retained outputs, replace the case, or spend another solver run to obtain a cleaner result. Passing prelaunch unit tests had not established that the protocol itself was coherent.

### Timing did not establish a speedup

| Recorded interval sum | Unchanged | Candidate |
| --- | ---: | ---: |
| All six attempted audit jobs | 265.072 s | 244.202 s |
| Four targeted Pi jobs | 178.141 s | 177.494 s |

The targeted jobs were essentially tied, and most apparent overall difference occurred in unchanged-format controls. These single sequential observations do not establish causal attribution or a reliable time advantage.

Discovery took 16.013 s and promotion/review took 154.976 s. Their combined 170.989 s already exceeded the 20.870 s raw difference between the audit-job sums. Candidate jobs plus those stages were 415.191 s before closing interpretation.

Later closeout charged another 1308.614 s of audit, interpretation, reporting and preview to the candidate, conservatively including control auditing. That brought the candidate job/discovery/review/closing interval sum to 1723.804 s. Shared design/freeze and between-job controller gaps remained separate. This is study accounting, not a forecast of recurring operating cost or a single accepted-delivery clock. The final closeout is later than the earlier report-validation cutoff.

Owner acceptance, attention, actual billing, parent-stage inference attribution and actual tool execution time were not measured. Recorded token counters were not verified subscription charges. No owner-correction benefit was established.

## What we kept—and what we did not adopt

The engineering interpretation is a proposed maintenance boundary:

1. Collect an explicitly selected scope and report its coverage.
2. Retain provenance, independent root identity, version context and counterevidence.
3. Apply deterministic checks before asking a model for a proposal.
4. Put one proposed correction in its owning layer.
5. Compare it with the unchanged baseline and verify that the changed mechanism is exercised.
6. Review release and rollback separately from observation and proposal.

This is a design recommendation informed by the investigation, not an evaluated end-to-end autonomous system. It does not authorize transcript dumping into global guidance, automatic instruction edits, recurring model review or fleet rollout.

The original research changed no installed instructions, skills or services. The remaining source candidate was a narrow deterministic Pi coverage repair, not productionized by this study. The real memory backend remained unverified. The research stopping rule was applied; this report does not reopen the campaign.

## Evidence and reproduction limits

The coordinating assistant retained freezes, failures, prompts, responses, collection receipts and manifests privately. The final pilot's closing manifest covered 122 files; its initial and treatment freezes covered 68 and 10 files respectively. Seventeen final unit-test methods passed: thirteen frozen prelaunch methods and four later collection-only methods. Collection changes preserved the original task, outputs and grades. Neither unit tests nor artifact hashes establish task efficacy.

This report publishes no raw session, reasoning, argument/output payload, account identity, private repository URL or operational endpoint. It reports selected aggregates and methods. Local source inspection supports the account, but a public reader cannot independently reproduce the private model cohort from this page. Releasing portable fixtures later would require separate selection and review, and newly written teaching fixtures must not be presented as the original cohort. The study does not establish broad Pi-version coverage, native Grok coverage or production logging reliability.

The [experiments chapter](../../chapters/07-experiments.md) explains simpler baselines and complete cohorts. [Context and memory](../../chapters/05-context-and-memory.md) explains current decisions and source access. [Improve a skill after a miss](../../walkthroughs/improve-a-skill.md) separates implementation defects from procedural revisions. This investigation adds an executed case; it does not complete a broad skill-transfer or fresh-session context study.

## A practice to try

Choose one recurring failure. Write down the current version, the source that establishes the failure and the smallest correction that could address it. Keep a no-change alternative. Before evaluating the correction, specify how you will tell whether the next task actually used the revised mechanism.

If a parser cannot read a format, start with the parser—not a new instruction telling every agent to try harder. If the next task bypasses the parser, keep the component repair and delivery claim separate. You may have improved a tool without yet showing an improved workflow.
