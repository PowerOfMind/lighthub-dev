---
title: How to write prompts that use fewer tokens
desc: Write focused prompts that reduce unnecessary reads and repetition: define the task, set a verification goal and correct course early.
---
A focused prompt helps an agent search less and avoid extra clarification rounds. State the goal, where to work and how to verify the result; include only the context needed.

## Before and after
| Before | After |
|---|---|
| “Improve the project” | “Add input validation to the login function in auth.ts and check empty inputs.” |
| “Fix the tests” | “Investigate the login failure; preserve the expected behaviour and run the relevant tests.” |
| “Return every file” | “Summarise the changes and show the relevant diff.” |

A focused request does not guarantee lower usage: measure it and check the solution covers the problem. Asking for a diff reduces the requested response, but the agent may still need to read files to do the work.

## Guide the work
1. For complex tasks, use plan mode and review the approach before implementation.
2. Define an observable check: relevant tests, expected output or a screenshot.
3. If the agent goes off track, stop and correct it early; in Claude Code you can use Escape and `/rewind` to return to an earlier point.
4. When switching to an unrelated task, use `/clear`. To return to the earlier task, use `/rename` before clearing and `/resume` to return.

> [!AI] With AI
> Ask the agent to restate the goal and identify missing information before a complex task. Check that it does not expand the scope unnecessarily.

Source: [Claude Code costs](https://code.claude.com/docs/en/costs).

=== esquema
# Ask better
- Define the goal and relevant files.
- Specify how to verify the result.
- Correct early and clear between unrelated tasks.
=== test
? Which request better defines the work?
* Add login validation in auth.ts and check empty inputs
- Improve the entire project without details
- Read every generated file
! A specific goal and location guide the search.
? Why set a verification goal?
* To check whether the result meets the request
- To guarantee there are no errors
- To avoid reviewing the result
! An observable check helps evaluate the solution.
? What can /clear do between unrelated tasks?
* Clear the previous context
- Automatically restore the previous task
- Run every test
! It avoids carrying the previous task's context forward.
? What does asking for a diff imply?
* It narrows the requested output
- It prevents the agent from reading files
- It guarantees the code works
! The agent may still need reads and verification.
