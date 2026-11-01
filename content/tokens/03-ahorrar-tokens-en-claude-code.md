---
title: Cómo ahorrar tokens en Claude Code
desc: Reduce el uso de Claude Code con tareas concretas, limpieza de contexto, compactación, elección de modelo y revisión temprana.
---
Para ahorrar tokens en Claude Code, separa las tareas, limita lo que pides y revisa pronto el trabajo. El historial se reenvía en cada petición, así que una sesión larga puede consumir más incluso si el cambio es pequeño.

## Hábitos por orden de impacto
1. Usa `/clear` entre tareas no relacionadas. Antes, usa `/rename` para identificar la sesión y `/resume` para volver a ella cuando la necesites.
2. Acota el encargo: «añade validación de entrada a la función de login en auth.ts» evita una exploración tan amplia como «mejora el proyecto». Incluye cómo comprobar el resultado.
3. Si necesitas conservar el hilo, usa `/compact Focus on code samples and API usage` y adapta las instrucciones a lo que importa conservar. Compactar también consume tokens.
4. Revisa `/context` y usa `/mcp` para desactivar servidores innecesarios. Cambia de modelo con `/model` y ajusta el esfuerzo con `/effort` según la dificultad.
5. Para trabajo complejo, entra en modo plan con Shift+Tab. Detén un rumbo incorrecto con Escape y usa `/rewind` o doble Escape para volver a un punto anterior.

## Delegar con criterio
Los subagentes pueden resumir salidas largas sin llenar la conversación principal, aunque también consumen uso. Los equipos de agentes consumen aproximadamente siete veces los tokens de una sesión estándar cuando los compañeros están en modo plan; reserva esa opción para tareas que la justifiquen.

> [!AI] Con IA
> Pide un cambio concreto y una comprobación observable; revisa el plan antes de autorizar una exploración extensa.

Fuente: [costes de Claude Code](https://code.claude.com/docs/en/costs).
=== esquema
# Ahorrar
- Separar — limpia entre tareas.
- Acotar — concreta archivo, objetivo y verificación.
- Medir — revisa contexto, modelo y herramientas.
=== test
? ¿Qué comando limpia entre tareas independientes?
* /clear
- /model
- /mcp
! /clear elimina el contexto de la sesión actual.
? ¿Cómo puedes volver a una sesión identificada?
* Con /resume
- Con /effort
- Con Escape
! Usa /rename para identificarla antes.
? ¿Qué muestra el consumo de contexto?
* /context
- /rename
- /rewind
! /context muestra qué ocupa espacio.
? ¿Consumen uso los subagentes?
* Sí
- No
- Solo si se renombra la sesión
! Su resumen reduce la salida en la conversación principal, pero su trabajo consume uso.
