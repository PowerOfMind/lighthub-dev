---
title: ¿Por qué MCP y las herramientas consumen contexto?
desc: Aprende a detectar herramientas MCP que ocupan contexto, comparar su uso con alternativas CLI y reducir lecturas innecesarias en Claude Code.
---
Las herramientas pueden ocupar parte de la ventana de contexto con sus definiciones y resultados. En Claude Code, revisa qué ocupa espacio y desactiva los servidores que no necesites para la tarea.

## Comprueba antes de quitar herramientas
Usa `/context` para ver qué consume espacio y `/mcp` para revisar los servidores configurados y desactivar los que no uses. Las definiciones de herramientas MCP se difieren por defecto: hasta que se usa una herramienta, entran en contexto solo los nombres y las instrucciones del servidor. No des por hecho que todas sus definiciones completas se cargan al empezar.

## Elige la herramienta según la tarea
Una CLI como `gh`, `aws`, `gcloud` o `sentry-cli` puede ser más eficiente en contexto porque no añade un listado por herramienta. Compara también la salida: un resultado extenso que vuelve a la conversación ocupa espacio aunque la herramienta sea útil. Un subagente puede procesar logs y devolver un resumen, aunque también consume uso.

Los plugins de inteligencia de código para lenguajes tipados permiten navegar por símbolos con precisión y evitar lecturas innecesarias de archivos.

| Síntoma | Posible causa | Arreglo |
|---|---|---|
| El contexto se llena | Resultados extensos de herramientas | Filtra la salida o pide a un subagente un resumen |
| Hay servidores innecesarios | Configuración demasiado amplia para la tarea | Revísalos con `/mcp` |
| Se leen muchos archivos | Búsqueda de texto poco precisa | Valora un plugin de inteligencia de código |

> [!AI] Con IA
> Pide un resumen de los fallos relevantes de un log, con las rutas y mensajes necesarios para verificarlos. Oculta credenciales antes de compartirlo.

Fuente: [costes de Claude Code](https://code.claude.com/docs/en/costs), [ventanas de contexto](https://platform.claude.com/docs/en/build-with-claude/context-windows).
=== esquema
# Herramientas y contexto
- Medir — `/context` muestra qué ocupa espacio.
- Revisar — `/mcp` permite gestionar servidores.
- Reducir — filtra resultados y usa navegación precisa.
=== test
? ¿Qué muestra `/context`?
* Qué consume espacio en el contexto
- La factura definitiva
- Solo los servidores desactivados
! Sirve para examinar el espacio ocupado.
? ¿Cuándo se carga la definición diferida de una herramienta MCP?
* Cuando se usa la herramienta
- Siempre al iniciar la sesión
- Solo al cerrar la sesión
! Los nombres e instrucciones del servidor sí entran antes.
? ¿Por qué una CLI puede ahorrar contexto?
* No añade un listado por herramienta
- Sus resultados nunca ocupan contexto
- Elimina toda la conversación
! La salida de una CLI también puede ocupar espacio.
? ¿Qué coste tiene delegar en un subagente?
* El subagente también consume uso
- Ninguno
- Solo consume espacio en el navegador
! Delegar puede reducir la salida en el contexto principal, pero no es gratis.
