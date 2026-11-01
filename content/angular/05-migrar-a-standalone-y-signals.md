---
title: Migrar Angular a standalone y signals
desc: Migrar Angular a standalone y signals requiere revisar imports y proveedores; aplica las migraciones oficiales por etapas y valida cada cambio.
pkgs: @angular/core, @angular/cli
---
## Cómo se manifiesta
- Un componente migrado puede necesitar una revisión de sus imports.
- Puede ser necesario conservar proveedores de un NgModule.
- Algunos módulos pueden requerir cambios manuales.
- Las entradas migradas a signals deben leerse como funciones.

## Causa más probable
1. Los componentes dependen de declaraciones o proveedores de NgModule que deben conservarse.
2. La migración automática no puede resolver todos los casos.
3. Una entrada convertida en signal debe leerse como función.

## Arreglo
1. Parte de una rama limpia y un proyecto que compile. Consulta los requisitos de la migración oficial.
2. Ejecuta tres veces el schematic desde el workspace, seleccionando en orden convertir declaraciones, eliminar NgModules innecesarios y cambiar el arranque a APIs standalone:
```bash
ng generate @angular/core:standalone
```
Revisa los cambios y comprueba compilación y comportamiento entre etapas. Algunos módulos requieren intervención manual; conserva los proveedores necesarios.
3. Las signals son una migración independiente y opcional. Para migrar entradas compatibles:
```bash
ng generate @angular/core:signal-input-migration
```
Revisa las entradas omitidas y sus usos. Una entrada migrada se lee invocándola:
```ts
import {Component, input} from '@angular/core';

@Component({selector: 'app-saludo', template: '<p>Hola {{ nombre() }}</p>'})
export class SaludoComponent {
  readonly nombre = input('');
}
```

> [!NOTE] Comprueba tu versión
> Los requisitos de los schematics y la disponibilidad de las APIs dependen de la versión de Angular. Consulta ambas guías antes de ejecutar comandos.

## Cómo comprobar que está arreglado
Ejecuta la compilación, el lint y las pruebas del proyecto. Recorre rutas, formularios y servicios afectados; revisa los módulos y entradas que la migración no haya podido modificar.

## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Directiva no disponible | Imports del componente standalone |
| Servicio no disponible | Proveedores y alcance del inyector |
| Entrada omitida | Usos incompatibles y notas del schematic |

> [!AI] Con IA
> Comparte la versión, el log completo, el diff de cada etapa y el componente, módulo o entrada afectada. Pide que distinga standalone de signals.

Fuente: [migración standalone](https://angular.dev/reference/migrations/standalone) y [migración de entradas signal](https://angular.dev/reference/migrations/signal-inputs).

Relacionado: [errores de inyección](@/angular/nullinjectorerror-y-errores-de-inyeccion).

=== esquema
# Migración
- Preparar — rama limpia y compilación correcta.
- Convertir — tres etapas standalone con comprobaciones.
- Adoptar — migrar entradas signal por separado y revisar.
=== test
? ¿Cuántas etapas ordenadas tiene la migración standalone?
* Tres
- Una
- Ninguna
! Ejecuta el schematic para cada etapa.
? ¿Qué pasa con los casos que el schematic no resuelve?
* Requieren revisión manual
- Siempre se borran sin consecuencias
- Se publican automáticamente
! Revisa los cambios tras cada etapa.
? ¿Cómo se lee una entrada signal?
* Llamándola como función
- Asignando un NgModule
- Cambiando el nombre del fichero
! Por ejemplo, nombre().
? ¿Es obligatoria la migración a signals para usar standalone?
* No, es independiente
- Sí, siempre
- Solo en pruebas
! Son decisiones separadas.
