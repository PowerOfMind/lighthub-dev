---
title: Why do MCP servers and tools consume context?
desc: Learn how to spot MCP tools using context, compare them with CLI alternatives and avoid unnecessary file reads in Claude Code.
---
Tools can use part of the context window for their definitions and results. In Claude Code, inspect what takes up space and disable servers you do not need for the task.

## Check before removing tools
Use `/context` to see what consumes space and `/mcp` to inspect configured servers and disable unused ones. MCP tool definitions are deferred by default: only names and server instructions enter context until a tool is used. Do not assume every full definition is loaded at startup.

## Choose the right tool
A CLI such as `gh`, `aws`, `gcloud` or `sentry-cli` can be more context-efficient because it does not add a listing for each tool. Compare output too: a long result returned to the conversation takes up space even when the tool is useful. A subagent can process logs and return a summary, but it also consumes usage.

Code intelligence plugins for typed languages support precise symbol navigation and can avoid unnecessary file reads.

| Symptom | Possible cause | Fix |
|---|---|---|
| Context fills up | Long tool results | Filter output or ask a subagent for a summary |
| Unneeded servers are present | Configuration is too broad for the task | Review them with `/mcp` |
| Many files are read | Imprecise text search | Consider a code intelligence plugin |

> [!AI] With AI
> Ask for a summary of relevant log failures, including the paths and messages needed to verify them. Hide credentials before sharing.

Source: [Claude Code costs](https://code.claude.com/docs/en/costs), [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows).
=== esquema
# Tools and context
- Measure — `/context` shows what takes up space.
- Review — `/mcp` manages servers.
- Reduce — filter results and use precise navigation.
=== test
? What does `/context` show?
* What consumes context space
- The final invoice
- Only disabled servers
! It helps inspect context usage.
? When is a deferred MCP tool definition loaded?
* When the tool is used
- Always at session start
- Only when the session ends
! Server names and instructions enter earlier.
? Why can a CLI save context?
* It does not add a listing for each tool
- Its results never occupy context
- It deletes the entire conversation
! CLI output can still take up space.
? What does delegating to a subagent cost?
* The subagent also consumes usage
- Nothing
- Only browser space
! Delegation can reduce output in the main context, but is not free.
