# When the source goes quiet, the interface should say so.

*By Marc / @NeuralYogi. Reproduced from [the original public essay](https://neuralyogi.com/essays/when-the-source-goes-quiet/). Original publication date not shown in the live archive. Captured 19 October 2026 UTC. Body wording preserved; HTML converted to Markdown. Project state and limitations are those of the original essay.*

> **Editorial note:** The original page includes an interactive source-state demo. This edition includes its initial static text. Open [the original page](https://neuralyogi.com/essays/when-the-source-goes-quiet/) to switch between current and expired source states.

---

A dashboard can look reassuring long after the information behind it has stopped arriving. The layout is intact. The typography is crisp. Yesterday’s answer is still sitting in today’s slot.

Recompose explores a different behavior: keep the destination stable, but make every displayed fact answer to its source.

## The interface borrows its evidence

A calendar owns its events. A weather source owns its observations. The interface reads selected fields through adapters, with a clear boundary around what it can claim.

The view should not quietly become a second authority just because it has a convenient copy of the data.

When a source expires, the adapter withholds the affected value and explains the gap. Other independent sources can still appear. One missing source does not have to erase the entire page.

## Try the boundary

The example below uses invented demonstration data. Switch the source state to see how the same interface can preserve its place without preserving an expired claim.

Current sourceExpired source

EXAMPLE DATA / PROJECT STATUS

**In progress**

Example source is within its freshness window.

## A gap with a reason

“Unavailable” is more helpful when the interface explains what happened. The source may be missing, the reading may be too old, or the requested field may never have been supplied.

Those cases should not collapse into the same apparently valid zero or an old value with a new timestamp.

The original Recompose study uses an unavailable tank feed as a concrete boundary. The source code can still be linked. The expired feed cannot be presented as live.

## Where the idea transfers

This pattern matters in briefings, alerting systems, retrieval workflows, and agent interfaces. In each case, the presentation needs a way to distinguish evidence from the absence of evidence.

The useful outcome here is a visible behavior and a design constraint. This is a lab concept, not a measured customer deployment or a finished service.

Read the original essay, [A surface that refuses](https://neuralyogi.com/essays/a-surface-that-refuses/), for the broader reasoning.
