---
title: Rechazo por permisos y configuración nativa en Expo
desc: Revisa rechazos por permisos y configuración nativa en Expo, consulta el aviso de la tienda y prepara y prueba una nueva build.
pkgs: expo, react-native
---
## Cómo se manifiesta
- La tienda rechaza la aplicación durante la revisión.
- El aviso de revisión señala cuestiones que necesitan atención.
- La aplicación puede ser retirada si los permisos están mal configurados o no se explican.

## Causas más probables
1. Los permisos mal configurados o sin explicar pueden provocar un rechazo o una retirada.
2. Google puede rechazar permisos peligrosos que no estén justificados.

## Arreglo
1. Lee el aviso completo y revisa cada motivo en la consola de la tienda.
2. Comprueba los permisos solicitados y explica su uso. En iOS, adapta los mensajes de los plugins y configura los textos en `ios.infoPlist`; en Android, bloquea los permisos añadidos por paquetes que no necesites mediante `android.blockedPermissions`.
3. Consulta las directrices de revisión de Apple y la política de permisos y el Centro de ayuda de Play Console. Si cambias la configuración nativa, genera una nueva build antes de enviarla.

Existen otras causas de rechazo: lee el motivo literal del aviso de la tienda y consulta la guía oficial correspondiente.

| Otras causas | Qué revisar |
|---|---|
| Otros problemas de revisión | El aviso literal y la guía oficial de la tienda |

## Cómo comprobar que está arreglado
Repite el flujo afectado en la plataforma correspondiente y comprueba el resultado.

Fuente: [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [Expo: permisos](https://docs.expo.dev/guides/permissions/).

=== esquema
# Proceso
- Identificar — localizar el flujo afectado.
- Ajustar — aplicar la configuración o corrección pertinente.
- Comprobar — repetir el flujo afectado.
=== test
? ¿Qué debe revisarse primero?
* El aviso completo de la tienda
- Solo el registro de Metro
- Solo el nombre de la aplicación
! El aviso contiene los motivos concretos.
? ¿Qué permisos puede rechazar Google si no se justifican?
* Permisos peligrosos
- Solo permisos bloqueados
- Únicamente permisos de iOS
! La página señala los permisos peligrosos sin justificar.
? ¿Cómo se bloquean permisos no deseados añadidos por paquetes en Android?
* Con android.blockedPermissions
- Con ios.infoPlist
- Con una actualización OTA
! La configuración permite bloquearlos.
? ¿Qué hacer tras cambiar la configuración nativa?
* Generar una nueva build antes de enviarla
- Enviar la misma build sin cambios
- Limpiar solo la caché del navegador
! La nueva configuración requiere otra build.
