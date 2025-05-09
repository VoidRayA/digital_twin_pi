import RPi.GPIO as gpio
from time import sleep

class Led:
    def __init__(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin, gpio.LOW)

    def ledOn(self):
        gpio.output(self.pin, gpio.HIGH)

    def ledOff(self):
        gpio.output(self.pin, gpio.LOW)

    def ledBlink(self, count, time):
        for _ in range(count):
            gpio.output(self.pin, gpio.HIGH)
            sleep(time)
            gpio.output(self.pin, gpio.LOW)
            sleep(time)