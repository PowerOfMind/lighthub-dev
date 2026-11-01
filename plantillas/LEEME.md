# Cómo añadir un tema nuevo a LightHub Dev

Tienes contenido (apuntes, un error que has resuelto, una idea) y quieres que acabe en la web. Solo hay que darle formato.

## 1. Elige el tipo de página
| Tipo | Úsalo para | Plantilla |
|---|---|---|
| `error` | Un error concreto o una migración: síntoma, causa, arreglo | [error.md](error.md) |
| `guia` | Un concepto, una comparativa, una lista de hábitos o pasos | [guia.md](guia.md) |

## 2. Crea los ficheros (ES y EN a la vez)
```bash
python tools/nueva_pagina.py <seccion> <slug> --tipo error --titulo "Título tal como lo buscaría la gente"
```
Crea `content/<seccion>/NN-slug.md` y `content/en/<seccion>/NN-slug.md` con el siguiente número libre. Secciones existentes: las carpetas de `content/` (por ejemplo `react`, `react-native`, `angular`, `tokens`, `ia`, `seguridad`, `seo-geo`, `lit`, `js-ts`, `atascado`, `librerias`).

Si la sección es nueva, regístrala en `build.py`, en la lista `secs` de ES y de EN: `("carpeta", "Nombre visible", "Descripción corta")`.

## 3. Rellena los TODO
Pega tu contenido en la plantilla. Si quieres que lo haga una IA, dale este encargo (cambia lo que va entre corchetes):

> Formatea el contenido de abajo siguiendo EXACTAMENTE la plantilla `plantillas/[error|guia].md` de LightHub Dev. Reglas: título = lo que escribiría la persona en Google; `desc` de 120 a 155 caracteres, única y empezando por el síntoma o el tema; mensajes de error y comandos solo si están en el contenido que te paso o en la documentación oficial (no inventes ninguno; si no hay mensaje literal, usa «Cómo se manifiesta» en lugar de «Síntoma»); línea «Fuente:» con enlaces oficiales; `=== esquema` y `=== test` con 3 a 6 preguntas, una sola respuesta correcta marcada con `*` y distractores plausibles; versión EN natural (no traducida palabra por palabra) con los mensajes de error sin traducir. Contenido: [pega aquí]

## 4. Valida y construye
```bash
python tools/validar.py
python build.py -W error
```
`validar.py` comprueba cabecera, `desc` (120-155 caracteres y única), TODO sin rellenar, esquema, test (una `*` por pregunta, mínimo 3), pareja ES/EN, BOM y enlaces internos. `build.py` falla si hay un enlace interno roto.

## 5. Publica
Commit y `git push origin main`: Vercel construye y publica solo (el proyecto `lighthub-dev` está conectado al repositorio).

## Formato rápido
- Cabecera: `title`, `desc` y, si hay paquetes npm, `pkgs: a, b` (los vigila el flujo semanal de novedades).
- Avisos: `> [!TIP] Título` / `[!WARN]` / `[!AI]` / `[!SEC]` / `[!NOTE]`, en líneas que empiezan por `>`.
- Enlaces internos: `(@/seccion/slug)` sin número ni `.md`. Externos, normales.
- Código: bloques con lenguaje (` ```js `, ` ```bash `, ` ```text `, ` ```jsx `).
- Test: `? pregunta`, `* correcta`, `- incorrecta`, `! explicación`.
- Esquema: `# Bloque` y `- Concepto — frase corta`.
- Prueba ejecutable (opcional): `=== prueba`, cada ejemplo con `## Título`, descripción, bloques ` ```html ` y ` ```js ` (o ` ```jsx ` para React y React Native) y, si quieres, `Reto:` y `Clave:`.
- Guarda siempre en UTF-8 **sin BOM** (el validador avisa).

## Reglas de contenido
- Solo hechos que puedas comprobar en la documentación oficial. Si dudas, omítelo.
- Mensajes de error literales en bloque ` ```text `; si no los tienes, descríbelo en prosa.
- Sin precios ni versiones concretas salvo que sean de una fuente oficial y la página diga la fecha; usa el aviso «Comprueba tu versión».
- No contar secretos reales: tokens y claves siempre ocultos.
