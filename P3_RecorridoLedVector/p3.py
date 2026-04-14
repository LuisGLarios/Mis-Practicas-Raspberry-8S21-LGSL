import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Definición del vector de pines para los LEDs
vector_pines_gpio = [17, 27, 22, 23]
leds_pwm = []
frecuencia = 1000 

# Inicialización de cada pin en el vector con PWM
for pin in vector_pines_gpio:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, frecuencia)
    pwm.start(0) 
    leds_pwm.append(pwm)

print("Iniciando recorrido LED. Presiona Ctrl+C para detener.")

try:
    while True:
        for pwm in leds_pwm:
            # Incremento gradual del brillo (Fade In)
            for duty_cycle in range(0, 101, 5):
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(0.02)
                
            # Decremento gradual del brillo (Fade Out)
            for duty_cycle in range(100, -1, -5):
                pwm.ChangeDutyCycle(duty_cycle)
                time.sleep(0.02)
                
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nRecorrido detenido por el usuario.")

finally:
    # Finalización de procesos PWM y limpieza de pines
    for pwm in leds_pwm:
        pwm.stop()
    GPIO.cleanup()
    print("Pines GPIO liberados.")
