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

## A practice to try

Choose one changing value in an interface. Test fresh data, expired data, unavailable data, and a source that returns after a failure. Inspect both what the person sees and what an agent receives. Record whether either surface silently converts an old value into a current-looking one.
