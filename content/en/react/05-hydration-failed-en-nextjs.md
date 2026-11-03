---
tipo: error
title: Hydration failed in Next.js
desc: Hydration failed in Next.js when server HTML differs from the initial client render; find the mismatch and make the output consistent.
pkgs: next, react, react-dom
---
## Symptom
```text
Text content does not match server-rendered HTML
```
The exact console text may vary by version; this is the title used by the Next.js documentation.
This appears when the server-rendered React tree differs from the browser’s first render.

## Most likely causes
1. The first render uses changing values such as the time, or browser-only data.
2. Invalid HTML nesting causes the browser to change the tree.
3. An extension or intermediary changes the HTML before hydration.

## Fix
1. Locate the component in the error and compare server output with the browser's first render.
2. Make both produce the same initial content. Read browser-only data after mounting:
```jsx
'use client';
import {useEffect, useState} from 'react';

export default function TimeZone() {
  const [zone, setZone] = useState('Loading');
  useEffect(() => setZone(Intl.DateTimeFormat().resolvedOptions().timeZone), []);
  return <p>{zone}</p>;
}
```
3. Fix HTML nesting and avoid `window`-based conditions during the initial render.

For client-only content, `next/dynamic` with `{ ssr: false }` is another option. `suppressHydrationWarning={true}` is an emergency escape hatch: it works only one level deep and React does not try to patch the text.

## How to verify the fix
Reload the page directly and check the console and initial output. Repeat without extensions and in a production build.

## If that was not the cause
| Possible cause | What to check |
|---|---|
| Invalid HTML | Paragraph and interactive element nesting |
| CSS-in-JS | The library's server-rendering setup |
| Modified HTML | Extensions and CDN configuration |

> [!AI] With AI
> Provide versions, the complete log, a minimal component and initial server HTML; mention extensions and CDNs.

Source: [Next.js hydration error](https://nextjs.org/docs/messages/react-hydration-error).

Related: [window is not defined](@/react/window-is-not-defined-y-use-client).

=== esquema
# Hydration
- Compare — server and first browser render.
- Fix — stable initial content and valid HTML.
- Verify — reload and check the console.
=== test
? What must match during hydration?
* Server HTML and the first client render
- Installed extensions
- Every user's clock
! React expects matching initial content.
? When does useEffect run?
* After mounting on the client
- During server rendering
- Before server HTML is created
! Read browser data after mounting.
? What can alter HTML before hydration?
* A browser extension
- A code comment
- The file name
! Also try without extensions.
? What should you do with invalid nesting?
* Correct the structure
- Always hide the warning
- Delete tests
! The browser may change the tree.
