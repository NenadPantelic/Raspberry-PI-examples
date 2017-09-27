# blinkig led
import RPi.GPIO as GPIO
import time

# GPIO pins init

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


#you can use GPIO.BCM (Broadcom channel) -- NAME on headersheet.jpg (pin 18 ) or GPIO.BOARD  -- PIN# on headersheet.jpg (pin 12 )
#so, GPIO.BCM+pin18  or GPIO.BOARD+pin12

#20 led blinks
for i in range(0,20):
    GPIO.output(18,1) # light on
    time.sleep(1)     # sleep 1 second
    GPIO.output(18,0) # light off
    time.sleep(1)     # sleep 1 second 

GPIO.cleanup()        #clean GPIO ports that were used
