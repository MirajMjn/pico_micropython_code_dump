from machine import Pin, Timer
from time import ticks_ms

# Initialize the LED pin
led_pin = Pin(21, Pin.OUT)

# Create a timer instance
timer = Timer()

# Define the timer callback function
def toggle_led(timer):
    led_pin.toggle()
    print(ticks_ms())

# Configure the timer to call toggle_led function every 500 milliseconds
timer.init(freq=1, mode=Timer.PERIODIC, callback=toggle_led)

# Main loop (empty in this case)
try:
    while True:
        pass

except KeyboardInterrupt:
    print("Keyboard interrupt")

finally:
    timer.deinit()  # Deinitialize the timer
    led_pin.value(0)  # Turn off the LED
    print("Cleaned up and turned off the LED.")
