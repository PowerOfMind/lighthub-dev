---
title: window is not defined in Next.js
desc: window is not defined when Next.js server rendering reaches browser APIs; move the access to the client and check the initial render.
pkgs: next, react
---
## How it shows up
The route fails with a ReferenceError about `window`.
- A route fails while rendering on the server.
- A dependency can fail when imported.
- Browser-only data is unavailable during server rendering.
- Different initial output can cause a hydration mismatch.

A separate error appears when a client hook is used in a Server Component; the Next.js documentation lists it under the title "React client hook in Server Component".
Add `'use client'` at the top of the file using the hook.

## Most likely causes
1. Code accesses `window` during server rendering.
2. A dependency accesses `window` when imported.
3. A Client Component is also prerendered and accesses `window` during its initial render.

## Fix
1. Find the access in the stack trace. In App Router, put `use client` at the top of the interactive component file.
2. Move the read into an effect or event handler, not the render body:
```jsx
'use client';
import {useEffect, useState} from 'react';

export default function Width() {
  const [width, setWidth] = useState(null);
  useEffect(() => setWidth(window.innerWidth), []);
  return <p>{width === null ? 'Loading' : width}</p>;
}
```
3. If a library fails on import, consult Next.js lazy loading and disable prerendering for the Client Component containing it when necessary.

> [!NOTE] Check your version
> `use client` and loading options depend on the Next.js version and router.

## How to verify the fix
Reload the route directly, check server logs and the console, and try a production build. Check that initial content does not cause a hydration error.

## If that was not the cause
| Possible cause | What to check |
|---|---|
| Module-level access | Imports and code run when the library loads |
| Different initial render | Conditions using `typeof window` |
| Another API | Access to `document` or `localStorage` |

> [!AI] With AI
> Share versions, router, complete stack trace and minimal component including imports. Say whether it fails on render or import.

Source: [server and client components](https://nextjs.org/docs/app/getting-started/server-and-client-components) and [lazy loading](https://nextjs.org/docs/app/guides/lazy-loading).

Related: [hydration failed](@/react/hydration-failed-en-nextjs).

=== esquema
# Browser and server
- Identify — locate the window access.
- Move — read it after mounting.
- Verify — check server, console and hydration.
=== test
? Is window available on the server?
* No, it is a browser API
- Always
- Only in server effects
! It is unavailable during SSR.
? Does use client guarantee the first render never runs on the server?
* No
- Yes, always
- Only in production
! A Client Component can be prerendered.
? Where can window be read after mounting?
* In an effect
- In the server render
- In an import executed on the server
! The effect runs on the client.
? What else should be checked?
* Hydration mismatches
- The editor name
- The terminal colour
! Initial content must match.
