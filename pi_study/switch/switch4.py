import RPi.GPIO as gpio
from time import sleep
from threading import Thread

gpio.setmode(gpio.BCM)

class Led:

    def __init__(self, pin, color):
        self.pin = pin
        self.color = color
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin, gpio.LOW)

    def blink(self, count, time):
        for _ in range(count):
            gpio.output(self.pin, gpio.HIGH)
            sleep(time)
            gpio.output(self.pin, gpio.LOW)
            sleep(time)

    def ledOn(self):
        gpio.output(self.pin, gpio.HIGH)

    def ledOff(self):
        gpio.output(self.pin, gpio.LOW)

class Button:

    def __init__(self, pin, onPressed):
        self.pin = pin
        self.prevState = gpio.LOW
        self.onPressed = onPressed
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

    def waitPressed(self):
        currentState = gpio.input(self.pin)
        if self.checkPressed(currentState):
            self.onPressed()
        self.prevState = currentState
        sleep(0.05)

    def checkPressed(self, currentState):
        return currentState == gpio.HIGH and self.prevState == gpio.LOW

password = "111"

leds = (Led(16, "RED"), Led(20, "YELLOW"), Led(21, "GREEN"))

def ledRedFunction():
    def threadRun():
        leds[0].blink(3, 0.5)

    thread = Thread(target=threadRun, daemon=True)
    thread.start()

def ledYellowFunction():
    def threadRun():
        leds[1].blink(3, 0.5)

    thread = Thread(target=threadRun, daemon=True)
    thread.start()

def ledGreenFunction():
    def threadRun():
        leds[2].blink(3, 0.5)

    thread = Thread(target=threadRun, daemon=True)
    thread.start()

buttons = (Button(13, ledRedFunction), Button(19, ledYellowFunction), Button(26, ledGreenFunction))

try:
    prePassword = ""

    while True:
        for button in buttons:
            button.waitPressed()
            prePassword = button
            if len(prePassword) == 3:
                break

        if password == prePassword:
            for i in len(prePassword):
                leds[i].blink(3, 0.5)
        else:
            leds[0].blink(3, 0.5)
            leds[1].blink(3, 0.5)
            leds[2].blink(3, 0.5)

except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()