---
title: How does prompt caching work in the Claude API?
desc: Learn to reuse prefixes with Claude API prompt caching, interpret usage fields and prevent cache misses and unexpected costs.
---
Prompt caching reuses an identical prefix across requests to reduce the cost of processing it again. Enable caching, keep the prefix stable and check usage fields: not every prompt reaches the cacheable minimum.

## Enable caching
For automatic caching, add this at the top level of the request:
```json
"cache_control": {"type": "ephemeral"}
```
The breakpoint moves to the last cacheable block. You can also put `cache_control` on specific blocks to set breakpoints: a request supports up to four, and automatic caching uses one. The prefix follows the order `tools`, `system`, `messages`, up to the marked block. Segments must be identical for a cache hit.

## Lifetime and relative cost
| Lifetime | Write relative to base input | Read |
|---|---|---|
| 5 minutes, the default | 1.25 times | 0.1 times for most models |
| 1 hour | 2 times | 0.1 times for most models |

Some recent models have an even lower read multiplier; check current pricing. Each use refreshes the lifetime at no extra cost. For one hour use `"cache_control": {"type": "ephemeral", "ttl": "1h"}`. If you mix lifetimes, put one-hour entries before five-minute entries.

The cacheable minimum depends on the model: it can be 512, 1,024, 2,048 or 4,096 tokens. Below that, the request is processed without caching or an error. Check the documentation for your model's minimum.

## Prevent misses and measure
Changing tool definitions invalidates `tools`, `system` and `messages`; toggling web search, citations or speed invalidates `system` and `messages`. Changing `tool_choice` or adding or removing images invalidates `messages`. Changes to thinking parameters also invalidate the cache. Keep shared material stable and put variable material afterward.

In `usage`, add `cache_read_input_tokens` (reads), `cache_creation_input_tokens` (writes) and `input_tokens` (input after the last breakpoint, neither read nor written to cache) to get total input. If both cache fields are zero, the prompt was not cached; it may be too short. Caching changes the cost, but those tokens still count toward the context window.

To prewarm a shared prefix, you can use `max_tokens: 0` and `cache_control`. The cache entry is available only after the first response begins, so wait before launching parallel requests that depend on that hit.

> [!TIP] Measure your traffic
> Compare reads and writes in `usage`: a write may not pay off without enough reuse. These figures are input multipliers, not a complete invoice.

Source: [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [pricing](https://platform.claude.com/docs/en/about-claude/pricing).
=== esquema
# Prompt caching
- Enable — use automatic or block-level `cache_control`.
- Reuse — keep the prefix identical and respect minimums and lifetime.
- Measure — check reads, writes and input in `usage`.
=== test
? What does a cache hit require?
* Identical prefix segments
- Changing tools every time
- A different prompt
! The cached prefix must match.
? What is the default lifetime?
* Five minutes
- One week
- It never expires
! Usage refreshes the lifetime at no extra cost.
? What happens below the cacheable minimum?
* The request is processed without caching or an error
- It is always rejected
- It is cached indefinitely
! The minimum depends on the model.
? Which field reports tokens read from cache?
* `cache_read_input_tokens`
- `cache_creation_input_tokens`
- `max_tokens`
! The creation field reports writes, not reads.
? Does caching reduce the tokens counted toward the window?
* No, they still count
- Yes, they disappear from the window
- Only with a one-hour lifetime
! Caching changes cost, not the space counted.
