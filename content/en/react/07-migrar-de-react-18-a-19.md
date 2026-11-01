---
title: Migrate from React 18 to React 19
desc: Migrating from React 18 to React 19 can break deprecated APIs and types; review the changes, apply codemods and test before shipping.
pkgs: react, react-dom
---
## Symptom
```text
Your app (or one of its dependencies) is using an outdated JSX transform. Update to the modern JSX transform for faster performance: https://react.dev/link/new-jsx-transform
```
This warning appears when the app or a dependency uses an outdated JSX transform.

## Most likely cause
1. Application or test code uses APIs removed in React 19.
2. TypeScript types need adjustments, such as an initial argument for `useRef`.
3. A dependency is not yet compatible with React 19.

## Fix
1. Review application warnings and the official guide before upgrading. Check your libraries' compatibility.
2. On a working branch, with React 19 installed, run the codemod recipe described by React and review each change:
```bash
npx codemod@latest react/19/migration-recipe
```
3. Following the official guide, replace string refs with callbacks and removed uses of `ReactDOM.render` with the appropriate root API.
4. If you use TypeScript, follow the guide's types section: the recipe above does not cover all those changes. For example, initialize the ref explicitly:
```tsx
const inputRef = useRef<HTMLInputElement>(null);
```
5. In function components, React 19 allows `ref` as a prop. Preserve the compatibility your library's consumers need.

> [!NOTE] Check your version
> `ref` as a prop requires React 19. In React 18 and earlier, use `forwardRef` to receive it.

React 19 removes `propTypes` and `defaultProps` for function components, Legacy Context, string refs, `ReactDOM.render`, `ReactDOM.hydrate` and `ReactDOM.findDOMNode`. Use `createRoot`, `hydrateRoot` and refs as appropriate. Uncaught render errors are reported to `window.reportError`, and caught errors to `console.error`; roots accept `onUncaughtError` and `onCaughtError`. For TypeScript, use the separate codemod `npx types-react-codemod@latest preset-19 ./path-to-app`.

## How to check the fix
Run your project's type checker and tests. Exercise mounting, refs and affected flows in a production build; review warnings and error reporting.

## If that was not it
| Possible cause | What to check |
|---|---|
| A codemod misses the case | Remaining guide steps and generated diff |
| Incompatible dependency types | Versions and support declared by each package |
| Different error reporting | React 19 render error handling changes |

> [!AI] With AI
> Provide React, React DOM, TypeScript and affected library versions, the full error and a minimal reproduction. Ask it to identify the specific change in the official guide.

Source: [React 19 upgrade guide](https://react.dev/blog/2024/04/25/react-19-upgrade-guide) and [ref as a prop](https://react.dev/blog/2024/12/05/react-19).

Related: [React](@/react/react).

=== esquema
# Migration
- Review — identify deprecated APIs and dependencies.
- Transform — run codemods and review the diff.
- Verify — check types, tests and behavior.
=== test
? What does the migration recipe include?
* Several React API codemods
- Every possible change to every dependency
- An automatic production build
! Review its output and remaining steps.
? What does useRef need with React 19 types?
* An initial argument
- A mandatory string
- A class component
! For example, use null as the initial value.
? When is ref available as a prop in function components?
* In React 19
- In every React version
- Only outside React
! In React 18 use forwardRef to receive it.
? What should you do after running codemods?
* Review the diff and test the application
- Publish without review
- Delete all tests
! Automated changes need review.
