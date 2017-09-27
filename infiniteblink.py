#infinite blinking of two LEDs controlled by GPIOs 23 and 24

import time
import RPi.GPIO as GPIO
#init parameters
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#init pins as output
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
#inifinite blinking of leds connected to pins 23 & 24 (BCM mode)
while True:
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(24,GPIO.LOW)
    time.sleep(1)


