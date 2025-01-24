from machine import Pin
from time import sleep
led = Pin('LED', Pin.OUT)

try:
    while True:
      led.value(not led.value())
      sleep(1.0)

except KeyboardInterrupt:
    print("Keyboard Interrupt")
    
finally:
    led.value(0)
    print("Power Off")