#checks when button is pressed
import time
import os
import RPi.GPIO as GPIO

#init parameters
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#init pins as input - button pressed input
GPIO.setup(10,GPIO.IN)
print GPIO.input(10)

#infinite loop checks when button is pressed
while True:
    if (GPIO.input(10)==False):
        print("Button is pressed")
        os.system('date')
        print GPIO.input(10)
        time.sleep(5)
    else:
        os.system('clear')
        print('Waiting for button press')
time.sleep(1)
