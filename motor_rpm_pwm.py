from machine import PWM, Pin, ADC, Timer
from time import sleep

# button interrupt setup
bt_pin = Pin(21, Pin.IN, Pin.PULL_UP)
pwm = 20000

def button_isr(bt_pin):
    global pwm
    if(pwm == 20000):
        pwm = 64000
    elif(pwm == 15000):
        pwm = 64000
    else:
        pwm = 15000

bt_pin.irq(trigger=(Pin.IRQ_FALLING), handler=button_isr)

# encoder (interrupt) setup
enc_pin = Pin(22, Pin.IN, Pin.PULL_UP)
count = 0
rpm = 0

def enc_isr(enc_pin):
    global count
    count +=1

enc_pin.irq(trigger=(Pin.IRQ_FALLING), handler=enc_isr)

# timer setup code
timer_1 = Timer()

def calc_rpm(timer_1):
    global rpm
    global count
    rpm = count * 3
    count = 0 

timer_1.init(freq=1, mode=Timer.PERIODIC, callback=calc_rpm)

# L298N pins
IN1 = Pin(16, Pin.OUT)
IN2 = Pin(17, Pin.OUT)
ENA = Pin(15)

frequency = 1000
ENA_pwm = PWM(ENA)
ENA_pwm.freq(frequency)

# set motor direction as fwd
IN1.value(1)
IN2.value(0)

try:
    while True:
        ENA_pwm.duty_u16(pwm)
        print(f"pwm = {pwm} rpm = {rpm}")
        sleep(0.5)
            
except KeyboardInterrupt:
    print('keyboard interrupt')
    
finally:
    timer_1.deinit()  # Deinitialize the timer
    ENA_pwm.duty_u16(0) # ENA = 0 basically
    IN1.value(0)
    IN2.value(0)
    ENA_pwm.deinit()
    print('Power Off')
            
        
