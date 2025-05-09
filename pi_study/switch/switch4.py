import RPi.GPIO as gpio
from time import sleep

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

leds = (Led(16, "RED"), Led(20, "YELLOW"), Led(21, "GREEN"))
input_buffer = ""
password = "123"

def all_leds_off():
    for led in leds:
        led.ledOff()

def success_sequence():
    for _ in range(3):
        for i in range(3):
            all_leds_off()
            leds[i].ledOn()
            sleep(0.3)
    all_leds_off()

def failure_sequence():
    for _ in range(3):
        for led in leds:
            led.ledOn()
        sleep(0.3)
        all_leds_off()
        sleep(0.3)

def ledRedFunction():
    handle_input(1)

def ledYellowFunction():
    handle_input(2)

def ledGreenFunction():
    handle_input(3)

def handle_input(digit):
    global input_buffer
    input_buffer += str(digit)
    leds[digit - 1].blink(1, 0.3)

    if len(input_buffer) == 3:
        if input_buffer == password:
            success_sequence()
        else:
            failure_sequence()
        input_buffer = ""

buttons = (Button(13, ledRedFunction), Button(19, ledYellowFunction), Button(26, ledGreenFunction))

try:
    while True:
        for button in buttons:
            button.waitPressed()

except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()