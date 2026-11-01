---
title: Expo no vuelve a pedir permisos en iOS o Android
desc: Descubre por qué Expo no vuelve a pedir permisos en iOS o Android, cómo configurar cada plataforma y probar una nueva build.
pkgs: expo, react-native
---
## Cómo se manifiesta
- El diálogo de permiso no vuelve a aparecer tras una denegación.
- Una función que necesita acceso no puede continuar.
- La build instalada no refleja los cambios de permisos.

## Causas más probables
1. Una denegación previa puede impedir volver a mostrar la solicitud.
2. La build puede carecer de la configuración nativa necesaria.
3. En iOS, el texto de uso puede faltar o no explicar adecuadamente el acceso.

## Arreglo
1. En iOS, configura los textos en `ios.infoPlist`, por ejemplo `NSCameraUsageDescription`. Adapta los mensajes por defecto de los plugins; `expo-media-library` ofrece `photosPermission` y `savePhotosPermission`.
2. En Android, usa `android.permissions` solo para permisos adicionales no incluidos por defecto. Para retirar permisos añadidos por paquetes, usa `android.blockedPermissions` con el nombre completo.
3. Genera una nueva build tras cambiar la configuración nativa: los cambios de Info.plist no se actualizan por OTA. Para probar de nuevo el rechazo, desinstala y reinstala la aplicación.

## Cómo comprobar que está arreglado
Repite el flujo afectado en la plataforma correspondiente y comprueba el resultado.

Fuente: [Expo](https://docs.expo.dev/guides/permissions/).

=== esquema
# Proceso
- Identificar — localizar el flujo afectado.
- Ajustar — aplicar la configuración o corrección pertinente.
- Comprobar — repetir el flujo afectado.
=== test
? ¿Dónde se configura el texto de uso de cámara en iOS?
* En ios.infoPlist
- En android.permissions
- En android.blockedPermissions
! El texto se configura en Info.plist.
? ¿Qué permite bloquear permisos añadidos por paquetes en Android?
* android.blockedPermissions
- ios.infoPlist
- android.permissions
! Usa el nombre completo del permiso.
? ¿Cómo se entrega un cambio en Info.plist?
* Con una nueva build nativa
- Mediante una actualización OTA
- Reiniciando Metro únicamente
! Los cambios nativos requieren otra build.
? ¿Cómo se puede probar de nuevo el rechazo?
* Desinstalando y reinstalando la app
- Limpiando solo la caché de Metro
- Editando el texto sin reconstruir
! La página propone reinstalar para probar el rechazo.
