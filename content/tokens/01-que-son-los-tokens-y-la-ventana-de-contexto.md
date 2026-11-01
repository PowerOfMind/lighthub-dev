---
title: Qué son los tokens y la ventana de contexto
desc: Entiende qué son los tokens, por qué crece el contexto en cada turno y cómo influye la caché en una conversación con IA.
---
Un token es una unidad en la que el modelo procesa contenido; no equivale necesariamente a una palabra. La ventana de contexto es su memoria de trabajo: incluye la entrada y la respuesta que genera, no sus datos de entrenamiento.

## Por qué crece la entrada
En una conversación que conserva el historial, cada turno envía el mensaje actual junto con los anteriores. Es como releer un libro entero antes de añadir una frase: la respuesta de hoy también formará parte de la entrada de mañana.

Cuentan las instrucciones de sistema, mensajes, imágenes, documentos, definiciones y resultados de herramientas, además de la salida, incluido el pensamiento. Más contexto no garantiza mejores respuestas: al crecer puede empeorar la precisión y el recuerdo, fenómeno llamado *context rot*.

## Qué cambia la caché
La caché puede reducir el coste de leer un prefijo repetido, pero esos tokens siguen ocupando ventana. Selecciona el contexto relevante y elimina lo que ya no haga falta.

> [!NOTE] Simulación
> La prueba compara unidades de coste de entrada, no una factura. Supone un prefijo idéntico y disponible en caché; las condiciones reales pueden impedir un acierto.

Fuente: [ventanas de contexto](https://platform.claude.com/docs/en/build-with-claude/context-windows), [caché de prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
=== esquema
# Contexto
- Entrada — historial y mensaje actual.
- Salida — respuesta y pensamiento.
- Caché — cambia el coste, no el espacio ocupado.
=== test
? ¿Qué es la ventana de contexto?
* La memoria de trabajo disponible para entrada y salida
- Los datos de entrenamiento completos
- Solo el último mensaje
! Incluye la entrada y la respuesta.
? ¿Qué ocurre con el historial conservado?
* Se vuelve a enviar en turnos posteriores
- Desaparece automáticamente en cada turno
- Nunca ocupa contexto
! El historial acumulado aumenta la entrada.
? ¿Qué hace la caché con la ventana?
* Los tokens cacheados siguen ocupándola
- La amplía
- Elimina la respuesta
! La caché afecta al coste, no al espacio.
? ¿Qué es context rot?
* La posible degradación de precisión y recuerdo con más contexto
- Un tipo de contraseña
- La eliminación del entrenamiento
! Conviene seleccionar información relevante.
=== prueba

## Simulador de acumulación de contexto
Cada turno reenvía todo el historial. Cambia los números y compara la entrada acumulada; con la casilla de caché verás una estimación relativa que aplica 1,25x a lo nuevo y 0,1x a lo ya cacheado (ratios documentados para la mayoría de modelos). Es una simulación, no una factura.
```html
<label for="turns">Turnos</label><input id="turns" type="number" min="1" max="100" value="5">
<label for="user">Tokens por mensaje de usuario</label><input id="user" type="number" min="0" max="100000" value="100">
<label for="answer">Tokens por respuesta</label><input id="answer" type="number" min="0" max="100000" value="200">
<label><input id="cache" type="checkbox"> Comparar con caché</label>
<button id="run">Calcular</button><div id="result" aria-live="polite"></div>
```
```js
document.getElementById('run').addEventListener('click', () => {
  const read = id => Number(document.getElementById(id).value);
  const n = read('turns'), u = read('user'), a = read('answer');
  const out = document.getElementById('result');
  if (![n, u, a].every(Number.isInteger) || n < 1 || n > 100 || u < 0 || a < 0 || u > 100000 || a > 100000) { out.textContent = 'Introduce valores enteros dentro de los límites.'; return; }
  let total = 0, cachedCost = 0, previous = 0, cachedPrefix = 0;
  const rows = [];
  for (let i = 1; i <= n; i++) {
    const input = previous + u;
    total += input;
    cachedCost += cachedPrefix * 0.1 + (input - cachedPrefix) * 1.25;
    rows.push(`<li>Turno ${i}: ${input} tokens de entrada</li>`);
    cachedPrefix = input;
    previous = input + a;
  }
  out.innerHTML = `<ul>${rows.join('')}</ul><p>Entrada acumulada sin caché: ${total} tokens.</p>` + (document.getElementById('cache').checked ? `<p>Coste relativo simulado: sin caché ${total}; con caché ${cachedCost.toFixed(2)} unidades. Supone escritura a 1,25× y lectura a 0,1× para la mayoría de modelos; no es una factura.</p>` : '');
});
```
Reto: sube los turnos de 5 a 20 y observa que la entrada acumulada crece mucho más rápido que el número de turnos.
Clave: la conversación se reenvía entera en cada turno; limpiar el contexto entre tareas es lo que más ahorra.
