from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(26))

while True:
  reading = pot.read_u16() # read value, 0-65535 across voltage range 0.0v - 3.3v
  mapped_reading = reading // 256
  print(mapped_reading)
  sleep(0.5)