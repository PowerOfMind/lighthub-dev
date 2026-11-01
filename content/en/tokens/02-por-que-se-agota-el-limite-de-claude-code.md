---
title: Why does Claude Code hit its usage limit?
desc: Understand Claude Code session, weekly and model-specific usage limits, and learn when switching models or waiting can help.
---
Claude Code can reach a subscription usage limit even when context space remains. The message identifies the limit and its reset time; use `/usage` to inspect your plan usage.

## Identify the message
| Symptom | Cause | Fix |
|---|---|---|
| `You've hit your session limit` | Session-window limit shared across models | Wait for the reset; switching models does not reset it. |
| `You've hit your weekly limit` | Weekly limit shared across models | Wait for the reset; switching models does not reset it. |
| `You've hit your Opus limit` or `You've hit your Sonnet limit` | Limit for that family | Use `/model` to select another family. |
| Context or compaction warning | The conversation takes up substantial space | Compact or start another task; this is not a usage limit. |

In Teams and Enterprise, usage windows are shared across Claude chat, Claude Code and Cowork. When signed in with claude.ai, `/usage-credits` lets you use extra usage credits; you can also wait for the reset.

## Why usage grows
Long sessions resend history on each request. Caching can make reading it cheaper, but cache misses, subagents, teams and background tasks also contribute. Compacting a large conversation also requires processing it.

> [!TIP] Separate tasks
> Use `/clear` between unrelated tasks and check `/usage` to observe the difference.

Source: [Claude Code costs](https://code.claude.com/docs/en/costs).
=== esquema
# Limits
- Session and week — switching models does not reset a shared limit.
- Family — another family may remain available.
- Context — distinct from usage limits.
=== test
? What shows plan usage?
* /usage
- /rewind
- /rename
! Check /usage.
? Does /model reset the shared weekly limit?
* No
- Yes, always
- Only after compaction
! Wait for the indicated reset.
? What can help with an Opus-specific limit?
* Choose another family with /model
- Resend the same message
- Rename the session
! Another family may be available.
? Is a compaction warning a usage limit?
* No
- Yes, always
- Only in short sessions
! Context space and usage are different concepts.
