# P1 - Control de Parpadeo LED (Raspberry Pi)

Este repositorio contiene la primera práctica de control de hardware, donde se implementa un ciclo de parpadeo continuo utilizando los pines GPIO de una Raspberry Pi.

## Descripción

Este proyecto es el punto de partida para interactuar con componentes electrónicos externos. A través de un script en Python, controlamos la salida de voltaje de la placa para encender y apagar un LED rítmicamente.

## Objetivos

* Configurar el acceso a los pines **GPIO** mediante software.
* Implementar un ciclo de trabajo con retardos de tiempo.
* Asegurar la liberación de recursos del sistema al finalizar la ejecución.

## Requisitos de Hardware

| Cantidad | Componente | Notas |
| :--- | :--- | :--- |
| 1 | Raspberry Pi | Modelos 3, 4 o Zero |
| 1 | LED | Cualquier color |
| - | Jumpers y Protoboard | Para conexiones físicas |

## Esquema de Conexión

La conexión se realiza siguiendo el estándar de numeración **BCM**:

* **Señal:** Pin Físico 12 (GPIO 18) Resistencia Ánodo del LED (+).
* **Tierra:** Cátodo del LED (-) Pin Físico 14 (GND).

## Instalación y Uso

### 1. Preparar el entorno

Es recomendable trabajar dentro de un entorno virtual. Asegúrate de tener instalada la librería necesaria:

`pip install RPi.GPIO`
