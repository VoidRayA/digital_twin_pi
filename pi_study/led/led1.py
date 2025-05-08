import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 20, 21)

#BCM	-> GPIO
#BOARD	-> BOARD
gpio.setmode(gpio.BCM)
gpio.setup(ledPin, gpio.OUT)

try:
    while True:
        number = int(input("led number(1/2/3): "))
        mode = input("mode(on/off): ")        
            
        if mode == "on":
            gpio.output(ledPin[number - 1], gpio.HIGH)            
        elif mode == "off":        
            gpio.output(ledPin[number - 1], gpio.LOW)            
            
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()
