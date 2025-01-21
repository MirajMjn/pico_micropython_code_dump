from machine import PWM, Pin
from time import sleep

# L298N pins
IN1 = Pin(16, Pin.OUT)
IN2 = Pin(17, Pin.OUT)
ENA = Pin(15)

frequency = 5000
ENA_pwm = PWM(ENA)
ENA_pwm.freq(frequency)
delay = 1

def fwd(pwm):
    ENA_pwm.duty_u16(pwm)
    IN1.value(1)
    IN2.value(0)
    
def rev(pwm):
    ENA_pwm.duty_u16(pwm)
    IN1.value(0)
    IN2.value(1)
    
def hlt():
    ENA_pwm.duty_u16(65535) # ENA = 1 basically
    IN1.value(1)
    IN2.value(1)

def idle():
    ENA_pwm.duty_u16(0) # ENA = 1 basically
    IN1.value(0)
    IN2.value(0)
    
try:
    while True:
        for pwm in range(15000, 65000, 1000):
            print(pwm)
            fwd(pwm)
            sleep(delay)
        for pwm in range(65000, 15000, -1000):
            print(pwm)
            fwd(pwm)
            sleep(delay)
        
        hlt()
        print('!! HALT !!')
        sleep(5)
        
        for pwm in range(15000, 65000, 1000):
            print(pwm)
            rev(pwm)
            sleep(delay)
        for pwm in range(65000, 15000, -1000):
            print(pwm)
            rev(pwm)
            sleep(delay)
            
except KeyboardInterrupt:
    print('keyboard interrupt')
    
finally:
    idle()
    print('Power Off')
            
        