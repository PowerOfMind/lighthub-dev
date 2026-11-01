---
title: Las notificaciones push no llegan en Expo
desc: Las notificaciones push no llegan en Expo si faltan permisos, el token o las credenciales; comprueba el envío y la build instalada.
pkgs: expo, expo-notifications, expo-constants
---
## Síntoma
```text
Project ID not found
```
El ejemplo oficial lanza este error si falta el projectId de EAS. Si no se concede el permiso de notificaciones, muestra:
```text
Failed to get push token for push notification!
```
## Causa más probable
1. El permiso está denegado o no se ha obtenido un token válido para la instalación.
2. Faltan credenciales de FCM para Android o de APNs para iOS, o no corresponden a la aplicación.
3. Se prueba con un entorno incompatible o el servicio devuelve un error de envío o entrega.
## Arreglo
1. Instala las bibliotecas desde la raíz:
```bash
npx expo install expo-notifications expo-constants
```
2. Sigue el ejemplo oficial para crear el canal de Android, consultar y solicitar permisos y obtener el `ExpoPushToken` con el `projectId` de EAS. Comprueba el resultado antes de enviarlo a tu servidor; no solicites de nuevo automáticamente si el sistema indica que no puede volver a preguntar.
3. Configura Firebase Cloud Messaging para Android y la clave de APNs para iOS siguiendo las guías de Expo. Usa `eas credentials` para gestionar las credenciales y crea una development build nueva.
4. Instala la build en un dispositivo compatible, obtén un token y envía una prueba con la herramienta de notificaciones de Expo. Revisa tickets y recibos si el envío falla o no se entrega.
> [!NOTE] Comprueba tu versión
> Las notificaciones push remotas no están disponibles en Expo Go en Android desde SDK 53; las locales sí funcionan. Usa una development build.
### Errores de push
Revisa la propiedad `details` del ticket o recibo.

| Código | Significado y acción |
|---|---|
| DeviceNotRegistered | El dispositivo ya no puede recibir push; deja de enviar a ese token. |
| MessageTooBig | El payload supera 4096 bytes; reduce su tamaño. |
| MessageRateExceeded | Envíos demasiado frecuentes; usa backoff exponencial. |
| MismatchSenderId | Comprueba que coincidan la clave de servidor FCM y el sender ID de google-services.json. |
| InvalidCredentials | Revisa las credenciales inválidas o revocadas. |
| TOO_MANY_REQUESTS | Respeta el límite de 600 notificaciones por segundo por proyecto. |
| PUSH_TOO_MANY_EXPERIENCE_IDS | Revisa los identificadores de experiencia de la petición. |
| PUSH_TOO_MANY_NOTIFICATIONS | Envía como máximo 100 notificaciones por petición. |
| PUSH_TOO_MANY_RECEIPTS | Solicita como máximo 1000 recibos por petición. |
| UNAUTHORIZED | Si la seguridad de push está activada, proporciona un token de acceso válido. |

En iOS, `No valid aps-environment entitlement string found` indica que no hay una clave de push de iOS configurada. Revisa Project Credentials y ejecuta `eas build --profile [profile] --platform ios`. En Android, crea un canal de notificaciones antes de llamar a `getExpoPushTokenAsync` o `getDevicePushTokenAsync` para que pueda aparecer el diálogo de permiso.

## Cómo comprobar que está arreglado
Con permiso concedido, envía una notificación de prueba al token de esa instalación. Comprueba el ticket, el recibo y la llegada en cada plataforma; prueba también la build de distribución con sus credenciales.
## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Permiso denegado | Ajustes de notificaciones del sistema |
| Token caducado | Recibo del servicio y registro actualizado |
| No aparece en primer plano | Configuración del manejador de notificaciones |
> [!AI] Con IA
> Comparte SDK, plataforma, tipo de build, estado del permiso y logs completos de envío y recibo. Oculta tokens y credenciales.
Fuente: [configuración de push](https://docs.expo.dev/push-notifications/push-notifications-setup/), [envío y recibos](https://docs.expo.dev/push-notifications/sending-notifications/), [diagnóstico](https://docs.expo.dev/push-notifications/faq/).
Relacionado: [Expo y publicación](@/react-native/expo-eas-y-publicar).
=== esquema
# Notificaciones
- Preparar — instalar bibliotecas y solicitar permiso.
- Configurar — FCM y APNs para cada plataforma.
- Verificar — token, envío, recibo y dispositivo.
=== test
? ¿Qué necesita el servicio de Expo para dirigir el envío?
* ExpoPushToken
- La ruta de un componente
- El nombre del editor
! El token identifica el destino del envío.
? ¿Qué servicio usa Android para push?
* Firebase Cloud Messaging
- CocoaPods
- Metro
! Android requiere configurar FCM.
? ¿Qué se revisa si el envío no llega?
* Tickets y recibos
- Solo el color del icono
- Solo el README
! Los recibos ayudan a detectar errores de entrega.
? ¿Qué debe ocultarse al compartir logs?
* Tokens y credenciales
- La plataforma
- La versión del SDK
! No compartas datos sensibles.
