---
tipo: error
title: Los deep links no abren la pantalla en Expo Router
desc: Los deep links no abren la pantalla en Expo Router si el esquema, la ruta o la asociación del dominio no coinciden con la aplicación.
pkgs: expo, expo-router
---
## Cómo se manifiesta
- Un enlace se abre en el navegador en vez de en la aplicación.
- La aplicación se abre sin llegar a la pantalla prevista.
- Un esquema personalizado no abre la aplicación instalada.
- Un enlace HTTPS no abre la aplicación asociada.
## Causa más probable
1. El esquema o la ruta del enlace no coincide con la configuración o los archivos de rutas.
2. La build instalada no incorpora la configuración nativa nueva.
3. En enlaces HTTPS, falta la asociación entre dominio y aplicación.
## Arreglo
1. Define el esquema en `app.json` y adapta el nombre a tu aplicación:
```json
{ "expo": { "scheme": "myapp" } }
```
2. Crea e instala una nueva development build. Comprueba que la ruta del enlace corresponde a una pantalla de Expo Router y prueba `myapp://` seguido de esa ruta.
3. Para Universal Links en iOS, configura `ios.associatedDomains` y publica `/.well-known/apple-app-site-association` en tu dominio con el equipo, identificador y rutas correctos.
4. Para Android App Links, configura `android.intentFilters` y publica `/.well-known/assetlinks.json` con el paquete y la huella del certificado de firma. Sigue las guías oficiales para la estructura y verificación de ambos archivos.
> [!NOTE] Comprueba tu versión
> La configuración nativa y las herramientas de prueba dependen del SDK y del sistema. Expo Go ofrece soporte limitado para enlaces entrantes.
## Cómo comprobar que está arreglado
Instala la build nueva y abre un enlace a una ruta existente con la app cerrada y abierta. Prueba los enlaces HTTPS en cada plataforma y comprueba la asociación del dominio; sin app instalada, verifica la web.
## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Ruta incorrecta | Archivos de Expo Router y parámetros |
| Asociación incorrecta | Dominio, identificadores y certificado de firma |
| Build antigua | Instalación de una build con la configuración nueva |
> [!AI] Con IA
> Comparte SDK, plataforma, URL de ejemplo sin datos privados, configuración, archivos de asociación y logs completos sin credenciales.
Fuente: [esquemas](https://docs.expo.dev/linking/into-your-app/), [Universal Links](https://docs.expo.dev/linking/ios-universal-links/), [Android App Links](https://docs.expo.dev/linking/android-app-links/).
Relacionado: [Expo Router y navegación](@/react-native/expo-router-y-navegacion).
=== esquema
# Enlaces
- Esquema — configurar y crear una build nueva.
- HTTPS — asociar dominio y aplicación en cada plataforma.
- Validar — probar rutas con la app abierta y cerrada.
=== test
? ¿Qué propiedad define un esquema personalizado?
* scheme
- title
- desc
! Se configura en la app config.
? ¿Qué requiere un Universal Link?
* Asociación entre dominio y app
- Solo un icono
- Solo Metro
! iOS verifica la asociación.
? ¿Qué archivo usa Android para asociar el dominio?
* assetlinks.json
- package.json
- Podfile
! Se publica en .well-known.
? ¿Qué hay que hacer tras cambiar el esquema nativo?
* Crear e instalar una build nueva
- Cambiar el color de fondo
- Borrar las rutas
! La app instalada debe incorporar el cambio.
