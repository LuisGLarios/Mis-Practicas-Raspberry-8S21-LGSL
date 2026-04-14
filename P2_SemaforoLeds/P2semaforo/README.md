# Práctica 2: Semáforo Avanzado con Modo Nocturno

Este repositorio contiene la segunda práctica de control de hardware, donde se implementa un semáforo de tres luces (rojo, amarillo, verde) para Raspberry Pi, incorporando una lógica que cambia su comportamiento según la hora del sistema.

## Descripción

A diferencia de un secuenciador de luces simple, este proyecto utiliza un "semáforo inteligente". El script en Python consulta la hora real de la Raspberry Pi y decide qué modo ejecutar:

* **Modo Normal:** Ejecuta una secuencia de tráfico estándar con tiempos específicos para cada color.
* **Modo Nocturno:** Entre las 2:00 AM y las 5:00 AM (horario configurable), el semáforo apaga todos sus LEDs para ahorro de energía, indicando un estado de precaución o inactividad.

## Objetivos

* Controlar tres salidas digitales GPIO simultáneamente.
* Implementar una secuencia lógica basada en arrays de estados y tiempos.
* Utilizar librerías estándar como `datetime` para obtener el tiempo real del sistema.
* Gestionar el hardware de forma segura, garantizando la limpieza de pines GPIO al finalizar.

## Requisitos de Hardware

| Cantidad | Componente | Notas |
| :--- | :--- | :--- |
| 1 | Raspberry Pi | Modelos 3, 4 o Zero |
| 1 | LED Rojo | Indicador de Detener |
| 1 | LED Amarillo | Indicador de Precaución |
| 1 | LED Verde | Indicador de Siga |
| - | Jumpers y Protoboard | Para conexiones físicas |

## Esquema de Conexión

La interfaz se realiza a través de la cabecera de 40 pines utilizando la numeración **BCM**:

* **Verde:** Pin Físico 11 → GPIO 17 → Resistencia → LED (+).
* **Amarillo:** Pin Físico 13 → GPIO 27 → Resistencia → LED (+).
* **Rojo:** Pin Físico 15 → GPIO 22 → Resistencia → LED (+).
* **GND:** Pin Físico 14 (o 6, 9) → Cátodo Común del LED (-).

## Instalación y Uso

### 1. Preparar el Entorno

Se recomienda encarecidamente trabajar dentro de un entorno virtual. Para este proyecto avanzado, se necesitan librerías adicionales. Primero, activa tu entorno e instala las dependencias:

```bash
source 8S21/bin/activate  # O tu entorno virtual correspondiente
pip install RPi.GPIO numpy

### 2. Guardar el progreso
* Baja a **"Commit changes"**.
* Escribe: `Agregando documentación de la Práctica 2 - Semáforo`.
* Dale al botón verde.

**Nota para tu equipo:** Si quieres que el profe vea que otros también participaron, diles que uno de ellos suba el archivo de código `p2.py` dentro de esa misma carpeta `P2semaforo`.

¿Me pasas la tercera captura cuando estés listo?
