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

## A practice to try

Choose one recurring task and write down the data it needs, its acceptable completion time, and what makes an answer useful. Run a small matched comparison through the complete workflow. Keep speed, task quality, and operational effort as separate observations before making the adoption decision.
