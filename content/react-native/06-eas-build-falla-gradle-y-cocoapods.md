---
title: EAS Build falla en Gradle o al empaquetar JavaScript
desc: Diagnostica fallos de EAS Build en Gradle o al empaquetar JavaScript revisando logs, dependencias y configuración nativa.
pkgs: expo, react-native
---
## Síntoma
```text
Gradle build daemon disappeared unexpectedly (it may have been killed or may have crashed)
```
Este error de Gradle puede aparecer cuando se termina el proceso de Node que empaqueta JavaScript.

```text
Task :app:bundleReleaseJsAndAssets FAILED
```
En Android puede indicar que Metro no pudo empaquetar JavaScript. En iOS, el mensaje correspondiente es:
```text
Metro encountered an error
```
## Causa más probable
1. Una dependencia o plugin nativo es incompatible o está mal configurado.
2. Faltan archivos o variables en el entorno de EAS.
3. En el error citado, el proceso de Node que genera el bundle puede haber sido terminado, a menudo por un bundle muy grande.
## Arreglo
1. Abre la fase fallida en EAS y busca el error concreto anterior al resumen; si el fallo está en la fase de iOS, revisa el registro de esa fase.
2. Ejecuta `npx expo-doctor` y corrige los avisos relevantes.
3. Compara con una build correcta: paquetes, plugins, variables y archivos enviados. Para aislar el bundle JavaScript, ejecuta `npx expo export`.
4. Para el error del daemon, examina el tamaño del bundle con Expo Atlas: un bundle grande puede provocar que se termine el proceso de Node. Configura la clase de recursos `large` en `eas.json`.
> [!NOTE] Comprueba tu versión
> SDK, plugins y herramientas nativas deben ser compatibles; consulta sus notas antes de cambiarlos.
## Cómo comprobar que está arreglado
Repite la build en la plataforma afectada, instala el resultado y prueba la función modificada.
## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Variables ausentes | Entorno seleccionado para EAS |
| Archivo excluido | Archivo enviado, sin exponer secretos |
| Error nativo | Mensaje completo de la fase fallida |
> [!AI] Con IA
> Comparte plataforma, SDK, perfil, cambios recientes y logs completos, sin credenciales.
Fuente: [diagnóstico de EAS Build](https://docs.expo.dev/build-reference/troubleshooting/).
Relacionado: [actualizar Expo SDK](@/react-native/actualizar-expo-sdk-sin-romper).
=== esquema
# Build
- Localizar — leer el error de la fase.
- Comparar — entorno y dependencias.
- Validar — repetir build y probarla.
=== test
? ¿Qué permite diagnosticar la build?
* El error concreto del log
- Solo el nombre de la fase
- El icono
! La fase no identifica por sí sola la causa.
? ¿Qué revisa Expo Doctor?
* Configuración y dependencias
- El diseño
- La cuenta bancaria
! Revisa sus avisos.
? ¿Para qué sirve npx expo export aquí?
* Para aislar errores del bundle JavaScript
- Para crear credenciales
- Para cambiar el dominio
! Comprueba el bundle por separado.
? ¿Cómo se valida el arreglo?
* Con otra build y una prueba de la app
- Cerrando el log
- Cambiando el nombre de carpeta
! Prueba también la build resultante.
