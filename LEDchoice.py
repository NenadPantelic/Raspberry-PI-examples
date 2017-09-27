#choice of LED and number of times that it will blink
import os
import time
import RPi.GPIO as GPIO

#init parameters
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

#init state
led_choice = 0
count = 0
os.system('clear')
#possible choices of diode
print ("Which diode to turn on?")
print ("1:First?")
print ("2:Scond?")

#dictionaries that maps number of ledsto some useful expressions or numbers
choices = {1:"the first one",2:" the second one"}
LEDS = {1:23,2:24}
#your choice
led_choice = input("Your choice:")


if  led_choice in choices:
    os.system('clear')
    print "You chose "+ choices[led_choice]
    count = input("Enter number of blinks: ")
    while count>0:
        GPIO.output(LEDS[int(led_choice)],GPIO.HIGH)
        time.sleep(1)
        print("Blink")
        GPIO.output(LEDS[int(led_choice)],GPIO.LOW)
        time.sleep(1)
        count-=1
else:
    print ("There are just 2 LEDs. Enter 1 or 2.")

        
