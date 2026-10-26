# 6. Make the interface tell the truth

An interface helps someone decide what to do. Its presentation should make the state of the information visible: where it came from, whether it is current enough, what is missing, and what actions remain available.

The essay [When the source goes quiet](../essays/when-the-source-goes-quiet.md) develops this through a missing or expired value. Keeping an old value on screen can make it look newly observed. A visible gap can carry more useful information than that impression of continuity.

## Carry freshness with the value

For a value that changes over time, define which time matters. The source might have an observation time, the system a retrieval time, and the interface a rendering time. Those are different events. A recently refreshed page can still contain an old observation.

Choose what the interface should do when the observation expires. It might remove an action, show the age, offer a refresh, or display the last known value as historical. Make that behavior serve the person's decision. A visible timestamp alone does little if the rest of the screen still invites an action that depends on current information.

## Let the surface explain a refusal

[Recompose Experience](../sources/README.md#recompose) is a public concept site and fictional interactive demo that explores bounded information surfaces. It is a source for interface ideas and prototype contracts. Its presence does not establish a deployed private service or the behavior of real calendar, weather, or other providers.

A refusal becomes useful when it says what is missing and what would make the action available. The explanation should use product language. Someone deciding whether to leave now needs to know that the travel estimate is unavailable; they usually do not need an adapter's implementation details.

When the agent is a user of the interface, make the same state available through its observation tools. Otherwise the person can see that information is stale while the agent continues to act on an apparently valid response.

## Separate data from interpretation

The shared project [Ergo Price MCP](../sources/README.md#ergo-price-mcp) documents a tool interface for public market data. Its role in this book is an example of giving models a bounded way to obtain source data. A tool result and a model's explanation remain distinct artifacts. This book does not verify that service's current uptime, data correctness, or suitability for a financial decision.

Keep units, source identity, observation time, and errors with the returned data. An interpretation can then state which supplied facts it used. That makes a stale source or a missing field easier to diagnose without treating every misleading answer as a reasoning failure.

## Write the state changes before drawing the screen

Use a **fictional unread-count panel** to make the contract concrete. The times, values, and responses below are constructed specifications, not observations from an implemented service. All times use one clock. For this exercise, a count is current only while its observation is less than two minutes old; at two minutes it expires. That threshold is a teaching choice, not a general recommendation.

The source first reports two unread entries observed at 10:00:00. The panel receives that record at 10:00:05. A later refresh can retrieve that same observation without making it newer.

| Event | What the person should see | What the agent should receive |
| --- | --- | --- |
| Render at 10:01:00 | “2 unread · observed 10:00” | Current; count `2`; observation time 10:00:00 |
| Clock reaches 10:02:00 | “Unread count unavailable. Last observation 10:00.” | Expired; current count absent; last observation time retained |
| Refresh at 10:02:10 returns the same old observation | The expired state remains | Expired; receiving old data again does not renew it |
| Next refresh fails | “Could not refresh. Last observation 10:00.” | Unavailable; current count absent; fetch failure explicit |
| A new observation at 10:03:00 reports zero, received at 10:03:05 | “No unread entries · observed 10:03” | Current; count `0`; observation time 10:03:00 |

The last row is recovery. A successful empty response carries a real zero; a failed response carries no current count. Converting both to zero would tell the person the reading list is empty when the system only lost access.

Decide which actions depend on the count. Here, an assistant may use a current count in a draft. During expiry or failure, it should report that the count is unavailable instead of writing “2 unread.” The panel may retain a clearly labeled historical value, but that value must stay distinguishable from the current field the assistant uses.

This policy also needs a clock-driven transition. If the panel only checks age when a refresh succeeds, an idle screen could display “current” indefinitely. Returning the same observation after a failure must not produce a brief false recovery.

An acceptance note can now specify four observations to obtain from a real implementation: let the freshness limit pass without a new response; return old data with a new receipt time; fail a fetch; then return a fresh zero. Capture the visible panel and the agent-facing result at each step. Those checks are proposed here, not executed. A recovery test for duplicates or notifications would need its own contract and evidence.

## A practice to try

Choose one changing value in an interface. Test fresh data, expired data, unavailable data, and a source that returns after a failure. Inspect both what the person sees and what an agent receives. Record whether either surface silently converts an old value into a current-looking one.
