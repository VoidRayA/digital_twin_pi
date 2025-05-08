import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 20, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.LOW)
    
try:    
    while True:
        password = int(input("new password: "))
        confirmPW = int(input("confirm password: "))
        
        if password == confirmPW:
            print("Passwords has been set")
            break
        else:
            print("Passwords do not match")
            
    while True:        
        loginPW = int(input("login password: "))
            
        if password == loginPW:
            gpio.output(ledPin[2], gpio.HIGH)
            break            
        else:                
            for i in range(5):            
                gpio.output(ledPin[0], gpio.HIGH)
                sleep(0.1)
                gpio.output(ledPin[0], gpio.LOW)
                sleep(0.1)
            continue        
            
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()