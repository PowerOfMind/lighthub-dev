---
tipo: error
title: Push notifications do not arrive in Expo
desc: Push notifications do not arrive in Expo when permissions, token or credentials are missing; check delivery and the installed build.
pkgs: expo, expo-notifications, expo-constants
---
## Symptom
```text
Project ID not found
```
The official example throws this error when the EAS projectId is missing. When notification permission is not granted, it displays:
```text
Failed to get push token for push notification!
```
## Most likely cause
1. Permission is denied or no valid token was obtained for the installation.
2. Android FCM or iOS APNs credentials are missing or do not match the app.
3. The test environment is incompatible or the service returns a sending or delivery error.
## Fix
1. Install the libraries from the project root:
```bash
npx expo install expo-notifications expo-constants
```
2. Follow the official example to create the Android channel, check and request permission, and obtain an `ExpoPushToken` with the EAS `projectId`. Check the result before sending it to your server; do not automatically ask again if the system says it cannot prompt again.
3. Configure Firebase Cloud Messaging for Android and an APNs key for iOS using Expo's guides. Manage credentials with `eas credentials` and create a new development build.
4. Install the build on a supported device, obtain a token and send a test with Expo's notifications tool. Inspect tickets and receipts if sending or delivery fails.
> [!NOTE] Check your version
> Remote push notifications are unavailable in Expo Go on Android from SDK 53; local notifications still work. Use a development build.
### Push errors
Inspect the `details` property of the ticket or receipt.

| Code | Meaning and action |
|---|---|
| DeviceNotRegistered | The device can no longer receive pushes; stop sending to that token. |
| MessageTooBig | Payload exceeds 4096 bytes; reduce it. |
| MessageRateExceeded | Sending too frequently; use exponential backoff. |
| MismatchSenderId | Check that the FCM server key and sender ID in google-services.json match. |
| InvalidCredentials | Check invalid or revoked credentials. |
| TOO_MANY_REQUESTS | Stay within 600 notifications per second per project. |
| PUSH_TOO_MANY_EXPERIENCE_IDS | Check the experience IDs in the request. |
| PUSH_TOO_MANY_NOTIFICATIONS | Send at most 100 notifications per request. |
| PUSH_TOO_MANY_RECEIPTS | Request at most 1000 receipts per request. |
| UNAUTHORIZED | When push security is enabled, supply a valid access token. |

On iOS, `No valid aps-environment entitlement string found` indicates that no iOS push key is configured. Check Project Credentials and run `eas build --profile [profile] --platform ios`. On Android, create a notification channel before calling `getExpoPushTokenAsync` or `getDevicePushTokenAsync`, so the permission prompt can appear.

## How to check the fix
With permission granted, send a test notification to that installation's token. Check the ticket, receipt and arrival on each platform; also test the distribution build with its credentials.
## If that was not it
| Possible cause | What to check |
|---|---|
| Permission denied | System notification settings |
| Expired token | Service receipt and updated registration |
| No foreground display | Notification handler configuration |
> [!AI] With AI
> Provide SDK, platform, build type, permission status and complete sending and receipt logs. Redact tokens and credentials.
Source: [push setup](https://docs.expo.dev/push-notifications/push-notifications-setup/), [sending and receipts](https://docs.expo.dev/push-notifications/sending-notifications/), [troubleshooting](https://docs.expo.dev/push-notifications/faq/).
Related: [Expo and publishing](@/react-native/expo-eas-y-publicar).
=== esquema
# Notifications
- Prepare — install libraries and request permission.
- Configure — FCM and APNs for each platform.
- Verify — token, send, receipt and device.
=== test
? What does Expo's service need to address a push?
* ExpoPushToken
- A component path
- The editor name
! The token identifies the destination.
? Which service handles Android push?
* Firebase Cloud Messaging
- CocoaPods
- Metro
! Android requires FCM configuration.
? What should you inspect when a push does not arrive?
* Tickets and receipts
- Only the icon colour
- Only the README
! Receipts help identify delivery errors.
? What should you redact from shared logs?
* Tokens and credentials
- The platform
- The SDK version
! Do not share sensitive data.
