---
tipo: error
title: Librería incompatible con la Nueva Arquitectura de React Native
desc: Comprueba la compatibilidad de una librería con la Nueva Arquitectura de React Native y conoce las opciones para resolver el problema.
pkgs: expo, react-native
---
## Cómo se manifiesta
- Una función que depende de una librería deja de funcionar.
- El problema aparece al usar la Nueva Arquitectura.
- La librería puede depender de funciones que la capa de interoperabilidad no cubre.

## Causas más probables
1. La capa de interoperabilidad es automática, pero no admite Shadow Nodes personalizados ni funciones concurrentes.
2. Una librería puede no ser compatible con la Nueva Arquitectura.

## Arreglo
1. Comprueba la compatibilidad en [React Native Directory](https://reactnative.directory).
2. Si no es compatible, abre una incidencia o busca una alternativa mantenida.
3. Como medida temporal, solo si tu versión aún lo permite, desactiva la Nueva Arquitectura: en Android, establece `newArchEnabled=false` en `android/gradle.properties`; en iOS, ejecuta `RCT_NEW_ARCH_ENABLED=0 bundle exec pod install`. La capa de interoperabilidad se eliminará en el futuro.

> [!NOTE] Comprueba tu versión
> Esta opción procede de un blog de octubre de 2024 y puede no funcionar en versiones recientes. Con generación nativa continua (prebuild), `android/gradle.properties` se regenera; revisa la configuración del proyecto.

## Cómo comprobar que está arreglado
Repite el flujo afectado en la plataforma correspondiente y comprueba el resultado.

Fuente: [React Native](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here).

=== esquema
# Proceso
- Identificar — localizar el flujo afectado.
- Ajustar — aplicar la configuración o corrección pertinente.
- Comprobar — repetir el flujo afectado.
=== test
? ¿Dónde se comprueba la compatibilidad de una librería?
* En React Native Directory
- En el registro de Metro exclusivamente
- En la consola de la tienda
! El directorio permite consultar compatibilidad.
? ¿Qué no admite la capa de interoperabilidad?
* Shadow Nodes personalizados
- Todas las librerías nativas
- La configuración de Android
! La página también menciona funciones concurrentes.
? ¿Qué hacer ante una librería incompatible?
* Abrir una incidencia o buscar una alternativa mantenida
- Suponer que la capa cubre todas sus funciones
- Eliminar todos los permisos nativos
! Busca una solución mantenida.
? ¿Cuándo puede probarse la desactivación temporal?
* Si la versión todavía la admite
- En cualquier versión sin comprobar
- Solo cambiando un mensaje de permisos
! Comprueba la versión y la generación nativa.
