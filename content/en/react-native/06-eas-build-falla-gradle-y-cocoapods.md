---
title: EAS Build fails in Gradle or JavaScript bundling
desc: Diagnose EAS Build failures in Gradle or JavaScript bundling by inspecting logs, dependencies, uploaded files and configuration.
pkgs: expo, react-native
---
## Symptom
```text
Gradle build daemon disappeared unexpectedly (it may have been killed or may have crashed)
```
This Gradle error can appear when the Node process bundling JavaScript is terminated.

```text
Task :app:bundleReleaseJsAndAssets FAILED
```
On Android, this can indicate that Metro could not bundle JavaScript. On iOS, the corresponding message is:
```text
Metro encountered an error
```
## Most likely cause
1. A native dependency or plugin is incompatible or misconfigured.
2. Files or variables are missing from the EAS environment.
3. For the quoted error, the Node bundling process may have been terminated, often because of a very large bundle.
## Fix
1. Open the failed EAS phase and find the specific error before the summary; if the failure is in the iOS phase, inspect that phase’s log.
2. Run `npx expo-doctor` and address relevant warnings.
3. Compare a successful build's packages, plugins, variables and uploaded files. Run `npx expo export` to isolate JavaScript bundling.
4. For the cited daemon error, inspect bundle size with Expo Atlas; a large bundle can terminate the Node process. Set the resource class to `large` in `eas.json`.
> [!NOTE] Check your version
> SDK, plugins and native tools must be compatible; consult their release notes before changing them.
## How to check the fix
Repeat the build on the affected platform, install it and test the changed feature.
## If that was not it
| Possible cause | What to check |
|---|---|
| Missing variables | Selected EAS environment |
| Excluded file | Uploaded archive, without exposing secrets |
| Native error | Complete message in the failed phase |
> [!AI] With AI
> Provide platform, SDK, profile, recent changes and complete logs, without credentials.
Source: [EAS Build troubleshooting](https://docs.expo.dev/build-reference/troubleshooting/).
Related: [Upgrade Expo SDK](@/react-native/actualizar-expo-sdk-sin-romper).
=== esquema
# Build
- Locate — read the phase error.
- Compare — environment and dependencies.
- Validate — rebuild and test.
=== test
? What helps diagnose the build?
* The specific error in the log
- Only the phase name
- The icon
! The phase alone does not identify the cause.
? What does Expo Doctor check?
* Configuration and dependencies
- Screen design
- Bank account details
! Review its warnings.
? Why run npx expo export here?
* To isolate JavaScript bundle errors
- To create credentials
- To change the domain
! It checks the bundle separately.
? How do you validate the fix?
* Rebuild and test the app
- Close the log
- Rename the folder
! Test the resulting build too.
