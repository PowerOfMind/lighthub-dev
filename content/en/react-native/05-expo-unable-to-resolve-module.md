---
tipo: error
title: Unable to resolve module in Expo
desc: Unable to resolve module in Expo prevents bundling; check the import path, package installation and files uploaded to the EAS build.
pkgs: expo, react-native
---
## Symptom
```text
Unable to resolve module ./src/Routes ...
```
This example appears when Metro cannot resolve an imported path.
## Most likely cause
1. The import path or letter case does not match the file.
2. The package is not installed.
3. A local file is missing from the EAS build archive.
## Fix
1. Compare the reported import with the actual path and correct names and letter case.
2. For a package, run `npx expo install package-name`, replacing the placeholder with the module name.
3. If only EAS fails, check `.gitignore`: EAS does not upload ignored files. Remove an unused import, use a file environment variable for a secret, or include a non-secret file with `.easignore`.
4. Restart Metro with a clear cache:
```bash
npx expo start --clear
```
> [!NOTE] Check your version
> Native dependencies must match the SDK; review `npx expo-doctor`.
## How to check the fix
Open the affected route. If EAS failed, repeat the build and inspect the bundle phase.
## If that was not it
| Possible cause | What to check |
|---|---|
| Alias | Path configuration |
| Monorepo | Dependencies and files available to the app |
| Generated file | Generation step before bundling |
> [!AI] With AI
> Provide Expo and Node versions, the import, file tree and complete log, without secrets.
Source: [build troubleshooting](https://docs.expo.dev/build-reference/troubleshooting/), [clearing cache](https://docs.expo.dev/troubleshooting/clear-cache-macos-linux/).
Related: [Upgrade Expo SDK](@/react-native/actualizar-expo-sdk-sin-romper).
=== esquema
# Diagnosis
- Import — check path and case.
- Dependency — install with Expo.
- EAS — check uploaded files.
=== test
? What helps locate the import?
* The file identified by Metro
- The app icon
- The Apple certificate
! Metro identifies the importing file.
? Which command clears Metro's cache?
* npx expo start --clear
- eas credentials
- npx expo-doctor
! It restarts Metro with a clear cache.
? What should you check if only EAS fails?
* Files excluded from upload
- Icon colour
- Screen size
! EAS needs the imported files.
? What should you check when an import fails only on EAS?
* Whether the import matches the file name and case
- Whether the app uses a development build
- Whether Expo Doctor is installed globally
! Import paths must match file names and case.
