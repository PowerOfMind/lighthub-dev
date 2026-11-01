---
title: Deep links do not open the screen in Expo Router
desc: Deep links do not open the screen in Expo Router when the scheme, route or domain association does not match the installed app.
pkgs: expo, expo-router
---
## How it shows up
- A link opens in the browser instead of the app.
- The app opens without reaching the intended screen.
- A custom scheme does not open the installed app.
- An HTTPS link does not open the associated app.
## Most likely cause
1. The link's scheme or path does not match the configuration or route files.
2. The installed build does not contain the new native configuration.
3. For HTTPS links, the domain and app association is missing.
## Fix
1. Define the scheme in `app.json`, replacing the example with your app's scheme:
```json
{ "expo": { "scheme": "myapp" } }
```
2. Create and install a new development build. Check that the link path matches an Expo Router screen and test `myapp://` followed by that path.
3. For iOS Universal Links, configure `ios.associatedDomains` and host `/.well-known/apple-app-site-association` on your domain with the correct team, identifier and paths.
4. For Android App Links, configure `android.intentFilters` and host `/.well-known/assetlinks.json` with the package and signing certificate fingerprint. Follow the official guides for both file formats and verification.
> [!NOTE] Check your version
> Native configuration and test tools depend on the SDK and operating system. Expo Go has limited support for incoming links.
## How to check the fix
Install the new build and open a link to an existing route with the app closed and open. Test HTTPS links on each platform and verify the domain association; check the website when the app is absent.
## If that was not it
| Possible cause | What to check |
|---|---|
| Wrong route | Expo Router files and parameters |
| Wrong association | Domain, identifiers and signing certificate |
| Old build | Install a build containing the new configuration |
> [!AI] With AI
> Provide SDK, platform, an example URL without private data, configuration, association files and complete logs without credentials.
Source: [schemes](https://docs.expo.dev/linking/into-your-app/), [Universal Links](https://docs.expo.dev/linking/ios-universal-links/), [Android App Links](https://docs.expo.dev/linking/android-app-links/).
Related: [Expo Router and navigation](@/react-native/expo-router-y-navegacion).
=== esquema
# Links
- Scheme — configure and create a new build.
- HTTPS — associate domain and app on each platform.
- Validate — test routes with the app open and closed.
=== test
? Which property defines a custom scheme?
* scheme
- title
- desc
! Set it in app config.
? What does a Universal Link require?
* An association between domain and app
- Only an icon
- Only Metro
! iOS verifies the association.
? Which file associates an Android domain?
* assetlinks.json
- package.json
- Podfile
! Host it in .well-known.
? What follows a native scheme change?
* Create and install a new build
- Change the background colour
- Delete the routes
! The installed app must contain the change.
