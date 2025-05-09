import RPi.GPIO as gpio
from time import sleep

class ButtonEvent:
    def __init__(self, clickEvent):
        self.clickEvent = clickEvent

    def onClick(self):
        self.clickEvent()

class Button:
    def __init__(self, pin, value):
        self.pin = pin
        self.value = value
        self.prevState = gpio.LOW
        self.currentState = gpio.LOW
        self.buttonEvent = None
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

    def setButtonEvent(self, buttonEvent):
        self.buttonEvent = buttonEvent

    def onClick(self):
        if self.buttonEvent is not None:
            self.currentState = gpio.input(self.pin)
            if self.currentState == gpio.HIGH and self.prevState == gpio.LOW:
                self.buttonEvent.onClick()
            self.prevState = self.currentState
            sleep(0.05)
