# LM393Tachometer
# Specs : 20 slits on encoder disk and rpm is calculated every second (1000 ms)

from machine import Pin, Timer
from time import ticks_us, ticks_diff

class Tachometer:
    def __init__(self, pin_num, slits=20, calc_interval=1000): 
        self.pin = Pin(pin_num, Pin.IN)
        self.slits = slits
        self.calc_interval = calc_interval
        self.pulse_count = 0
        #self.current_rpm = 0
        self.rpm = 0
        self.last_pulse_time = 0
        
        # Attach interrupt for pulse counting
        self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.intr_counter)
        
        # Timer for RPM calculation
        self.timer = Timer()
        self.timer.init(period=self.calc_interval, mode=Timer.PERIODIC, callback=self.calc_rpm)

    def intr_counter(self, pin):
        #self.pulse_count += 1
        current_time = ticks_us()
        
        #software debounce to help reduce multiple triggerings
        if ticks_diff(current_time, self.last_pulse_time) > 500:
            self.pulse_count += 1
            self.last_pulse_time = current_time

    def calc_rpm(self, timer):
        self.rpm = (self.pulse_count) * 3
        #self.current_rpm = (self.pulse_count / self.slits) * (60 / (self.calc_interval / 1000))
        #self.current_rpm = (self.pulse_count) * 3
        self.pulse_count = 0
        
        #using Exponential Moving Average to reduce random sensor fluctuation impact..kind of
        #alpha = 0.7
        #self.rpm = (alpha * self.current_rpm) + ((1 - alpha) * self.rpm)
        
        
    def get_rpm(self):
        return self.rpm
    
    def stop(self):
        self.timer.deinit()
        self.pin.irq(handler=None)

