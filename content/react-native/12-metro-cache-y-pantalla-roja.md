---
tipo: error
title: Metro muestra una pantalla roja y los cambios no aparecen
desc: Revisa una pantalla roja de Metro, identifica errores de importación y aprende a limpiar la caché en Expo o React Native CLI.
pkgs: expo, react-native
---
## Cómo se manifiesta
- La aplicación muestra una pantalla roja al cargar.
- Los cambios recientes no aparecen en la aplicación.
- La terminal o la pantalla muestra información sobre el problema.

## Causas más probables
1. Un error de importación puede impedir cargar el bundle.
2. Metro puede conservar datos de caché obsoletos.

## Arreglo
1. Lee el error completo en la pantalla y la terminal y revisa la importación o el archivo indicado.
2. En Expo, detén Metro y ejecuta `npx expo start --clear`. En React Native CLI, usa `npm start -- --reset-cache` o `yarn start -- --reset-cache`.
3. En macOS o Linux, la guía también indica `watchman watch-del-all`, `rm -rf $TMPDIR/metro-cache` y `rm -fr $TMPDIR/haste-map-*` para limpiar datos relacionados.

## Cómo comprobar que está arreglado
Repite el flujo afectado en la plataforma correspondiente y comprueba el resultado.

Fuente: [Expo](https://docs.expo.dev/troubleshooting/clear-cache-macos-linux/).

=== esquema
# Proceso
- Identificar — localizar el flujo afectado.
- Ajustar — aplicar la configuración o corrección pertinente.
- Comprobar — repetir el flujo afectado.
=== test
? ¿Qué revisar primero ante una pantalla roja?
* El error completo y el archivo señalado
- Solo la versión del sistema operativo
- Solo los permisos de la tienda
! El mensaje ayuda a localizar el problema.
? ¿Qué comando limpia la caché en Expo?
* npx expo start --clear
- npx expo-doctor
- eas credentials
! Reinicia Expo limpiando la caché.
? ¿Qué opción limpia la caché con React Native CLI?
* npm start -- --reset-cache
- npm start -- --clear
- npx expo start --reset-cache
! La guía ofrece también la variante con yarn.
? ¿Qué puede impedir cargar el bundle?
* Un error de importación
- Un cambio en el texto de permisos de iOS
- Una incidencia de revisión en la tienda
! Revisa el import indicado.
