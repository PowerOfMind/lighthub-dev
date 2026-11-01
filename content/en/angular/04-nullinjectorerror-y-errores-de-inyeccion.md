---
title: NullInjectorError: No provider for a service in Angular
desc: NullInjectorError: No provider for means Angular cannot find a provider; follow the injection chain and register the correct token.
pkgs: @angular/core
---
## Symptom
```text
No provider for <token> found
```
NG0201 appears when a service is injected without a declared provider.

```text
inject() must be called from an injection context
```
NG0203 appears when `inject()` is called outside an injection context.

## Most likely causes
1. The requested token has no provider.
2. The provider exists outside the consumer's injector hierarchy.
3. A different token was registered from the one being injected.

## Fix
1. Read the dependency chain in the error and find the missing token.
2. For your own shared service, provide it at the root:
```ts
import {Injectable} from '@angular/core';

@Injectable({providedIn: 'root'})
export class UserService {}
```
3. For a token or library service, follow its documentation and register its provider in the right injector. In a standalone application this can be done at bootstrap:
```ts
bootstrapApplication(AppComponent, {
  providers: [provideHttpClient()]
});
```
Import `bootstrapApplication` from `@angular/platform-browser`, `provideHttpClient` from `@angular/common/http` and your application's root component. Do not add providers blindly: their scope determines which instance is shared.

> [!NOTE] Check your version
> Available bootstrap and configuration APIs depend on the version and whether the application uses NgModule or standalone.

For NG0203, move `inject()` to the constructor or a field initializer; constructor parameters and provider factories are also allowed. It cannot be called in methods or lifecycle hooks such as `ngOnInit` after the instance is created. In tests use `TestBed.runInInjectionContext`. For HttpClient, configure `provideHttpClient()` or `HttpClientModule` in an NgModule.

## How to verify the fix
Repeat the failing route or test, verify the service works and check provider configuration in tests too.

## If that was not the cause
| Possible cause | What to check |
|---|---|
| Circular dependency | The chain and NG0200 diagnostic |
| `inject()` outside a context | NG0203 and where it is called |
| Interface token | Use an InjectionToken with a provider |

> [!AI] With AI
> Share the Angular version, full error and injection chain, service declaration and component, application or test providers.

Source: [NG0201](https://angular.dev/errors/NG0201) and [dependency injection debugging](https://angular.dev/guide/di/debugging-and-troubleshooting-di).

Related: [migrate to standalone and signals](@/angular/migrar-a-standalone-y-signals).

=== esquema
# Injection
- Identify — read the token and chain.
- Provide — register in the right injector.
- Verify — repeat the flow and tests.
=== test
? What does NG0201 mean?
* An accessible provider for a token is missing
- A stylesheet is missing
- HTML has a syntax error
! Check the token and hierarchy.
? What does providedIn root supply?
* A root provider for the service
- A visual component
- An HTTP request
! Scope determines sharing.
? What does NG0200 indicate?
* A circular dependency
- A correct HTTP provider
- A missing translation file
! Follow the dependency chain.
? Where should you look if only a test fails?
* Its providers
- The page title
- The browser colour
! The test has its own configuration.
