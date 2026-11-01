---
title: What are tokens and the context window?
desc: Learn what tokens are, why conversation context grows with each turn, and how prompt caching changes the cost of repeated input.
---
A token is a unit the model uses to process content; it is not necessarily a word. The context window is its working memory: it includes input and the generated response, not its training data.

## Why input grows
When a conversation retains its history, each turn sends the current message along with earlier ones. It is like rereading a whole book before adding a sentence: today's answer becomes part of the next turn's input.

System instructions, messages, images, documents, tool definitions and results all count, as does output including thinking. More context does not guarantee better answers: accuracy and recall can degrade as it grows, a phenomenon called *context rot*.

## What caching changes
Caching can reduce the cost of reading a repeated prefix, but those tokens still occupy the window. Select relevant context and remove what is no longer needed.

> [!NOTE] Simulation
> The exercise compares relative input cost units, not a bill. It assumes an identical prefix is available in cache; real conditions can prevent a hit.

Source: [context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows), [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
=== esquema
# Context
- Input — history and current message.
- Output — response and thinking.
- Cache — changes cost, not space used.
=== test
? What is the context window?
* Working memory available for input and output
- All training data
- Only the last message
! It includes input and the response.
? What happens to retained history?
* It is sent again in later turns
- It disappears automatically each turn
- It never occupies context
! Accumulated history increases input.
? What does caching do to the window?
* Cached tokens still occupy it
- It expands it
- It removes the response
! Caching affects cost, not space.
? What is context rot?
* Possible degradation of accuracy and recall as context grows
- A kind of password
- Deletion of training data
! Select relevant information.
=== prueba

## Context accumulation simulator
Every turn resends the whole history. Change the numbers and compare the accumulated input; with the cache box ticked you get a relative estimate that applies 1.25x to new tokens and 0.1x to already-cached ones (documented ratios for most models). It is a simulation, not a bill.
```html
<label for="turns">Turns</label><input id="turns" type="number" min="1" max="100" value="5">
<label for="user">Tokens per user message</label><input id="user" type="number" min="0" max="100000" value="100">
<label for="answer">Tokens per response</label><input id="answer" type="number" min="0" max="100000" value="200">
<label><input id="cache" type="checkbox"> Compare with caching</label>
<button id="run">Calculate</button><div id="result" aria-live="polite"></div>
```
```js
document.getElementById('run').addEventListener('click', () => {
  const read = id => Number(document.getElementById(id).value);
  const n = read('turns'), u = read('user'), a = read('answer');
  const out = document.getElementById('result');
  if (![n, u, a].every(Number.isInteger) || n < 1 || n > 100 || u < 0 || a < 0 || u > 100000 || a > 100000) { out.textContent = 'Enter whole numbers within the limits.'; return; }
  let total = 0, cachedCost = 0, previous = 0, cachedPrefix = 0;
  const rows = [];
  for (let i = 1; i <= n; i++) {
    const input = previous + u;
    total += input;
    cachedCost += cachedPrefix * 0.1 + (input - cachedPrefix) * 1.25;
    rows.push(`<li>Turn ${i}: ${input} input tokens</li>`);
    cachedPrefix = input;
    previous = input + a;
  }
  out.innerHTML = `<ul>${rows.join('')}</ul><p>Total input without caching: ${total} tokens.</p>` + (document.getElementById('cache').checked ? `<p>Simulated relative cost: without cache ${total}; with cache ${cachedCost.toFixed(2)} units. Assumes writes at 1.25× and reads at 0.1× for most models; this is not a bill.</p>` : '');
});
```
Reto: raise the turns from 5 to 20 and see that the accumulated input grows much faster than the number of turns.
Clave: the whole conversation is resent every turn; clearing context between tasks saves the most.
