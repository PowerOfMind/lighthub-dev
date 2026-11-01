---
title: Hydration failed en Next.js
desc: Hydration failed en Next.js aparece cuando el HTML inicial del servidor y el cliente difieren; identifica la causa y corrige el render.
pkgs: next, react, react-dom
---
## Síntoma
```text
Text content does not match server-rendered HTML
```
El texto exacto que ves en consola puede variar según la versión; la documentación de Next.js lo titula así.
Aparece cuando el árbol de React prerenderizado en el servidor difiere del primer render del navegador.

## Causa más probable
1. El primer render usa valores que cambian, como la hora, o datos exclusivos del navegador.
2. El HTML tiene elementos mal anidados y el navegador modifica el árbol.
3. Una extensión o una capa intermedia modifica el HTML antes de hidratarlo.

## Arreglo
1. Localiza en el error el componente y compara la salida del servidor con el primer render del navegador.
2. Haz que ambos produzcan el mismo contenido inicial. Si el dato solo existe en el navegador, léelo después del montaje:
```jsx
'use client';
import {useEffect, useState} from 'react';

export default function ZonaHoraria() {
  const [zona, setZona] = useState('Cargando');
  useEffect(() => setZona(Intl.DateTimeFormat().resolvedOptions().timeZone), []);
  return <p>{zona}</p>;
}
```
3. Corrige el anidamiento HTML y evita condiciones basadas en `window` durante el render inicial.

También puedes usar `next/dynamic` con `{ ssr: false }` para contenido exclusivo del cliente. `suppressHydrationWarning={true}` es una salida de emergencia: solo afecta a un nivel y React no intenta corregir el texto.

## Cómo comprobar que está arreglado
Recarga la página directamente y comprueba la consola y la salida inicial. Repite sin extensiones y en una build de producción.

## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| HTML inválido | Anidamiento de párrafos y elementos interactivos |
| CSS-in-JS | Configuración de renderizado en servidor de la biblioteca |
| HTML modificado | Extensiones y configuración del CDN |

> [!AI] Con IA
> Aporta versiones, log completo, componente mínimo y HTML inicial del servidor; indica si hay extensiones o CDN.

Fuente: [error de hidratación de Next.js](https://nextjs.org/docs/messages/react-hydration-error).

Relacionado: [window is not defined](@/react/window-is-not-defined-y-use-client).

=== esquema
# Hidratación
- Comparar — servidor y primer render del navegador.
- Corregir — contenido inicial estable y HTML válido.
- Comprobar — recargar y revisar la consola.
=== test
? ¿Qué debe coincidir al hidratar?
* El HTML del servidor y el primer render del cliente
- Las extensiones instaladas
- La hora de todos los usuarios
! React espera contenido inicial coincidente.
? ¿Cuándo se ejecuta useEffect?
* Después del montaje en el cliente
- Durante el render del servidor
- Antes de crear HTML en el servidor
! Permite leer datos del navegador tras el montaje.
? ¿Qué puede alterar el HTML antes de hidratar?
* Una extensión del navegador
- Un comentario de código
- El nombre del fichero
! Prueba también sin extensiones.
? ¿Qué hacer con HTML mal anidado?
* Corregir la estructura
- Ocultar siempre el aviso
- Eliminar las pruebas
! El navegador puede corregir el árbol de forma distinta.
