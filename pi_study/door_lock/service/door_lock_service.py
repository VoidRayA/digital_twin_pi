import RPi.GPIO as gpio
from door_lock.constant.password import PASSWORD
from door_lock.module.led import Led
from door_lock.module.button import Button, ButtonEvent
from time import sleep

class ModuleService:
    ledModules = []
    buttonModules = []

    @classmethod
    def addLedModule(cls, led:Led):
        cls.ledModules.append(led)

    @classmethod
    def addButtonModule(cls, button:Button):
        cls.buttonModules.append(button)

    @classmethod
    def getLedMoules(cls):
        return cls.ledModules

    @classmethod
    def getButtonMoules(cls):
        return cls.buttonModules

class DoorLockService:

    currentInputPassword = ""

    @classmethod
    def getPassword(cls):
        return PASSWORD

    @classmethod
    def setModule(cls):
        led1 = Led(16, "RED")
        led2 = Led(20, "YELLOW")
        led3 = Led(21, "GREEN")
        ModuleService.addLedModule(led1)
        ModuleService.addLedModule(led2)
        ModuleService.addLedModule(led3)

        button1 = Button(13, "1")
        cls.setLedOnAndOffButtonEvent(button1, led1)
        button2 = Button(19, "2")
        cls.setLedOnAndOffButtonEvent(button2, led2)
        button3 = Button(26, "3")
        cls.setLedOnAndOffButtonEvent(button3, led3)

        ModuleService.addButtonModule(button1)
        ModuleService.addButtonModule(button2)
        ModuleService.addButtonModule(button3)

    @classmethod
    def setLedOnAndOffButtonEvent(cls, button, led):
        def handleButtonOnClick():
            led.ledBlink(1, 0.01)
            if len(cls.currentInputPassword) < 3:
                cls.currentInputPassword += button.value
                if len(cls.currentInputPassword) == 3:
                    cls.checkPassword()
                    cls.currentInputPassword = ""
            else:
                cls.currentInputPassword = ""

        buttonEvent = ButtonEvent(handleButtonOnClick)
        button.setButtonEvent(buttonEvent)

    @classmethod
    def checkPassword(cls):
        if cls.getPassword() == DoorLockService.currentInputPassword:
            for _ in range(3):
                for ledModule in ModuleService.getLedMoules():
                    ledModule.ledBlink(1, 0.1)
        else:
            for _ in range(3):
                for ledModule in ModuleService.getLedMoules():
                    ledModule.ledOn()
                sleep(0.1)
                for ledModule in ModuleService.getLedMoules():
                    ledModule.ledOff()
                sleep(0.1)
