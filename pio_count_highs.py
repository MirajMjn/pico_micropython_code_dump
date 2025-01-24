import rp2
from machine import Pin

# Define the PIO program for counting high signals
@rp2.asm_pio()
def count_low():
    wait(0, pin, 0)       # Wait for the input pin to go LOW
    mov(x, x+1)        # Increment the X register
    wait(1, pin, 0)       # Wait for the input pin to go HIGH

# Set up the button pin (adjust GPIO pin as necessary)
button_pin = 16  # GPIO pin connected to the button
pin = Pin(button_pin, Pin.IN, Pin.PULL_UP)

# Instantiate the state machine
sm = rp2.StateMachine(0, count_low, in_base=pin)

# Start the state machine
sm.active(1)

# Function to read the count from the PIO
def read_count():
    return sm.get()  # Pull the X register value into the Python environment

# Main loop
try:
    while True:
        # Get the count from the PIO
        count = read_count()
        print(f"Button pressed {count} times")
except KeyboardInterrupt:
    sm.active(0)
    print("Program stopped")
