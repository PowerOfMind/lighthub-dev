---
title: How to reduce tokens in your API app
desc: Reduce application token usage: count input, limit output, keep only useful history and process requests in batches when appropriate.
---
To reduce token usage, measure input before sending it and remove content that does not help the task. Limit output with `max_tokens` and compare the result against a quality baseline.

## Before sending
The token counting API estimates a message's tokens before submission. Include instructions, tools and results; trim tool results to relevant material without removing errors needed for diagnosis.

## Control history and output
`max_tokens` limits output; thinking also counts towards that limit. Summarise long histories while preserving decisions, constraints and facts that need verification. Context editing can clear old tool results and thinking blocks; server-side compaction is in beta.

| Symptom | Possible cause | Fix |
|---|---|---|
| Growing input | Turns and results accumulate | Summarise and keep what matters |
| Truncated response | Output limit too low | Adjust `max_tokens` and check the result |
| Many non-urgent requests | Independent work | Consider batch processing |

## Retrieve relevant material
RAG retrieves relevant passages and adds them to context instead of including every document. It can reduce input, but poor retrieval can miss necessary information: evaluate retrieval and answers against real examples.

The batch API processes requests asynchronously at a 50% discount. It suits evaluations that do not need immediate answers; check retention conditions before using sensitive data.

> [!AI] With AI
> Ask which parts of the history are essential and review the summary before removing the originals.

Source: [Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting), [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) and [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing).

=== esquema
# Reduce
- Count input and trim tool results.
- Summarise history and adjust output.
- Evaluate RAG and use batches when appropriate.
=== test
? What does token counting allow?
* Estimating input before sending it
- Guaranteeing answer quality
- Removing the need for a context window
! It lets you measure before sending.
? What does max_tokens include?
* Output, including thinking
- Only tool results
- Only input
! Thinking is part of the output limit.
? When are batches useful?
* When an immediate response is not needed
- When every request needs an immediate response
- When requests cannot run asynchronously
! Batches are asynchronous.
? What is a RAG risk?
* Retrieval may miss necessary information
- Retrieval is guaranteed to be correct
- Evaluation is unnecessary
! Evaluate both retrieval and the answer.
