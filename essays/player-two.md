# I taught an AI agent to be Player Two

*By Marc / @NeuralYogi. Reproduced from [the original public essay](https://neuralyogi.com/essays/2026-10-10-i-taught-an-ai-agent-to-be-player-two/). Published 2026-10-10. Captured 19 October 2026 UTC. Body wording preserved; HTML converted to Markdown. Project state and limitations are those of the original essay.*

---

After Continue finished its recap, the other trainer was still there. The game knew about the player. The sprite on the screen had turned black.

That was one of the most useful findings from this week’s work on an agent game player. We had checks for movement, connection, maps and saves. Looking at the picture exposed a different problem: the game’s state could be correct while its presentation was broken.

I wanted the agent to join as another player, with its own controls and progress. That gave it a useful role both as a companion and as a playtester. It could take an action, wait, look at the result, and repeat a sequence that mattered to a person playing the game.

## Give the second player its own world

The controller gives each agent an independent browser profile. My controls and save stay separate. An agent can enter a supplied invitation, move around, open a menu, take a screenshot, and work with a test save of its own.

The actions are bounded. A button press has a duration and a release. The agent can wait or interact with the game’s interface. It can observe the game surface and selected position information. The interface gives it specific game operations rather than an unrestricted script console.

That separation makes tests easier to interpret. If opening one player’s menu affects the other, there is a concrete failure to investigate. If the players enter different maps, their visibility should change accordingly. Reloading one browser should preserve that player’s identity and progress without borrowing the other player’s session.

The same observation and control interface is available through a command-line client, a local JSON service and MCP, a tool protocol agents can use. The game adapter does not need a particular model vendor’s SDK. A tool-enabled model can use the controls; whether it makes good decisions is a separate question.

## Look at what the player sees

The FireRed checks exercised two independent players through movement, menus, stairs, map changes and save recovery. The recovery check needed more than a restored map. It waited for the quest recap to finish and required the player to regain movement control.

Screenshot inspection then showed the black remote trainer. The native field sprites use palette slots, and the recap could clear the dynamic palette selected for a remote sprite. The candidate correction gives remote trainers the native player’s palette slot and suppresses their presence during quest playback.

This is work around an existing game and emulator. Our contribution is the browser integration, player interface and repeatable checks. The correction addresses presentation without writing the player’s story or save state.

The lesson I want to keep is simple: some failures live in the image. A count can confirm that two players exist. It cannot establish that both look right after a transition. A useful agent tester needs to inspect the output the person will actually receive.

## Recovery is part of the feature

Finding a fix also creates a release question. The corrected game exists as a separately tested candidate. Moving it into the running service has to preserve the identities of remembered rooms and the saves associated with the previous build.

A player’s progress is part of the product. It deserves its own upgrade checks, backups and recovery path. Changing the executable underneath an existing room cannot be treated as a routine file swap.

There is more gameplay to exercise: starter choices, battles, wider movement modes and longer sessions. The current checks establish a narrower result around overworld control and persistence.

Even within that scope, the agent has become useful. It can enter the game as a separate participant, reproduce an interaction and bring back an observable result. That gives us something precise to discuss and something concrete to improve.
