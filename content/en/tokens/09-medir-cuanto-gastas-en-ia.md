---
title: How to measure your AI spending
desc: Measure Claude Code and API usage, establish a baseline and understand the difference between local estimates and actual billing.
---
To understand your spending, compare usage on a representative task with your provider's billing. In Claude Code, `/usage` shows session statistics; local dollar amounts are estimates, not the bill.

## Establish a baseline
1. Choose a repeatable task and record the model, scope and expected result.
2. Check `/usage` before and after; record tokens and cache usage. Session totals reset with `/clear`.
3. Repeat with one specific change, such as fewer unnecessary reads, and check that quality remains sufficient.
4. Compare authorised spending in the Usage page of Claude Console, or your cloud provider account if it bills the API.

Subscribers can also see plan usage bars in `/usage`. `/insights` produces a report on working patterns and consumes tokens. The cache line in `/usage` helps identify cache reads and misses.

## Measuring across a team
Claude Console supports workspace spending limits. OpenTelemetry provides per-user metrics, and an LLM gateway can help centralise usage monitoring. Decide who reviews the data and compare equivalent tasks: changing model or scope affects the comparison.

| Symptom | Possible cause | Fix |
|---|---|---|
| Usage grows during a task | Increasing history | Review context and split tasks |
| Estimate differs from bill | Local estimate uses list prices | Check Usage or your provider |
| Comparison is misleading | Scope or model changed | Record both alongside the outcome |

> [!TIP] Measure quality and cost
> A lower number is not useful if the task is incomplete or must be repeated.

Source: [Claude Code costs](https://code.claude.com/docs/en/costs) and [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing).

=== esquema
# Measure
- Establish a task and baseline.
- Check /usage and compare billing.
- Compare quality and cost at the same scope.
=== test
? What does /usage show?
* Session usage statistics
- Every provider's final bill
- Only modified code
! It shows session statistics.
? What happens to session totals after /clear?
* They reset
- They become a bill
- They remain unchanged in /usage
! Session totals reset.
? Where can you check authorised Claude API spending?
* The Usage page in Claude Console
- Only a local estimate
- Browser history
! The local estimate does not replace billing.
? What should be comparable?
* Scope, model and expected result
- Only the task name
- No conditions
! Scope and model changes affect comparisons.
