---
title: How to use CLAUDE.md, skills and hooks to save tokens
desc: Reduce Claude Code's base context with a concise CLAUDE.md, on-demand skills and practical filters for lengthy tool output.
---
A concise `CLAUDE.md` reduces the instructions Claude Code loads at the start of each session. Move specialised instructions into skills loaded on demand and filter lengthy output before it enters context.

## Keep essentials in CLAUDE.md
The documentation recommends keeping it under roughly 200 lines. Include general conventions, how to verify the project and a short map; avoid copying full documentation or instructions for infrequent tasks.

Example map, adapted to your project:
```text
src/ — application code
tests/ — tests
docs/ — decisions and guides
```

Put the detailed procedure for a specialised task in a skill. The base context then retains only what is needed to navigate the project.

## Filter without hiding failures
A hook can preprocess data before Claude sees it. The documentation describes a `PreToolUse` hook for Bash that filters output from `npm test`, `pytest` or `go test` with `grep` to retain failures; consult the official example and check your hooks with `/hooks`.

> [!WARN] Preserve diagnostics
> Check that the filter does not hide relevant errors or make a failing test look successful. Keep access to full output for investigations.

> [!AI] With AI
> Ask for a proposal to separate general and specialised instructions; check that essential rules remain available in every session.

Source: [Claude Code costs](https://code.claude.com/docs/en/costs).
=== esquema
# Instructions and output
- CLAUDE.md — general guidance and a short map.
- Skills — specialised procedures on demand.
- Hooks — preprocess output and verify the filter.
=== test
? When is CLAUDE.md loaded?
* At the start of each session
- Only when running tests
- Only when closing the session
! It loads at session start.
? Where can specialised instructions go?
* In an on-demand skill
- In every tool result
- In the project name
! Skills load when needed.
? What can a hook do?
* Filter lengthy output before Claude sees it
- Automatically expand the window
- Remove usage limits
! It can preprocess data.
? Which command lets you inspect hooks?
* /hooks
- /resume
- /model
! Use /hooks to check them.
