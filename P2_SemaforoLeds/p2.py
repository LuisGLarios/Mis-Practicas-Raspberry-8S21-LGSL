import RPi.GPIO as GPIO
import time
from datetime import datetime
import numpy as np

LED_ROJO = 17
LED_AMARILLO = 27
LED_VERDE = 22

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup([LED_ROJO, LED_AMARILLO, LED_VERDE], GPIO.OUT)

ESTADOS = np.array([
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
])

TIEMPOS = np.array([10, 10, 3])

timeline = np.cumsum(TIEMPOS)
ciclo_total = timeline[-1]

def hora_a_segundos(h, m=0, s=0):
    return h*3600 + m*60 + s

rango_nocturno = np.array([
    hora_a_segundos(2,0,0),
    hora_a_segundos(5,0,0)
])

def obtener_segundos_actuales():
    ahora = datetime.now()
    return ahora.hour*3600 + ahora.minute*60 + ahora.second

def aplicar_estado(estado):
    GPIO.output(LED_ROJO, estado[0])
    GPIO.output(LED_AMARILLO, estado[1])
    GPIO.output(LED_VERDE, estado[2])

print("Iniciando semáforo...")
print("Presiona Ctrl + C para terminar el proceso\n")

estado_previo = None

try:
    while True:
        seg_actual = obtener_segundos_actuales()

        en_nocturno = np.logical_and(
            seg_actual >= rango_nocturno[0],
            seg_actual < rango_nocturno[1]
        )

        modo = int(en_nocturno)
        modos = ["NORMAL", "NOCTURNO"]

        if modos[modo] == "NOCTURNO":
            if estado_previo != "APAGADO":
                print("Modo nocturno: Semáforo apagado")
                estado_previo = "APAGADO"
            aplicar_estado([0,0,0])
            time.sleep(1)
            continue

        t = time.time() % ciclo_total
        indice = np.searchsorted(timeline, t)
        estado_actual = ESTADOS[indice].tolist()

        if estado_actual != estado_previo:
            if estado_actual == [1, 0, 0]:
                print("LED Rojo encendido")
            elif estado_actual == [0, 0, 1]:
                print("LED Verde encendido")
            elif estado_actual == [0, 1, 0]:
                print("LED Amarillo encendido")
            
            estado_previo = estado_actual

        aplicar_estado(estado_actual)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProceso terminado. Limpiando pines GPIO...")
    GPIO.cleanup()
