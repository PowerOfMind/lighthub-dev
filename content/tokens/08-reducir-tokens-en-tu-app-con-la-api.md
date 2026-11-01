---
title: Cómo reducir tokens en tu app con la API
desc: Reduce los tokens de tu aplicación: cuenta la entrada, limita la salida, conserva solo el historial útil y procesa por lotes cuando puedas.
---
Para reducir tokens, mide la entrada antes de enviarla y elimina contenido que no ayude a resolver la tarea. Limita la salida con `max_tokens` y compara el resultado con una referencia de calidad.

## Antes de enviar
La API de conteo permite estimar los tokens de un mensaje antes de enviarlo. Cuenta también instrucciones, herramientas y resultados; recorta los resultados de herramientas a lo relevante, sin quitar errores necesarios para diagnosticar el problema.

## Controla el historial y la salida
`max_tokens` limita la salida; el pensamiento también forma parte de ese límite. Resume el historial cuando sea largo y conserva decisiones, restricciones y datos que deban verificarse. La edición de contexto puede limpiar resultados de herramientas y bloques de pensamiento antiguos; la compactación del servidor está en beta.

| Síntoma | Causa posible | Arreglo |
|---|---|---|
| Entrada creciente | Se acumulan turnos y resultados | Resume y conserva lo necesario |
| Respuesta truncada | Límite de salida insuficiente | Ajusta `max_tokens` y comprueba el resultado |
| Muchas peticiones sin urgencia | Trabajo independiente | Valora procesarlo por lotes |

## Recuperar solo lo relevante
RAG busca fragmentos pertinentes y los añade al contexto en vez de incluir todos los documentos. Puede reducir la entrada, pero una búsqueda deficiente puede omitir información necesaria: evalúa la recuperación y la respuesta con ejemplos reales.

La API de lotes procesa peticiones de forma asíncrona con un descuento del 50 %. Es útil para evaluaciones sin respuesta inmediata; revisa las condiciones de retención antes de usar datos sensibles.

> [!AI] Con IA
> Pide que identifique qué fragmentos del historial son imprescindibles y revisa el resumen antes de eliminar los originales.

Fuente: [Conteo de tokens](https://platform.claude.com/docs/en/build-with-claude/token-counting), [ventana de contexto](https://platform.claude.com/docs/en/build-with-claude/context-windows) y [lotes](https://platform.claude.com/docs/en/build-with-claude/batch-processing).

=== esquema
# Reducir
- Cuenta la entrada y recorta resultados de herramientas.
- Resume el historial y ajusta la salida.
- Evalúa RAG y usa lotes cuando no haya urgencia.
=== test
? ¿Qué permite el conteo de tokens?
* Estimar la entrada antes de enviarla
- Garantizar la calidad de la respuesta
- Eliminar la necesidad de una ventana de contexto
! Permite medir antes de enviar.
? ¿Qué incluye el límite max_tokens?
* La salida, incluido el pensamiento
- Solo los resultados de herramientas
- Solo la entrada
! El pensamiento forma parte del límite de salida.
? ¿Cuándo encajan los lotes?
* Cuando no hace falta respuesta inmediata
- Cuando cada petición necesita respuesta inmediata
- Cuando no se pueden procesar peticiones de forma asíncrona
! Los lotes son asíncronos.
? ¿Qué riesgo tiene RAG?
* La búsqueda puede omitir información necesaria
- Garantiza que toda recuperación es correcta
- Elimina toda necesidad de evaluar
! Evalúa tanto la recuperación como la respuesta.
