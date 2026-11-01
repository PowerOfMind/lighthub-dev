---
title: window is not defined en Next.js
desc: window is not defined aparece al usar APIs del navegador en el servidor de Next.js; mueve el acceso al cliente y comprueba el render inicial.
pkgs: next, react
---
## Cómo se manifiesta
La ruta falla con un ReferenceError sobre `window`.
- Una ruta falla al renderizarse en el servidor.
- Una dependencia puede fallar al importarse.
- Los datos exclusivos del navegador no están disponibles durante el render en servidor.
- Un contenido inicial diferente puede provocar un error de hidratación.

Un error distinto aparece al usar un hook de cliente en un Server Component; la documentación de Next.js lo recoge bajo el título «React client hook in Server Component».
Añade `'use client'` al principio del fichero que usa el hook.

## Causa más probable
1. El código accede a `window` durante el render en servidor.
2. Una dependencia accede a `window` al importarse.
3. Un Client Component también se prerenderiza y accede a `window` durante el render inicial.

## Arreglo
1. Identifica el acceso en la traza. En App Router, marca el componente interactivo con `use client` al principio del fichero.
2. Mueve la lectura a un efecto o a un manejador de eventos, no al cuerpo del render:
```jsx
'use client';
import {useEffect, useState} from 'react';

export default function Ancho() {
  const [ancho, setAncho] = useState(null);
  useEffect(() => setAncho(window.innerWidth), []);
  return <p>{ancho === null ? 'Cargando' : ancho}</p>;
}
```
3. Si una biblioteca falla al importarse, consulta la carga diferida de Next.js y desactiva el prerenderizado del componente cliente que la contiene cuando sea necesario.

> [!NOTE] Comprueba tu versión
> `use client` y las opciones de carga dependen del router y de la versión de Next.js.

## Cómo comprobar que está arreglado
Recarga la ruta directamente, revisa los logs del servidor y la consola y prueba una build de producción. Comprueba también que el contenido inicial no produce errores de hidratación.

## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Acceso a nivel de módulo | Imports y código ejecutado al cargar la biblioteca |
| Diferencia en el primer render | Condiciones con `typeof window` |
| API distinta | Accesos a `document` o `localStorage` |

> [!AI] Con IA
> Comparte versiones, router, traza completa y componente mínimo, incluidos los imports. Indica si falla al renderizar o al importar.

Fuente: [componentes de servidor y cliente](https://nextjs.org/docs/app/getting-started/server-and-client-components) y [carga diferida](https://nextjs.org/docs/app/guides/lazy-loading).

Relacionado: [hydration failed](@/react/hydration-failed-en-nextjs).

=== esquema
# Navegador y servidor
- Identificar — localizar el acceso a window.
- Mover — leerlo después del montaje.
- Validar — revisar servidor, consola e hidratación.
=== test
? ¿Existe window en el servidor?
* No, es una API del navegador
- Siempre
- Solo en cada efecto del servidor
! No está disponible durante SSR.
? ¿Garantiza use client que el render inicial no se haga en servidor?
* No
- Sí, siempre
- Solo en producción
! Un Client Component puede prerenderizarse.
? ¿Dónde puede leerse window tras el montaje?
* En un efecto
- En el render del servidor
- En una importación que se ejecuta en servidor
! El efecto se ejecuta en el cliente.
? ¿Qué se debe comprobar además del error original?
* Que no haya diferencias de hidratación
- El nombre del editor
- El color del terminal
! El primer contenido debe coincidir.
