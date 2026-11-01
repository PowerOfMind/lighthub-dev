---
title: ¿Cómo funciona prompt caching en la API de Claude?
desc: Aprende a reutilizar prefijos con prompt caching en la API de Claude, interpretar usage y evitar fallos de caché y costes inesperados.
---
Prompt caching reutiliza un prefijo idéntico entre peticiones para reducir el coste de volver a procesarlo. Hay que activar la caché, mantener estable el prefijo y comprobar los campos de uso: no todos los prompts alcanzan el mínimo cacheable.

## Activa la caché
Para caché automática, añade al nivel superior de la petición:
```json
"cache_control": {"type": "ephemeral"}
```
El punto de corte se mueve al último bloque cacheable. También puedes colocar `cache_control` en bloques concretos para fijar los cortes: hay hasta cuatro por petición y el automático utiliza uno. El prefijo sigue el orden `tools`, `system`, `messages`, hasta el bloque marcado. Los segmentos deben ser idénticos para obtener un acierto.

## Duración y coste relativo
| Duración | Escritura respecto a entrada base | Lectura |
|---|---|---|
| 5 minutos, por defecto | 1,25 veces | 0,1 veces para la mayoría de modelos |
| 1 hora | 2 veces | 0,1 veces para la mayoría de modelos |

Algunos modelos recientes tienen un multiplicador de lectura menor; consulta los precios actuales. Cada uso refresca la duración sin coste extra. Para una hora usa `"cache_control": {"type": "ephemeral", "ttl": "1h"}`. Si mezclas duraciones, coloca las entradas de una hora antes que las de cinco minutos.

El mínimo cacheable depende del modelo: puede ser 512, 1.024, 2.048 o 4.096 tokens. Por debajo, la petición se procesa sin caché y sin error. Consulta la documentación para el mínimo del modelo elegido.

## Evita fallos y mide
Cambiar definiciones de herramientas invalida `tools`, `system` y `messages`; activar o desactivar búsqueda web, citas o velocidad invalida `system` y `messages`. Cambiar `tool_choice` o añadir o quitar imágenes invalida `messages`. Los cambios en parámetros de pensamiento también invalidan la caché. Mantén el material compartido estable y coloca lo variable después.

En `usage`, suma `cache_read_input_tokens` (lectura), `cache_creation_input_tokens` (escritura) e `input_tokens` (entrada posterior al último corte, no leída ni escrita en caché) para obtener la entrada total. Si ambos campos de caché son cero, el prompt no se cacheó; puede ser demasiado corto. La caché cambia el coste, pero los tokens siguen contando para la ventana de contexto.

Para precalentar el prefijo compartido se puede usar `max_tokens: 0` y `cache_control`. La entrada solo está disponible una vez empieza la primera respuesta: espera antes de lanzar peticiones paralelas que dependan de ese acierto.

> [!TIP] Mide con tu tráfico
> Compara lecturas y escrituras en `usage`: una escritura sin reutilización suficiente puede no compensar. Las cifras son multiplicadores de entrada, no una factura completa.

Fuente: [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), [ventanas de contexto](https://platform.claude.com/docs/en/build-with-claude/context-windows), [precios](https://platform.claude.com/docs/en/about-claude/pricing).
=== esquema
# Caché de prompt
- Activar — usa `cache_control` automático o por bloque.
- Reutilizar — conserva idéntico el prefijo y respeta mínimos y duración.
- Medir — revisa lectura, escritura y entrada en `usage`.
=== test
? ¿Qué exige un acierto de caché?
* Segmentos del prefijo idénticos
- Cambiar siempre las herramientas
- Que el prompt sea diferente
! El prefijo cacheado debe coincidir.
? ¿Cuál es la duración predeterminada?
* Cinco minutos
- Una semana
- No caduca
! El uso refresca la duración sin coste extra.
? ¿Qué pasa si el prompt no alcanza el mínimo cacheable?
* Se procesa sin caché y sin error
- Se rechaza siempre
- Se guarda indefinidamente
! El mínimo depende del modelo.
? ¿Qué campo indica tokens leídos de caché?
* `cache_read_input_tokens`
- `cache_creation_input_tokens`
- `max_tokens`
! El campo de creación indica escritura, no lectura.
? ¿Reduce la caché los tokens que cuentan para la ventana?
* No, siguen contando
- Sí, desaparecen de la ventana
- Solo si dura una hora
! La caché cambia el coste, no el espacio contabilizado.
