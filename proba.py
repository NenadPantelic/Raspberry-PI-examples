#simple led blink controlled by GPIO 18 and 23

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(18,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
