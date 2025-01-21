from machine import Pin
from time import sleep

led = Pin(20, Pin.OUT)
button = Pin(21, Pin.IN, Pin.PULL_DOWN)

while True:
  if(button.value() == 1):
      led.toggle()
      # print('toggle')
