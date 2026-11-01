---
title: Por qué se agota el límite de Claude Code
desc: Identifica los límites de sesión, semanales y por modelo de Claude Code, y descubre cuándo cambiar de modelo o cuándo esperar.
---
Claude Code puede alcanzar un límite de uso de la suscripción aunque aún quede espacio de contexto. El mensaje indica qué límite se ha alcanzado y cuándo se reinicia; consulta `/usage` para ver el uso del plan.

## Identifica el aviso
| Síntoma | Causa | Arreglo |
|---|---|---|
| `You've hit your session limit` | Límite de la ventana de sesión compartido entre modelos | Espera al reinicio; cambiar de modelo no lo restablece. |
| `You've hit your weekly limit` | Límite semanal compartido entre modelos | Espera al reinicio; cambiar de modelo no lo restablece. |
| `You've hit your Opus limit` o `You've hit your Sonnet limit` | Límite de esa familia | Usa `/model` para elegir otra familia. |
| Aviso de contexto o compactación | La conversación ocupa mucho espacio | Compacta o inicia otra tarea; no es un límite de uso. |

En Teams y Enterprise, las ventanas de uso se comparten entre Claude chat, Claude Code y Cowork. Con inicio de sesión de claude.ai, `/usage-credits` permite usar créditos de uso adicionales; también puedes esperar al reinicio.

## Por qué aumenta el uso
En una sesión larga se reenvía el historial en cada petición. La caché puede abaratar su lectura, pero también influyen los fallos de caché, subagentes, equipos y tareas en segundo plano. Compactar una conversación grande también requiere procesarla.

> [!TIP] Separa tareas
> Usa `/clear` entre tareas sin relación y consulta `/usage` para observar la diferencia.

Fuente: [costes de Claude Code](https://code.claude.com/docs/en/costs).
=== esquema
# Límites
- Sesión y semana — cambiar de modelo no reinicia el límite compartido.
- Familia — otra familia puede seguir disponible.
- Contexto — es distinto del límite de uso.
=== test
? ¿Qué muestra el uso del plan?
* /usage
- /rewind
- /rename
! Consulta /usage.
? ¿Reinicia /model el límite semanal compartido?
* No
- Sí, siempre
- Solo al compactar
! Espera al reinicio indicado.
? ¿Qué puede ayudar ante un límite específico de Opus?
* Elegir otra familia con /model
- Reenviar el mismo mensaje
- Cambiar el nombre de la sesión
! Otra familia puede estar disponible.
? ¿Es un aviso de compactación un límite de uso?
* No
- Sí, siempre
- Solo en sesiones cortas
! La ventana de contexto y el uso son conceptos distintos.
