from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(26))

def map(value, from_low, from_high, to_low, to_high):
    return (value - from_low) * (to_high - to_low) // (from_high - from_low) + to_low

while True:
  reading = pot.read_u16() # read value, 0-65535 across voltage range 0.0v - 3.3v
  mapped = map(reading, 0, 65535, 0, 255)
  print(mapped)
  sleep(0.5)
