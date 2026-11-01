---
title: Cómo medir cuánto gastas en IA
desc: Aprende a medir el uso de Claude Code y la API, establecer una línea base y distinguir las estimaciones locales de la facturación real.
---
Para saber cuánto gastas, compara el uso de una tarea representativa con la facturación del proveedor. En Claude Code, `/usage` muestra estadísticas de la sesión; los importes locales son estimaciones, no la factura.

## Establece una línea base
1. Elige una tarea repetible y anota modelo, alcance y resultado esperado.
2. Consulta `/usage` antes y después; registra tokens y uso de caché. Los totales de sesión se reinician con `/clear`.
3. Repite con un cambio concreto, como reducir lecturas innecesarias, y comprueba que la calidad siga siendo suficiente.
4. Contrasta el gasto autorizado en la página Usage de Claude Console, o en la cuenta del proveedor cloud si este factura la API.

Los suscriptores también pueden ver barras de uso del plan en `/usage`. `/insights` genera un informe sobre la forma de trabajar y consume tokens. La línea de caché de `/usage` ayuda a detectar lecturas y fallos de caché.

## Medición en equipos
Claude Console permite establecer límites de gasto por workspace. OpenTelemetry aporta métricas por usuario y una pasarela LLM puede ayudar a centralizar la observación del uso. Define quién revisa los datos y compara tareas equivalentes: un cambio de modelo o alcance altera la comparación.

| Síntoma | Causa posible | Arreglo |
|---|---|---|
| Uso crece durante una tarea | Historial cada vez mayor | Revisa contexto y divide tareas |
| Estimación difiere de factura | La estimación local usa precio de lista | Consulta Usage o al proveedor |
| Comparación poco útil | Cambió el alcance o el modelo | Registra ambos junto al resultado |

> [!TIP] Mide calidad y coste
> Una cifra menor no sirve si la tarea queda incompleta o requiere repetirla.

Fuente: [Costes de Claude Code](https://code.claude.com/docs/en/costs) y [precios de Claude](https://platform.claude.com/docs/en/about-claude/pricing).

=== esquema
# Medir
- Establece una tarea y una línea base.
- Consulta /usage y contrasta la facturación.
- Compara calidad y coste con el mismo alcance.
=== test
? ¿Qué muestra /usage?
* Estadísticas de uso de la sesión
- La factura definitiva de cualquier proveedor
- Solo el código modificado
! Muestra estadísticas de la sesión.
? ¿Qué ocurre con los totales de sesión al usar /clear?
* Se reinician
- Se convierten en factura
- Se conservan sin cambios en /usage
! Los totales de sesión se reinician.
? ¿Dónde se comprueba el gasto autorizado de Claude API?
* En Usage de Claude Console
- En una estimación local exclusivamente
- En el historial del navegador
! La estimación local no sustituye a la facturación.
? ¿Qué conviene mantener comparable?
* Alcance, modelo y resultado esperado
- Solo el nombre de la tarea
- Ninguna condición
! Los cambios de alcance y modelo afectan a la comparación.
