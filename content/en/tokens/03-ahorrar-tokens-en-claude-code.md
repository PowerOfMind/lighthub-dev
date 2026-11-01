---
title: How to save tokens in Claude Code
desc: Reduce Claude Code token usage with focused tasks, context cleanup, compaction, model selection and early review of its work.
---
To save tokens in Claude Code, separate tasks, narrow your requests and review work early. History is resent on each request, so a long session can consume more even for a small change.

## Habits to prioritise
1. Use `/clear` between unrelated tasks. First use `/rename` to identify the session and `/resume` to return when needed.
2. Narrow the request: “add input validation to the login function in auth.ts” avoids the broad exploration prompted by “improve this codebase”. Include how to verify the result.
3. If you need to keep the thread, use `/compact Focus on code samples and API usage` and adapt the instructions to what matters. Compaction also uses tokens.
4. Inspect `/context` and use `/mcp` to disable unnecessary servers. Switch models with `/model` and adjust effort with `/effort` to suit the task.
5. For complex work, enter plan mode with Shift+Tab. Stop a wrong direction with Escape and use `/rewind` or double Escape to return to an earlier point.

## Delegate deliberately
Subagents can summarise long output without filling the main conversation, but they still consume usage. Agent teams use about seven times as many tokens as a standard session when teammates are in plan mode; reserve them for work that justifies it.

> [!AI] With AI
> Ask for a specific change and an observable verification; review the plan before authorising broad exploration.

Source: [Claude Code costs](https://code.claude.com/docs/en/costs).
=== esquema
# Save tokens
- Separate — clear between tasks.
- Focus — specify file, goal and verification.
- Measure — inspect context, model and tools.
=== test
? Which command clears context between unrelated tasks?
* /clear
- /model
- /mcp
! /clear clears the current session context.
? How can you return to an identified session?
* With /resume
- With /effort
- With Escape
! Use /rename to identify it first.
? What shows context usage?
* /context
- /rename
- /rewind
! /context shows what occupies space.
? Do subagents consume usage?
* Yes
- No
- Only if the session is renamed
! Their summary reduces output in the main conversation, but their work consumes usage.
