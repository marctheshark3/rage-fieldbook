# 9. Cross into the physical world carefully

Moving from software to a device introduces new questions about geometry, timing, physical state, and recovery. Keep the agent's high-level intent connected to a narrow control contract and to observations of the actual output.

The essay [Outsource the thinking. Keep the understanding.](../essays/keep-the-understanding.md) gives the guiding example: an agent expresses an event, while a lower layer owns the light and movement associated with it. The public [Agent Body Protocol](../sources/README.md#agent-body-protocol) documents that vocabulary and its simulator-oriented implementation. The cited evidence does not establish a completed physical lamp.

## Name the kind of evidence

Source inspection can establish what the code specifies. A simulation can establish what happened in a modeled environment. An exported solid can establish a property of that geometry. A physical fit check can establish something about the parts actually tested.

Each is useful. Keep its conditions visible when moving to the next stage. A rendered assembly does not establish clearance with the real cable in place. A simulator replay does not establish a motor's behavior under load.

[Printables](../sources/README.md#printables) documents a workflow around a print specification, geometry checks, and inspectable outputs. Its public method supports a staged approach: make the question small enough to answer before committing to a larger fabrication step. Follow the source's current instructions for any real operation.

## Keep calculations and controls distinct

[Spatial Tools](../sources/README.md#spatial-tools) can check explicit two-dimensional scenes. The supplied units, frame, footprint, uncertainty, and freshness determine what the calculation can support. An image alone does not establish real-world scale. A static fit and an insertion path are different questions.

The geometry tool does not operate the machine. That separation lets one component answer a spatial question while the controller handles observation, actuation, and authorization.

The public [Bambu P1S MCP](../sources/README.md#bambu-p1s-mcp) project provides a useful example of tool-level operation checks. Its print interface requires a confirmation argument and checks certain busy states. The confirmation flag is supplied by the caller; it does not authenticate a human decision or replace a hardware interlock.

## Learn from games before generalizing

The [Player Two essay](../essays/player-two.md) shows the same observe–act–observe pattern in a game. Independent controls and bounded actions made failures easier to reproduce. Looking at the rendered image exposed a presentation problem after recovery.

Games can make feedback cheap and visible. They offer a place to study the loop; they do not establish physical reliability. Carry the practice of inspection into the new domain and establish that domain's own evidence.

## A practice to try

For the next physical build, list the claims you are making and mark each as designed, simulated, exported, fitted, or physically measured. Choose one unresolved interface between stages. Define the smallest observation that would let you cross it.
