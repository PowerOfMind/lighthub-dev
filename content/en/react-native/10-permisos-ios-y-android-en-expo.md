---
tipo: error
title: Expo does not ask for iOS or Android permissions again
desc: Learn why Expo may not ask for permissions again on iOS or Android, how to configure each platform and test a new build.
pkgs: expo, react-native
---
## How it shows up
- The permission prompt does not reappear after a denial.
- A feature that needs access cannot continue.
- The installed build does not reflect permission changes.

## Most likely causes
1. A previous denial can prevent another prompt.
2. The build may lack the required native configuration.
3. On iOS, the usage message may be missing or insufficient.

## Fix
1. On iOS, configure usage messages in `ios.infoPlist`, for example `NSCameraUsageDescription`. Adapt the default plugin messages; `expo-media-library` provides `photosPermission` and `savePhotosPermission`.
2. On Android, use `android.permissions` only for additional permissions not included by default. To remove permissions added by packages, use `android.blockedPermissions` with the full permission name.
3. Create a new build after changing native configuration: Info.plist changes cannot be delivered over the air. To test denial again, uninstall and reinstall the app.

## How to verify the fix
Repeat the affected flow on the relevant platform and check the result.

Source: [Expo](https://docs.expo.dev/guides/permissions/).

=== esquema
# Workflow
- Inspect — identify the affected flow.
- Adjust — apply the relevant configuration or fix.
- Verify — repeat the affected flow.
=== test
? Where is the iOS camera usage message configured?
* In ios.infoPlist
- In android.permissions
- In android.blockedPermissions
! Configure usage text in Info.plist.
? What blocks permissions added by Android packages?
* android.blockedPermissions
- ios.infoPlist
- android.permissions
! Use the full permission name.
? How is an Info.plist change delivered?
* With a new native build
- Through an OTA update
- By restarting Metro alone
! Native changes require a new build.
? How can you test denial again?
* Uninstall and reinstall the app
- Clear only the Metro cache
- Edit the message without rebuilding
! The page suggests reinstalling to test denial.
