---
tipo: error
title: Unable to resolve module en Expo
desc: Unable to resolve module en Expo impide generar el bundle; revisa la ruta del import, la instalación y los archivos enviados a EAS.
pkgs: expo, react-native
---
## Síntoma
```text
Unable to resolve module ./src/Routes ...
```
Este ejemplo aparece cuando Metro no puede resolver una ruta importada.
## Causa más probable
1. La ruta o las mayúsculas del import no coinciden con el archivo.
2. El paquete no está instalado.
3. El archivo local no se incluye en la build de EAS.
## Arreglo
1. Compara el import señalado con la ruta real y corrige nombres y mayúsculas.
2. Para un paquete, ejecuta `npx expo install nombre-del-paquete`, sustituyendo el nombre por el del módulo.
3. Si falla solo en EAS, revisa `.gitignore`: EAS no sube los archivos ignorados. Elimina el import si no se usa, guarda un secreto como variable de entorno de tipo archivo o incluye un archivo no secreto con `.easignore`.
4. Reinicia Metro limpiando la caché:
```bash
npx expo start --clear
```
> [!NOTE] Comprueba tu versión
> Las dependencias nativas deben ser compatibles con el SDK; revisa `npx expo-doctor`.
## Cómo comprobar que está arreglado
Abre la ruta afectada. Si fallaba en EAS, repite la build y revisa la fase del bundle.
## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Alias | Configuración de rutas |
| Monorepo | Dependencias y archivos disponibles para la aplicación |
| Archivo generado | Paso de generación anterior al bundle |
> [!AI] Con IA
> Comparte versiones de Expo y Node, import, árbol de archivos y log completo, sin secretos.
Fuente: [diagnóstico de builds](https://docs.expo.dev/build-reference/troubleshooting/), [limpieza de caché](https://docs.expo.dev/troubleshooting/clear-cache-macos-linux/).
Relacionado: [actualizar Expo SDK](@/react-native/actualizar-expo-sdk-sin-romper).
=== esquema
# Diagnóstico
- Import — revisar ruta y mayúsculas.
- Dependencia — instalar con Expo.
- EAS — comprobar archivos enviados.
=== test
? ¿Qué ayuda a localizar el import?
* El archivo señalado por Metro
- El icono de la app
- El certificado de Apple
! Metro identifica el archivo que importa el módulo.
? ¿Qué comando limpia la caché de Metro?
* npx expo start --clear
- eas credentials
- npx expo-doctor
! Reinicia Metro con la caché limpia.
? ¿Qué revisar si falla solo en EAS?
* Los archivos excluidos del envío
- El color del icono
- El tamaño de pantalla
! EAS necesita los archivos importados.
? ¿Qué revisar si un import falla solo en EAS?
* Que el nombre y las mayúsculas coincidan con el archivo
- Que la aplicación use una build de desarrollo
- Que Expo Doctor esté instalado globalmente
! El import debe coincidir con el nombre y las mayúsculas del archivo.
