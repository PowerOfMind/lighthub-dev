---
title: Which model and effort level save tokens?
desc: Choose a Claude Code model and effort level for each task, manage thinking tokens and avoid overspending on a large default model.
---
Choose the model and effort level to suit the difficulty of the task. A more powerful model is not always necessary, and leaving Opus as the default can raise spending on sessions and subagents.

## A practical decision
| Task | Starting point |
|---|---|
| Everyday coding changes | Sonnet handles most coding tasks and costs less than Opus |
| Complex architecture decisions | Consider Opus |
| Simple delegated work | You can specify `model: haiku` for the subagent |
| Long logs or documentation | Delegate analysis and request a verifiable summary |

Use `/model` to switch models during a session. Set the default in `/config`. Switching to Opus also affects subagents that inherit the session model, so check that choice before delegating. Subagents consume usage too.

## Adjust thinking
Extended thinking is enabled by default and thinking tokens are billed as output. Lower effort with `/effort` or in `/model` when the task does not need as much depth. Thinking can be disabled in `/config`, although some recent models do not allow it. For fixed-budget models, `MAX_THINKING_TOKENS` is available, for example `MAX_THINKING_TOKENS=8000`.

> [!TIP] Check the result
> Lower effort can save work, but verify the answer and increase effort if it does not solve the problem. Compare usage on similar tasks.

Source: [Claude Code costs](https://code.claude.com/docs/en/costs), [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [current pricing](https://platform.claude.com/docs/en/about-claude/pricing).
=== esquema
# Model and effort
- Choose — match the model to the difficulty.
- Adjust — `/model` and `/effort` control the session.
- Verify — check results and usage, including subagents.
=== test
? Which model does this guide suggest considering for complex architecture?
* Opus
- Always Haiku
- None
! Opus is an option for complex decisions.
? How are thinking tokens billed?
* As output
- They are never billed
- Only as storage
! Thinking is billed as output.
? What can happen when switching to Opus?
* Subagents inheriting the session model may use it too
- All subagents stop consuming usage
- The history is deleted
! Check subagent configuration.
? Which command switches models during a session?
* `/model`
- `/mcp`
- `/context`
! `/model` changes the session model.
