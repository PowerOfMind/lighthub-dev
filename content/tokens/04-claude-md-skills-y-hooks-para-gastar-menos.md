---
title: Cómo usar CLAUDE.md, skills y hooks para gastar menos
desc: Reduce el contexto base de Claude Code con un CLAUDE.md breve, skills bajo demanda y filtros para salidas de herramientas.
---
Un `CLAUDE.md` breve reduce las instrucciones que Claude Code carga al iniciar cada sesión. Mueve las instrucciones específicas a skills que se cargan cuando hacen falta y filtra salidas extensas antes de enviarlas al contexto.

## Deja lo esencial en CLAUDE.md
La documentación recomienda mantenerlo por debajo de unas 200 líneas. Incluye convenciones generales, cómo comprobar el proyecto y un mapa breve; evita copiar documentación completa o instrucciones para una tarea poco frecuente.

Ejemplo de mapa, adaptado al proyecto:
```text
src/ — código de la aplicación
tests/ — pruebas
docs/ — decisiones y guías
```

Coloca el procedimiento detallado de una tarea especializada en una skill. Así el contexto base conserva solo lo necesario para orientarse.

## Filtra sin ocultar fallos
Un hook puede preprocesar datos antes de que Claude los vea. La documentación describe un hook `PreToolUse` para Bash que filtra con `grep` la salida de `npm test`, `pytest` o `go test` y conserva los fallos; consulta el ejemplo oficial y comprueba tus hooks con `/hooks`.

> [!WARN] Conserva el diagnóstico
> Comprueba que el filtro no oculte errores relevantes ni haga parecer correcta una prueba que ha fallado. Conserva acceso a la salida completa cuando necesites investigar.

> [!AI] Con IA
> Pide una propuesta para separar instrucciones generales y específicas; revisa que las reglas esenciales sigan disponibles en cada sesión.

Fuente: [costes de Claude Code](https://code.claude.com/docs/en/costs).
=== esquema
# Instrucciones y salida
- CLAUDE.md — orientaciones generales y mapa breve.
- Skills — procedimientos específicos bajo demanda.
- Hooks — preprocesar salidas y verificar el filtro.
=== test
? ¿Cuándo se carga CLAUDE.md?
* Al inicio de cada sesión
- Solo al ejecutar pruebas
- Solo al cerrar la sesión
! Se carga al iniciar cada sesión.
? ¿Dónde colocar instrucciones especializadas?
* En una skill bajo demanda
- En cada resultado de herramienta
- En el nombre del proyecto
! Las skills se cargan cuando hacen falta.
? ¿Para qué puede servir un hook?
* Para filtrar una salida extensa antes de que Claude la vea
- Para ampliar automáticamente la ventana
- Para eliminar los límites de uso
! Puede preprocesar datos.
? ¿Qué comando permite revisar hooks?
* /hooks
- /resume
- /model
! Usa /hooks para comprobarlos.
