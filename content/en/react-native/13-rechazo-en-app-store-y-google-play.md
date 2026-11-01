---
title: Store rejection for permissions and native configuration in Expo
desc: Review store rejection notices involving permissions and native configuration in Expo, then prepare and test a new build.
pkgs: expo, react-native
---
## How it shows up
- The store rejects the app during review.
- The review notice identifies issues requiring attention.
- The app may be removed if permissions are misconfigured or unexplained.

## Most likely causes
1. Misconfigured or unexplained permissions can lead to rejection or removal.
2. Google may reject dangerous permissions that lack justification.

## Fix
1. Read the complete notice and review each reason in the store console.
2. Check the requested permissions and explain their use. On iOS, adapt plugin messages and configure usage text in `ios.infoPlist`; on Android, block unwanted permissions added by packages with `android.blockedPermissions`.
3. Consult Apple’s review guidelines and Google Play’s permission policy and Play Console Help Center. If you change native configuration, create a new build before submitting it.

Other causes can lead to rejection: read the exact store notice and consult the relevant official guidance.

| Other causes | What to check |
|---|---|
| Other review issues | The exact notice and the store’s official guidance |

## How to verify the fix
Repeat the affected flow on the relevant platform and check the result.

Source: [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [Expo permissions](https://docs.expo.dev/guides/permissions/).

=== esquema
# Workflow
- Inspect — identify the affected flow.
- Adjust — apply the relevant configuration or fix.
- Verify — repeat the affected flow.
=== test
? What should you review first?
* The complete store notice
- Only the Metro log
- Only the application name
! The notice contains the specific reasons.
? Which unjustified permissions can Google reject?
* Dangerous permissions
- Only blocked permissions
- Only iOS permissions
! The page identifies unjustified dangerous permissions.
? How do you block unwanted Android permissions added by packages?
* With android.blockedPermissions
- With ios.infoPlist
- With an OTA update
! The configuration can block them.
? What follows a native configuration change?
* Create a new build before submission
- Resubmit the same unchanged build
- Clear only the browser cache
! The new configuration requires another build.
