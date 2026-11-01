---
title: NullInjectorError: No provider for un servicio en Angular
desc: NullInjectorError: No provider for aparece cuando Angular no encuentra un proveedor; sigue la cadena de inyección y registra el token correcto.
pkgs: @angular/core
---
## Síntoma
```text
No provider for <token> found
```
NG0201 aparece al inyectar un servicio sin proveedor declarado.

```text
inject() must be called from an injection context
```
NG0203 aparece al llamar a `inject()` fuera de un contexto de inyección.

## Causa más probable
1. Falta un proveedor para el token solicitado.
2. El proveedor existe, pero está fuera de la jerarquía del consumidor.
3. Se ha registrado un token distinto del que se inyecta.

## Arreglo
1. Lee la cadena de dependencias del error y localiza el token que falta.
2. Para un servicio propio compartido, proporciona el servicio en la raíz:
```ts
import {Injectable} from '@angular/core';

@Injectable({providedIn: 'root'})
export class UserService {}
```
3. Para un token o servicio de biblioteca, sigue su documentación y registra el proveedor en el inyector adecuado. En una aplicación standalone puede hacerse al arrancar:
```ts
bootstrapApplication(AppComponent, {
  providers: [provideHttpClient()]
});
```
Importa `bootstrapApplication` de `@angular/platform-browser`, `provideHttpClient` de `@angular/common/http` y el componente raíz de tu aplicación. No añadas proveedores a ciegas: su alcance determina qué instancia se comparte.

> [!NOTE] Comprueba tu versión
> Las APIs de arranque y configuración disponibles dependen de la versión y de si la aplicación usa NgModule o standalone.

Para NG0203, mueve `inject()` al constructor o a un inicializador de campo; también se permite en parámetros del constructor y fábricas de proveedores. No puede llamarse en métodos ni en hooks como `ngOnInit` una vez creada la instancia. En pruebas usa `TestBed.runInInjectionContext`. Para HttpClient, configura `provideHttpClient()` o `HttpClientModule` en un NgModule.

## Cómo comprobar que está arreglado
Repite la ruta o prueba que fallaba, verifica que el servicio funciona y comprueba también la configuración de proveedores en las pruebas.

## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Dependencia circular | La cadena y el diagnóstico NG0200 |
| `inject()` fuera de contexto | El diagnóstico NG0203 y dónde se llama |
| Token de interfaz | Usar un InjectionToken con proveedor |

> [!AI] Con IA
> Comparte versión de Angular, error completo y cadena de inyección, declaración del servicio y proveedores del componente, aplicación o prueba.

Fuente: [NG0201](https://angular.dev/errors/NG0201) y [depuración de inyección](https://angular.dev/guide/di/debugging-and-troubleshooting-di).

Relacionado: [migrar a standalone y signals](@/angular/migrar-a-standalone-y-signals).

=== esquema
# Inyección
- Identificar — leer el token y la cadena.
- Proporcionar — registrar en el inyector adecuado.
- Verificar — repetir el flujo y las pruebas.
=== test
? ¿Qué indica NG0201?
* Falta un proveedor accesible para un token
- Falta una hoja de estilos
- Hay un error de sintaxis HTML
! Revisa el token y la jerarquía.
? ¿Qué aporta providedIn root?
* Un proveedor del servicio en la raíz
- Un componente visual
- Una petición HTTP
! El alcance determina cómo se comparte.
? ¿Qué indica NG0200?
* Una dependencia circular
- Un proveedor HTTP correcto
- Un archivo de traducción ausente
! Sigue la cadena de dependencias.
? ¿Dónde revisar si solo falla una prueba?
* En sus proveedores
- En el título de la página
- En el color del navegador
! La prueba tiene su propia configuración.
