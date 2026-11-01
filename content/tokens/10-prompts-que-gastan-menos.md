---
title: Cómo escribir prompts que gastan menos tokens
desc: Escribe prompts concretos que reduzcan lecturas y repeticiones: delimita la tarea, define cómo verificarla y corrige el rumbo pronto.
---
Un prompt concreto ayuda al agente a buscar menos y evita rondas de aclaración. Indica el objetivo, el lugar donde trabajar y cómo comprobar el resultado; incluye solo el contexto necesario.

## Antes y después
| Antes | Después |
|---|---|
| «Mejora el proyecto» | «Añade validación de entrada a la función de login en auth.ts y comprueba los casos vacíos». |
| «Arregla los tests» | «Investiga el fallo de login; conserva el comportamiento esperado y ejecuta los tests relevantes». |
| «Devuelve todos los ficheros» | «Resume los cambios y muestra el diff relevante». |

Una petición acotada no garantiza menos gasto: mide el uso y revisa que la solución cubra el problema. Pedir un diff reduce la respuesta solicitada, pero el agente puede necesitar leer archivos para trabajar.

## Guía el trabajo
1. Para tareas complejas, usa el modo plan y revisa el enfoque antes de implementar.
2. Define una comprobación observable: tests relevantes, salida esperada o captura.
3. Si el agente va por mal camino, detén y corrige pronto; en Claude Code puedes usar Escape y `/rewind` para volver a un punto anterior.
4. Al cambiar a una tarea sin relación, usa `/clear`. Si necesitas retomar la anterior, usa `/rename` antes de limpiar y `/resume` para volver.

> [!AI] Con IA
> Pide al agente que reformule el objetivo y señale la información que falta antes de una tarea compleja. Comprueba que no amplíe el alcance sin necesidad.

Fuente: [Costes de Claude Code](https://code.claude.com/docs/en/costs).

=== esquema
# Pedir mejor
- Delimita objetivo y archivos pertinentes.
- Define cómo verificar el resultado.
- Corrige pronto y limpia entre tareas distintas.
=== test
? ¿Qué petición delimita mejor el trabajo?
* Añadir validación al login de auth.ts y comprobar entradas vacías
- Mejorar todo el proyecto sin más detalle
- Leer todos los archivos generados
! Un objetivo y ubicación concretos orientan la búsqueda.
? ¿Para qué sirve un objetivo de verificación?
* Para comprobar si el resultado cumple lo pedido
- Para garantizar que no haya errores
- Para evitar revisar el resultado
! Una prueba observable ayuda a evaluar la solución.
? ¿Qué puede hacer /clear entre tareas sin relación?
* Limpiar el contexto anterior
- Restaurar automáticamente la tarea anterior
- Ejecutar todos los tests
! Evita arrastrar el contexto de la tarea anterior.
? ¿Qué implica pedir un diff?
* Acota la salida solicitada
- Impide que el agente lea archivos
- Garantiza que el código funciona
! El agente aún puede necesitar lecturas y verificación.
