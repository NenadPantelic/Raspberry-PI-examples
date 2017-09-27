#reaction test game - who press the button first after LED light wins
from gpiozero import LED, Button
from time import sleep
from random import uniform
from sys import exit

#two buttons ( 14 & 15) and LED (4)
led = LED(4)
right_button = Button(14)
left_button = Button(15)

#player's names
print("Player 1")
first_player = input("Enter your name:\n")
print("Player 2")
second_player = input("Enter your name:\n")

#signal of LED
led.on()
sleep(uniform(5,10))
led.off()

#checks who pressed it
def pressed(button):
    if button.pin.number == 14:
        print (first_player + ' wins')
    elif button.pin.number == 15:
        print (second_player + ' wins')
    exit() 
       
left_button.when_pressed = pressed
right_button.when_pressed = pressed
