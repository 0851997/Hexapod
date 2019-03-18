#!/bin/python
 
# importeer de GPIO bibliotheek.
import RPi.GPIO as GPIO
# Importeer de time biblotheek voor tijdfuncties.
from time import sleep
 
# Zet de pinmode op Broadcom SOC.
GPIO.setmode(GPIO.BCM)
# Zet waarschuwingen uit.
GPIO.setwarnings(False)
 
# Zet de GPIO pin als uitgang.
GPIO.setup(4, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
# Configureer de pin voor PWM met een frequentie van 50Hz.
p = GPIO.PWM(4, 50)
k = GPIO.PWM(2, 50)
r = GPIO.PWM(3, 50)
# Start PWM op de GPIO pin met een duty-cycle van 6%
def angleToCycle(i):
      x = i/180*8.5+2.5
      return x

# the range is 0...180
for s in range(181):
      y = angleToCycle(s)
      
      p.start(y)
      k.start(y)
      r.start(y)
     
      try:
      while True:
            # 0 graden (neutraal)
            p.ChangeDutyCycle(y)
            k.ChangeDutyCycle(y)
            r.ChangeDutyCycle(y)
            sleep(1)

            # -90 graden (rechts)
            p.ChangeDutyCycle(y)
            r.ChangeDutyCycle(y)
            k.ChangeDutyCycle(y)
            sleep(1)

            # 0 graden (neutraal)
            p.ChangeDutyCycle(y)
            r.ChangeDutyCycle(y)
            k.ChangeDutyCycle(y)
            sleep(1)

            # 90 graden (links)
            p.ChangeDutyCycle(y)
            k.ChangeDutyCycle(y)
            r.ChangeDutyCycle(y)
            sleep(1)
             
      except KeyboardInterrupt:
        # Stop PWM op GPIO.
        p.stop()
        k.stop()
        r.stop()
        # GPIO netjes afsluiten
        GPIO.cleanup()
