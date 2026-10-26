# 8. Choose where the model runs

Where a model runs changes the rest of the workflow: what data crosses a boundary, how long feedback takes, which failures you need to handle, and who maintains the system. Begin with the task and its constraints before choosing a deployment.

The public [Lightning Compute](../sources/README.md#lightning-compute) project documents local serving and routing infrastructure. [DeepAgents Local](../sources/README.md#deepagents-local) documents connecting an agent workflow to local inference. These are examples of integration work. Their READMEs do not establish that a local model is the best choice for every task.

## Compare complete work

A serving benchmark can measure throughput, latency, and concurrency. A useful-work comparison also needs to ask whether the answer or action met the task's requirements and how much review or repair followed.

The public [LLM Benchmark](../sources/README.md#llm-benchmark) tool is a source for serving measurements. It does not by itself measure answer quality. Keep those questions separate when comparing a fast endpoint with a slower one.

For a bounded experiment, hold the task and acceptance criteria steady. Record setup time, task time, retries, tool failures, review effort, and total cost where available. If the local workflow requires a different tool contract, document that difference before attributing the outcome to the model.

## Make the boundary explicit

Local execution can reduce transfers when all required work and storage remain local. A local model can still call remote tools, download packages, or write to external services. Describe the actual data path when privacy is a reason for the choice.

Likewise, fallback is a product decision. A workflow intended to keep data on one device should not quietly send the task to another service after a timeout. Make fallback behavior explicit and verify it under the failure condition that triggers it.

## Treat operations as part of the cost

Model loading, service readiness, memory pressure, compatibility, updates, and recovery all affect the experience. A deployment that performs well during one prepared run may still be hard to operate over a week of changing tasks.

You do not need a large infrastructure plan to begin. Take one representative workflow and compare two viable routes. Keep the source data and result review within the intended boundary. Expand the serving setup only when the experiment identifies a useful reason.

## Read a comparison through to acceptance

Here is a **constructed comparison**, with invented timings and outcomes. It is an arithmetic and review exercise, not a benchmark, a provider recommendation, or a report from Marc's infrastructure.

Use the two planning drafts in [Everyday work beyond code](../walkthroughs/everyday-work.md#compare-documents-without-deciding-the-policy). Both routes receive the same text and assignment. An acceptable comparison must preserve the changed setup time and room, identify the registration deadline as present only in A, and leave the governing plan unresolved. Missing information in B cannot establish that the deadline was canceled.

For this exercise, Route L uses a local model and Route H a hosted model. Both receive only the supplied text and have no retrieval tools. Their illustrated first drafts require corrections: L incorrectly calls the deadline canceled; H miscopies the setup time. Each is repaired and checked against the original pair before acceptance.

Assume each stage happens sequentially. Times are wall-clock minutes, and setup is separate from work on the task:

| Stage | Route L | Route H |
| --- | --- | --- |
| Initial setup | 20 | 5 |
| First draft | 2 | 4 |
| Review against both sources | 6 | 2 |
| Repair | 4 | 1 |
| Final acceptance check | 1 | 1 |
| Task through acceptance, excluding setup | 13 | 8 |
| First accepted task, including setup | 33 | 13 |

L returns its first draft sooner. H reaches an accepted comparison sooner under these invented conditions. If both routes are permitted and elapsed time is the deciding constraint, H is the choice for this example. Calling L faster from the first-draft row would leave eleven minutes of task work out of its total.

Now change the boundary: suppose the supplied documents must remain on the device and H requires sending them away. H is ineligible before the timing comparison. You can still examine whether L is useful, whether another local route works, or whether doing this small comparison directly is simpler. A fast route does not satisfy a constraint it violates.

The table leaves resource and service costs unknown. A real adoption record should include those costs, the actual data path, model and runtime identities, the supplied packet, all returned drafts, review criteria, corrections, and failed attempts. Keep one-time setup separate so a recurring workflow can account for it explicitly. Do not extrapolate stable future review time from a single task.

Before expanding an evaluation, choose another ordinary task and one missing-input case, and define their expected returns. For example, a title without article text should produce a request for the missing source rather than invented findings. Those comparisons remain to be run. The worked table teaches how to read the whole cost of a result; it supplies no measured local-versus-hosted ranking.

## A practice to try

Choose one recurring task and write down the data it needs, its acceptable completion time, and what makes an answer useful. Run a small matched comparison through the complete workflow. Keep speed, task quality, and operational effort as separate observations before making the adoption decision.
