---
title: Migrar de React 18 a React 19
desc: Migrar de React 18 a React 19 puede romper APIs obsoletas y tipos; revisa los cambios, aplica codemods y prueba la aplicación antes de publicar.
pkgs: react, react-dom
---
## Síntoma
```text
Your app (or one of its dependencies) is using an outdated JSX transform. Update to the modern JSX transform for faster performance: https://react.dev/link/new-jsx-transform
```
Este aviso aparece cuando la aplicación o una dependencia utiliza una transformación JSX antigua.

## Causa más probable
1. El código o las pruebas usan APIs que React 19 ha retirado.
2. Los tipos de TypeScript requieren ajustes, como un argumento inicial para `useRef`.
3. Una dependencia aún no es compatible con React 19.

## Arreglo
1. Revisa los avisos de la aplicación y la guía oficial antes de actualizar. Comprueba la compatibilidad de tus bibliotecas.
2. En una rama de trabajo con React 19 instalado, aplica la receta de codemods indicada por React y revisa cada cambio:
```bash
npx codemod@latest react/19/migration-recipe
```
3. Siguiendo la guía oficial, sustituye las referencias de cadena por callbacks y los usos retirados de `ReactDOM.render` por la API de raíz correspondiente.
4. Si usas TypeScript, sigue la sección de tipos de la guía: la receta anterior no incluye todos esos cambios. Por ejemplo, inicializa explícitamente la referencia:
```tsx
const inputRef = useRef<HTMLInputElement>(null);
```
5. En componentes de función, React 19 permite recibir `ref` como prop. Mantén la compatibilidad que necesiten los consumidores de tu biblioteca.

> [!NOTE] Comprueba tu versión
> `ref` como prop requiere React 19. En React 18 y anteriores se usa `forwardRef` para recibirla.

React 19 elimina `propTypes` y `defaultProps` en componentes de función, Legacy Context, las refs de cadena, `ReactDOM.render`, `ReactDOM.hydrate` y `ReactDOM.findDOMNode`. Usa `createRoot`, `hydrateRoot` y refs según corresponda. Los errores de render no capturados se notifican a `window.reportError` y los capturados a `console.error`; las raíces admiten `onUncaughtError` y `onCaughtError`. Para TypeScript, usa el codemod independiente `npx types-react-codemod@latest preset-19 ./path-to-app`.

## Cómo comprobar que está arreglado
Ejecuta el comprobador de tipos y las pruebas de tu proyecto. Prueba el montaje, las referencias y los flujos afectados en una build de producción; revisa los avisos y el sistema de registro de errores.

## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Un codemod no cubre el caso | Cambios pendientes en la guía y diff generado |
| Tipos de dependencias incompatibles | Versiones y soporte declarado por cada paquete |
| Registro de errores diferente | Cambios de gestión de errores de render en React 19 |

> [!AI] Con IA
> Aporta las versiones de React, React DOM, TypeScript y las bibliotecas afectadas, el error completo y una reproducción mínima. Pide que identifique el cambio concreto de la guía oficial.

Fuente: [guía de actualización de React 19](https://react.dev/blog/2024/04/25/react-19-upgrade-guide) y [referencias como prop](https://react.dev/blog/2024/12/05/react-19).

Relacionado: [React](@/react/react).

=== esquema
# Migración
- Revisar — identificar APIs obsoletas y dependencias.
- Transformar — ejecutar codemods y revisar el diff.
- Comprobar — validar tipos, pruebas y comportamiento.
=== test
? ¿Qué incluye la receta de migración?
* Varios codemods de APIs de React
- Todos los cambios posibles de todas las dependencias
- Una build de producción automática
! Revisa el resultado y los pasos que quedan.
? ¿Qué necesita useRef con los tipos de React 19?
* Un argumento inicial
- Una cadena obligatoria
- Un componente de clase
! Por ejemplo, usa null como valor inicial.
? ¿Cuándo está disponible ref como prop en componentes de función?
* En React 19
- En todas las versiones de React
- Solo fuera de React
! En React 18 se usa forwardRef para recibirla.
? ¿Qué debe hacerse después de ejecutar codemods?
* Revisar el diff y probar la aplicación
- Publicar sin revisar
- Borrar todas las pruebas
! Los cambios automáticos requieren revisión.
