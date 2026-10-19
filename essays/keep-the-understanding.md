# Outsource the thinking. Keep the understanding.

*By Marc / @NeuralYogi. Reproduced from [the original public essay](https://neuralyogi.com/essays/keep-the-understanding/). Original publication date not shown in the live archive. Captured 19 October 2026 UTC. Body wording preserved; HTML converted to Markdown. Project state and limitations are those of the original essay.*

---

I am typing this without thinking about my fingers.

I know what I want the sentence to do. Somewhere below that intention, both hands are finding keys, correcting their position, pressing with enough force, and getting ready for the next word. I can pay attention to the mechanics if I choose to. The strange part is how quickly the sentence falls apart when I do.

The motor loop works because it has moved out of the foreground. I keep the meaning. My body handles the typing.

That is the idea I keep returning to with Agent Body Protocol. A conscious agent should be able to decide what it means without spending its context on how a joint turns or an LED breathes. The body needs its own layer, close to the hardware and boring in the best way.

## Meaning above. Motor loop below.

I do not need a second inner monologue for my hands. There is no little manager naming each tendon before I hit the space bar. Intention becomes motion through a stack of learned loops that I mostly do not notice.

Robots often get built in the opposite direction. We give the top-level agent access to everything, then ask it to reason all the way down. Pick a color. Set a duration. Choose an angle. Check the device state. Recover from the last command. Do it again when the next event arrives.

That can work in a demo. It is also an expensive place to keep the motor loop. The agent burns tokens narrating implementation details that have little to do with the task it is trying to finish. Worse, the same intention can produce different body behavior depending on what the model happens to say that time.

I want the conscious layer to say something closer to: I am thinking. I need permission. The tests failed. I am done.

The body should already know what those states feel like.

## A narrow contract, not another agent.

I think of Agent Body Protocol as a robot subconscious. Not consciousness in miniature. Not another agent waiting under the agent. It is a narrow contract that turns intent into repeatable body language.

A coding agent speaks nine events and four verbs. The body answers with light and pose. Most of the time it stays quiet. Speech, when used, is an optional short line in the event response, not a narrator explaining every movement.

That division matters. The conscious agent keeps the reason for the action. The protocol owns the physical expression of it. A permission request gets attention behavior. A failed test gets a clear failure pattern. Thinking can breathe without talking. Quiet restores the user's prior LED state.

None of those choices should require fresh prose from a model. They are body policy. We should be able to inspect and test them. They should also be dull enough to trust.

I like this boundary for the same reason I like a stable API. The caller says what happened. The implementation handles how this body expresses it. Change the hardware later and the meaning can survive.

## Put each kind of understanding where it belongs.

Models are useful at ambiguity. Hardware is less forgiving. A joint still has limits. A light still has state. Commands still arrive too quickly, get repeated, or land after the moment has passed.

Letting a model improvise every physical detail mixes two kinds of work. One is interpretation: what is happening, what does the user need, should the agent wait? The other is control: which allowed behavior runs, for how long, and what state gets restored afterward.

The first benefits from language and context. The second benefits from deterministic mapping and small state machines.

This is where outsourcing the thinking can sound backwards. I am not trying to make the robot less understandable. I am trying to put each kind of understanding where it belongs. The agent understands the task. The body layer understands the body.

That gives the conscious agent less to say and more room to notice. It can keep track of the work, the person, and the reason it moved in the first place. The protocol can handle coalescing events and returning the body to a known state without asking the model to rediscover those mechanics every time.

## Simulator today, real lamp later.

The current proof is deliberately modest. We built the protocol, not the lamp. The contract accepts a small set of coding-agent events and maps them to exact body behavior. It can record what it would send, run against the simulator, and keep speech optional.

What interests me is larger than this particular body, but I do not want to jump past the bench. The separation has to hold first. An agent needs to express state without thinking through the actuator stack each time. The body needs to stay consistent while the agent changes. And I need to be able to inspect the physical policy without reading a transcript of the model's mood.

That is enough work for now.

When I type, I still own the sentence even though I am not directing every finger. The understanding did not disappear when the motor loop moved down the stack. It became easier to use.

That is the relationship I want between an agent and a body. Keep the meaning near the work. Let the body learn how to carry it.
