---
tipo: error
title: Library incompatible with React Native New Architecture
desc: Check whether a library supports React Native’s New Architecture and explore the available options for resolving incompatibility.
pkgs: expo, react-native
---
## How it shows up
- A feature that relies on a library stops working.
- The problem appears when using the New Architecture.
- The library may rely on features the interoperability layer does not support.

## Most likely causes
1. The interoperability layer is automatic, but does not support custom Shadow Nodes or concurrent features.
2. A library may be incompatible with the New Architecture.

## Fix
1. Check compatibility in [React Native Directory](https://reactnative.directory).
2. If the library is incompatible, open an issue or look for a maintained alternative.
3. As a temporary measure, only if your version still supports it, disable the New Architecture: on Android, set `newArchEnabled=false` in `android/gradle.properties`; on iOS, run `RCT_NEW_ARCH_ENABLED=0 bundle exec pod install`. The interoperability layer will be removed in the future.

> [!NOTE] Check your version
> This opt-out comes from an October 2024 blog post and may not work in recent versions. With continuous native generation (prebuild), `android/gradle.properties` is regenerated; check your project configuration.

## How to verify the fix
Repeat the affected flow on the relevant platform and check the result.

Source: [React Native](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here).

=== esquema
# Workflow
- Inspect — identify the affected flow.
- Adjust — apply the relevant configuration or fix.
- Verify — repeat the affected flow.
=== test
? Where can library compatibility be checked?
* React Native Directory
- Only the Metro log
- The store console
! The directory lists compatibility.
? What does the interoperability layer not support?
* Custom Shadow Nodes
- Every native library
- Android configuration
! The page also mentions concurrent features.
? What can you do with an incompatible library?
* Open an issue or find a maintained alternative
- Assume the layer covers every feature
- Remove all native permissions
! Look for a maintained solution.
? When can temporary opt-out be tried?
* When the version still supports it
- In every version without checking
- Only by changing a permission message
! Check the version and native generation.
