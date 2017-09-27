#double led blink controlled by GPIO 23 & 24 (BCM mode)
import time
import RPi.GPIO as GPIO
#init parameters
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#init pins as output
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
#lights on
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
#lights off
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
time.sleep(1)
#lights on
GPIO.output(23,GPIO.HIGH)
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
#lights off
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.cleanup()

