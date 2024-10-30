# SyncTime Executable (English)

## Overview

The `SyncTime` executable is a standalone program designed to disable and then re-enable the time synchronization service on Windows. 

## How It Works

1. **Disable Time Synchronization**: The program uses the `w32tm` command to disable the time synchronization service. It clears the manual peer list and stops the `w32time` service.
2. **Wait**: The program pauses for a short period (2 seconds) to allow for any necessary changes or maintenance.
3. **Enable Time Synchronization**: The program then re-enables the time synchronization service by resynchronizing the time and starting the `w32time` service again.

## Requirements

- Windows operating system
- Administrative privileges to run the executable (required to modify time synchronization settings)

## Usage

1. Download the `SyncTime.exe` executable from the release section.
2. Right-click on the executable and select "Run as administrator" to ensure it has the necessary permissions.
3. Follow the on-screen instructions.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejecutable SyncTime (Español)

## Descripción

El ejecutable `SyncTime` es un programa independiente diseñado para desactivar y luego reactivar el servicio de sincronización de la hora en Windows. 

1. **Desactivar la Sincronización de la Hora**: El programa utiliza el comando `w32tm` para desactivar el servicio de sincronización de la hora. Limpia la lista de pares manuales y detiene el servicio `w32time`.
2. **Esperar**: El programa se pausa por un breve período (2 segundos) para permitir cualquier cambio o mantenimiento necesario.
3. **Activar la Sincronización de la Hora**: Luego, el programa vuelve a habilitar el servicio de sincronización de la hora resincronizando la hora y reiniciando el servicio `w32time`.

## Requisitos

- Sistema operativo Windows
- Privilegios administrativos para ejecutar el ejecutable (requerido para modificar la configuración de sincronización de la hora)

## Uso

1. Descarga el ejecutable `SyncTime.exe` desde la sección de lanzamientos.
2. Haz clic derecho en el ejecutable y selecciona "Ejecutar como administrador" para asegurarte de que tenga los permisos necesarios.
3. Sigue las instrucciones en pantalla.