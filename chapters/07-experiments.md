# 7. Keep the experiment honest

A research artifact becomes more useful when someone can tell which question it answers and which conditions made the result possible. Keep the claim, the comparison, and the evidence close together.

For an AI-assisted implementation, the first comparison can be small: the current approach, the candidate approach, the same task, and a result that matters. Add complexity when it resolves a real uncertainty. A large benchmark cannot repair a comparison whose conditions are unclear.

## Keep the simpler explanation in the experiment

[Rage JEPA](../sources/README.md#rage-jepa) publishes a small state-vector model, a cart-pendulum environment, classical baselines, and recorded evaluations. Its public documentation explains that the successful control path uses classical feedback and that the learned dynamics predictor failed its forecast gates.

That distinction changes the interpretation. The release offers material for studying inference and representation within a particular control setup. It does not justify saying that a learned world model planned the successful actions. The book describes the project's reported evidence; it has not rerun the experiments.

Keep a simpler baseline in the comparison. If it performs the task with less cost, that fact belongs beside the candidate's result. It can reveal where a complex method helps, where it adds overhead, or where the original question needs revision.

## Preserve the whole cohort

[Pendulum Arena](../sources/README.md#pendulum-arena) documents campaigns with protocol identities, controller freezes, complete cohorts, and linked artifacts. It distinguishes author-attested entries from independent reproduction and keeps the browser toy separate from scored native campaigns.

Those distinctions are useful beyond control research. Keep attempted cases, failures, exclusions, and the criteria used to decide success. Record when the criteria were chosen. A polished replay can illustrate an outcome; it does not supply the denominator of the experiment.

A validator can check a record's structure and accounting without establishing that the underlying controller works. State what each check actually did. Likewise, a source-controlled artifact preserves an identity without proving the scientific interpretation attached to it.

## Record negative results where the claim lives

A failed forecast gate or an unsuccessful ranking study can narrow the next experiment. Keep the failed condition and its consequence beside the positive result. Otherwise a later summary may preserve only the impressive part and lose the reason a method was not adopted.

The same care applies to speed. Report the work included in the timing, the environment, and the comparison conditions. Simulated cadence does not establish a physical deadline. A model's ability to execute inference does not establish prediction quality.

## A practice to try

[Give AI a finish line you can test](../walkthroughs/define-success-with-the-pole.md) turns the public pole protocol into a practical acceptance brief. Its fictional cases distinguish a short hold, a rail violation and missing evidence; they do not add controller results to the published campaign.

Use the [research guide](../research/README.md) and [research note template](../templates/research-note.md) when a comparison needs a fuller method and result record. The [context-position proposal](../research/proposals/context-position.md) shows how to state a bounded question before execution, with missing artifacts and results kept visible.

Pick one promising claim in a project. Write its strongest simpler alternative explanation. Identify the baseline or ablation that could distinguish them. Use the [evidence note](../templates/evidence-note.md) to record the comparison, including what a negative result would mean before running it.
