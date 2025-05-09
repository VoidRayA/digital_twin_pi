import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)

# === 클래스 정의 ===
class Led:
    def __init__(self, pin):
        self.pin = pin
        gpio.setup(self.pin, gpio.OUT)
        gpio.output(self.pin, gpio.LOW)

    def blink(self, count=1, delay=0.3):
        for _ in range(count):
            gpio.output(self.pin, gpio.HIGH)
            sleep(delay)
            gpio.output(self.pin, gpio.LOW)
            sleep(delay)

    def on(self):
        gpio.output(self.pin, gpio.HIGH)

    def off(self):
        gpio.output(self.pin, gpio.LOW)

class Button:
    def __init__(self, pin, on_pressed):
        self.pin = pin
        self.prev_state = gpio.LOW
        self.on_pressed = on_pressed
        gpio.setup(self.pin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

    def wait_pressed(self):
        current_state = gpio.input(self.pin)
        if current_state == gpio.HIGH and self.prev_state == gpio.LOW:
            self.on_pressed()
        self.prev_state = current_state
        sleep(0.05)

# === 설정 ===
led_pins = [16, 20, 21]  # 빨강, 노랑, 초록
button_pins = [13, 19, 26]  # 버튼 1, 2, 3

leds = [Led(pin) for pin in led_pins]
input_buffer = ""
password = "123"

# === LED 시퀀스 ===
def all_leds_off():
    for led in leds:
        led.off()

def success_sequence():
    for _ in range(3):
        for i in range(3):
            all_leds_off()
            leds[i].on()
            sleep(0.3)
    all_leds_off()

def failure_sequence():
    for _ in range(3):
        for led in leds:
            led.on()
        sleep(0.3)
        all_leds_off()
        sleep(0.3)

# === 입력 처리 ===
def handle_input(digit):
    global input_buffer
    input_buffer += str(digit)
    leds[digit - 1].blink()

    if len(input_buffer) == 3:
        print(f"입력된 비밀번호: {input_buffer}")
        if input_buffer == password:
            success_sequence()
        else:
            failure_sequence()
        input_buffer = ""

# === 버튼 설정 ===
buttons = [
    Button(button_pins[0], lambda: handle_input(1)),
    Button(button_pins[1], lambda: handle_input(2)),
    Button(button_pins[2], lambda: handle_input(3))
]

# === 메인 루프 ===
try:
    print("비밀번호 입력을 시작하세요.")
    while True:
        for button in buttons:
            button.wait_pressed()

except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    gpio.cleanup()