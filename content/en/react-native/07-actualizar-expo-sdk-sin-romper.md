---
title: Upgrade Expo SDK without breaking the app
desc: Upgrading Expo SDK can break dependencies or native projects; review the release notes and check compatibility before shipping the app.
pkgs: expo, react-native
---
## How it shows up
- Dependency compatibility warnings appear after the SDK upgrade.
- A native build fails after the upgrade.
- A library needs changes for the target SDK.
- The installed native projects need updating.

## Most likely cause
1. Dependency versions still match the previous SDK.
2. Native projects do not reflect the SDK changes.
3. A library or configuration needs a change described in the release notes.

## Fix
1. Save your changes and read the release notes for every SDK you will cross. Expo recommends upgrading one SDK version at a time.
2. Install the `expo` version for the target SDK as described in its guide. Then, from the project root:
```bash
npx expo install --fix
npx expo-doctor
```
3. Review the package manager changes and address Doctor's warnings. If you use continuous native generation, follow Expo's instructions to regenerate native directories. If you maintain `ios` and `android` manually, apply the relevant native changes and run `npx pod-install` for iOS.
4. Apply any additional release-note instructions and create new native builds.

> [!NOTE] Check your version
> The target version determines the required dependencies and native changes. Read its release notes before changing the project.

## How to check the fix
Run Doctor again, review remaining warnings and test a new build on each platform you distribute. Exercise features that use native modules.

## If that was not it
| Possible cause | What to check |
|---|---|
| Incompatible library | Library support for the SDK and chosen architecture |
| Custom native changes | Changes that must be retained before regeneration |
| Incompatible Expo Go | Project SDK and Expo Go version |

> [!AI] With AI
> Provide the source and target SDKs, package manager, complete Doctor and build logs, and whether you maintain native projects. Remove credentials from logs.

Source: [Upgrade Expo SDK](https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough/).

Related: [Expo and publishing](@/react-native/expo-eas-y-publicar).

=== esquema
# Migration
- Prepare — read each SDK's release notes.
- Align — install compatible dependencies and run Doctor.
- Validate — update native projects and test new builds.
=== test
? Which command aligns dependencies with the installed SDK?
* npx expo install --fix
- npx expo start
- npx pod-install
! Expo install checks and fixes compatible versions.
? Which tool checks common project problems?
* Expo Doctor
- The browser
- The text editor
! Expo Doctor checks configuration and dependencies.
? Where are version-specific changes documented?
* The target SDK release notes
- Only the Git history
- Only CSS documentation
! Release notes include changes and additional steps.
? What should you test after native changes?
* A new native build
- Only a screenshot
- Only the README text
! Test the build on the platforms you distribute.
