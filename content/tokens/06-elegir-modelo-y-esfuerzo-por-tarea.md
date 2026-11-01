---
title: ¿Qué modelo y nivel de esfuerzo elegir para ahorrar tokens?
desc: Elige modelo y esfuerzo en Claude Code según la tarea, controla el pensamiento y evita gastar de más con un modelo grande por defecto.
---
Elige el modelo y el esfuerzo según la dificultad de la tarea. Un modelo más potente no siempre es necesario y dejar Opus por defecto puede elevar el gasto de sesiones y subagentes.

## Una decisión práctica
| Tarea | Punto de partida |
|---|---|
| Cambios habituales de código | Sonnet resuelve la mayoría de estas tareas y cuesta menos que Opus |
| Decisiones de arquitectura complejas | Valora Opus |
| Trabajo sencillo delegado | Puedes indicar `model: haiku` en el subagente |
| Logs o documentación extensa | Delega el análisis y pide un resumen verificable |

Cambia de modelo durante la sesión con `/model`. El valor predeterminado se configura en `/config`. Un cambio a Opus también afecta a los subagentes que heredan el modelo de la sesión; comprueba esa elección antes de delegar. Los subagentes también consumen uso.

## Ajusta el pensamiento
El pensamiento extendido está activado por defecto y sus tokens se facturan como salida. Reduce el esfuerzo con `/effort` o en `/model` cuando la tarea no requiera tanta profundidad. En `/config` se puede desactivar el pensamiento, aunque algunos modelos recientes no permiten hacerlo. En modelos con presupuesto fijo existe `MAX_THINKING_TOKENS`, por ejemplo `MAX_THINKING_TOKENS=8000`.

> [!TIP] Comprueba el resultado
> Un nivel menor puede ahorrar trabajo, pero verifica la respuesta y aumenta el esfuerzo si no resuelve el problema. Compara el uso en tareas similares.

Fuente: [costes de Claude Code](https://code.claude.com/docs/en/costs), [ventanas de contexto](https://platform.claude.com/docs/en/build-with-claude/context-windows), [precios actuales](https://platform.claude.com/docs/en/about-claude/pricing).
=== esquema
# Modelo y esfuerzo
- Elegir — adapta el modelo a la dificultad.
- Ajustar — `/model` y `/effort` controlan la sesión.
- Verificar — revisa resultados y uso, también en subagentes.
=== test
? ¿Qué modelo propone la guía para decisiones complejas de arquitectura?
* Opus
- Siempre Haiku
- Ninguno
! Opus es una opción para decisiones complejas.
? ¿Cómo se facturan los tokens de pensamiento?
* Como salida
- Nunca se facturan
- Solo como almacenamiento
! El pensamiento se factura como salida.
? ¿Qué puede ocurrir al cambiar a Opus?
* Los subagentes que heredan el modelo también pueden usarlo
- Todos los subagentes dejan de consumir uso
- Se borra el historial
! Comprueba la configuración de los subagentes.
? ¿Qué comando permite cambiar de modelo durante la sesión?
* `/model`
- `/mcp`
- `/context`
! `/model` cambia el modelo de la sesión.
