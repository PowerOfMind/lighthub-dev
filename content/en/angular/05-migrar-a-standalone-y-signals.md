---
title: Migrate Angular to standalone and signals
desc: Migrating Angular to standalone and signals requires reviewing imports and providers; run official migrations in stages and verify changes.
pkgs: @angular/core, @angular/cli
---
## How it shows up
- A migrated component may need its imports reviewed.
- Providers from an NgModule may need to be retained.
- Some modules may require manual changes.
- Migrated signal inputs must be read as functions.

## Most likely causes
1. Components depend on NgModule declarations or providers that must be preserved.
2. The automatic migration cannot handle every case.
3. An input converted to a signal must be read as a function.

## Fix
1. Start with a clean branch and a project that compiles. Check the official migration requirements.
2. Run the schematic three times from the workspace, selecting in order conversion of declarations, removal of unnecessary NgModules and bootstrapping with standalone APIs:
```bash
ng generate @angular/core:standalone
```
Review changes and check compilation and behaviour between stages. Some modules require manual intervention; retain required providers.
3. Signals are a separate, optional migration. To migrate compatible inputs:
```bash
ng generate @angular/core:signal-input-migration
```
Review skipped inputs and their uses. A migrated input is read by calling it:
```ts
import {Component, input} from '@angular/core';

@Component({selector: 'app-greeting', template: '<p>Hello {{ name() }}</p>'})
export class GreetingComponent {
  readonly name = input('');
}
```

> [!NOTE] Check your version
> Schematic requirements and API availability depend on the Angular version. Consult both guides before running commands.

## How to verify the fix
Run the project's build, lint and tests. Exercise affected routes, forms and services; review modules and inputs the migration could not change.

## If that was not the cause
| Possible cause | What to check |
|---|---|
| Directive unavailable | Standalone component imports |
| Service unavailable | Providers and injector scope |
| Skipped input | Incompatible uses and schematic notes |

> [!AI] With AI
> Share the version, full log, diff from each stage and affected component, module or input. Ask it to distinguish standalone from signals.

Source: [standalone migration](https://angular.dev/reference/migrations/standalone) and [signal input migration](https://angular.dev/reference/migrations/signal-inputs).

Related: [injection errors](@/angular/nullinjectorerror-y-errores-de-inyeccion).

=== esquema
# Migration
- Prepare — clean branch and working compilation.
- Convert — three standalone stages with checks.
- Adopt — migrate signal inputs separately and review.
=== test
? How many ordered stages are in the standalone migration?
* Three
- One
- None
! Run the schematic for each stage.
? What happens to cases the schematic cannot handle?
* They require manual review
- They are always deleted without consequences
- They are published automatically
! Review changes after each stage.
? How do you read a signal input?
* Call it as a function
- Assign an NgModule
- Rename the file
! For example, name().
? Must you migrate to signals to use standalone?
* No, it is separate
- Yes, always
- Only in tests
! These are separate decisions.
