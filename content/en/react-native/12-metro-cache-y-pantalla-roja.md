---
tipo: error
title: Metro shows a red screen and changes do not appear
desc: Investigate a Metro red screen, check import errors and learn how to clear the cache in an Expo project or the React Native CLI.
pkgs: expo, react-native
---
## How it shows up
- The app displays a red screen when loading.
- Recent changes do not appear in the app.
- The terminal or screen provides information about the problem.

## Most likely causes
1. An import error can prevent the bundle from loading.
2. Metro may retain stale cached data.

## Fix
1. Read the full error on screen and in the terminal, then inspect the indicated import or file.
2. In Expo, stop Metro and run `npx expo start --clear`. With React Native CLI, use `npm start -- --reset-cache` or `yarn start -- --reset-cache`.
3. On macOS or Linux, the guide also lists `watchman watch-del-all`, `rm -rf $TMPDIR/metro-cache` and `rm -fr $TMPDIR/haste-map-*` for clearing related data.

## How to verify the fix
Repeat the affected flow on the relevant platform and check the result.

Source: [Expo](https://docs.expo.dev/troubleshooting/clear-cache-macos-linux/).

=== esquema
# Workflow
- Inspect — identify the affected flow.
- Adjust — apply the relevant configuration or fix.
- Verify — repeat the affected flow.
=== test
? What should you inspect first on a red screen?
* The complete error and the indicated file
- Only the operating system version
- Only store permissions
! The message helps locate the problem.
? Which command clears the cache in Expo?
* npx expo start --clear
- npx expo-doctor
- eas credentials
! Restart Expo with a cleared cache.
? Which option clears the React Native CLI cache?
* npm start -- --reset-cache
- npm start -- --clear
- npx expo start --reset-cache
! The page also gives a yarn variant.
? What can prevent the bundle from loading?
* An import error
- A change to an iOS permission message
- A store review issue
! Check the indicated import.
