---
title: Actualizar Expo SDK sin romper la aplicación
desc: Actualizar Expo SDK puede romper dependencias o proyectos nativos; revisa las notas de versión y comprueba la compatibilidad antes de publicar.
pkgs: expo, react-native
---
## Cómo se manifiesta
- Aparecen avisos de compatibilidad de dependencias tras actualizar el SDK.
- Falla una build nativa después de la actualización.
- Una biblioteca necesita cambios para el SDK de destino.
- Los proyectos nativos necesitan actualizarse.

## Causa más probable
1. Las versiones de las dependencias aún corresponden al SDK anterior.
2. Los proyectos nativos no reflejan los cambios del SDK.
3. Una biblioteca o configuración necesita un cambio indicado en las notas de versión.

## Arreglo
1. Guarda los cambios y consulta las notas de cada SDK que vayas a atravesar. Expo recomienda actualizar de una versión de SDK a la siguiente.
2. Instala la versión de `expo` correspondiente al SDK de destino siguiendo su guía. Después, desde la raíz del proyecto:
```bash
npx expo install --fix
npx expo-doctor
```
3. Revisa los cambios del gestor de paquetes y resuelve los avisos de Doctor. Si usas generación nativa continua, sigue las instrucciones de Expo para regenerar los directorios nativos. Si mantienes `ios` y `android` manualmente, aplica los cambios nativos pertinentes y ejecuta `npx pod-install` para iOS.
4. Aplica las instrucciones adicionales de las notas de versión y crea nuevas builds nativas.

> [!NOTE] Comprueba tu versión
> La versión de destino determina las dependencias y los cambios nativos necesarios. Consulta sus notas antes de modificar el proyecto.

## Cómo comprobar que está arreglado
Ejecuta de nuevo Doctor, revisa los avisos restantes y prueba una build nueva en cada plataforma que distribuyas. Recorre las funciones que usan módulos nativos.

## Si no era eso
| Posible causa | Qué revisar |
|---|---|
| Biblioteca incompatible | Compatibilidad de la biblioteca con el SDK y la arquitectura elegidos |
| Cambios nativos propios | Diferencias que deben conservarse antes de regenerar |
| Expo Go incompatible | SDK del proyecto y versión de Expo Go |

> [!AI] Con IA
> Comparte los SDK de origen y destino, el gestor de paquetes, los logs completos de Doctor y de la build, y si mantienes los proyectos nativos. Elimina credenciales de los registros.

Fuente: [actualización de Expo SDK](https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough/).

Relacionado: [Expo y publicación](@/react-native/expo-eas-y-publicar).

=== esquema
# Migración
- Preparar — revisar las notas de cada SDK.
- Alinear — instalar dependencias compatibles y ejecutar Doctor.
- Validar — actualizar proyectos nativos y probar builds nuevas.
=== test
? ¿Qué comando alinea dependencias con el SDK instalado?
* npx expo install --fix
- npx expo start
- npx pod-install
! Expo install comprueba y corrige versiones compatibles.
? ¿Qué herramienta revisa problemas habituales del proyecto?
* Expo Doctor
- El navegador
- El editor de texto
! Expo Doctor revisa configuración y dependencias.
? ¿Qué documentación hay que revisar para los cambios específicos?
* Las notas del SDK de destino
- Solo el historial de Git
- Solo la documentación de CSS
! Las notas incluyen cambios y pasos adicionales.
? ¿Qué hay que probar después de cambios nativos?
* Una build nativa nueva
- Solo una captura de pantalla
- Solo el texto del README
! Comprueba la build en las plataformas que distribuyas.
