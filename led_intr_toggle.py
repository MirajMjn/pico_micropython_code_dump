from machine import Pin
from time import sleep

intr_pin = Pin(22, Pin.IN, Pin.PULL_UP) # this is a button

# note that the button needs to be debounced, for me a 104 ceramic cap grounding the button pin worked
# see https://youtu.be/e1-kc04jSE4?t=37 

led_pin = Pin(21, Pin.OUT)

intr_count = 0

def button_isr(pin):
    global intr_count
    global led_pin
    #sleep(0.2)
    led_pin.toggle()
    intr_count +=1

intr_pin.irq(trigger=(Pin.IRQ_FALLING), handler=button_isr)

try:
    #led_pin.value(0)
    while True:
        print(f"count = {intr_count}")
        sleep(1)  # Main loop delay

except KeyboardInterrupt:
    print("Keyboard interrupt")
    
except Exception as e:
    print("An unexpected exception occurred:", e)

finally:
    intr_pin.irq(trigger=0)  # Disable the interrupt
    led_pin.value(0)  # Turn off the LED