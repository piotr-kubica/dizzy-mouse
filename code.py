import time
import usb_hid
import board
import digitalio
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = False

btn_pin = digitalio.DigitalInOut(board.GP20)
btn_pin.direction = digitalio.Direction.INPUT
btn_pin.pull = digitalio.Pull.UP

is_movement_on = False

while True:
    # pulled high -> check negative
    if not btn_pin.value:
        # debounce
        time.sleep(0.10)
        if not btn_pin.value:
            is_movement_on = not is_movement_on
            led.value = is_movement_on
            print('movement is: ' + str(is_movement_on))
            # prevent from too early switch back
            time.sleep(2.0)

    if is_movement_on:
        mouse.move(x=2)
        time.sleep(0.1)
        mouse.move(x=-2)
        time.sleep(0.1)
