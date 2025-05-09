import RPi.GPIO as gpio

class GpioConfig:

    @staticmethod
    def setMode():
        gpio.setmode(gpio.BCM)

    @staticmethod
    def cleanup():
        gpio.cleanup()