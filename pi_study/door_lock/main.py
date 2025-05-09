from door_lock.config.gpio_config import GpioConfig
from door_lock.service.door_lock_service import ModuleService, DoorLockService

if __name__ == "__main__":
    try:
        GpioConfig.setMode()
        DoorLockService.setModule()
        buttons = ModuleService.getButtonMoules()
        while True:
            for button in buttons:
                button.onClick()
    except KeyboardInterrupt:
        pass
    finally:
        GpioConfig.cleanup()

