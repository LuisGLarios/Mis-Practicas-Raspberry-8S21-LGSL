# P3 - Control de Intensidad con PWM (LED Fading)

Este repositorio contiene la tercera práctica de sistemas embebidos, enfocada en la técnica de PWM (Pulse Width Modulation) para controlar la intensidad lumínica de múltiples LEDs.

## Descripción

El proyecto utiliza una lista de pines GPIO para realizar un recorrido de intensidad gradual. Cada LED realiza un efecto de "encendido suave" (*Fade In*) seguido de un "apagado suave" (*Fade Out*) antes de pasar al siguiente LED en la secuencia.

## Objetivos

* Implementar **PWM por software** mediante la librería `RPi.GPIO`.
* Controlar el brillo variando el **Duty Cycle** (Ciclo de Trabajo) de 0% a 100%.
* Gestionar múltiples objetos PWM de manera eficiente mediante listas y bucles.

## Conexiones (Pinout)

| LED | Pin BCM | Pin Físico |
| :--- | :--- | :--- |
| LED 1 | GPIO 17 | Pin 11 |
| LED 2 | GPIO 27 | Pin 13 |
| LED 3 | GPIO 22 | Pin 15 |
| LED 4 | GPIO 23 | Pin 16 |
| GND | Tierra | Pin 14 |

## Uso e Instalación

### 1. Requisitos

Es necesario contar con la librería `RPi.GPIO`. Si utilizas el entorno virtual del curso:

```bash
source 8S21/bin/activate
