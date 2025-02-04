from machine import Pin, PWM
from time import sleep

class DCmotor_PID_Controller:
    def __init__(self, in1, in2, Kp = 1.0, Ki = 0.1, Kd = 0.05):
        #DC motor driver input pins
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)
        
        #Input pins PWM config
        self.in1_pwm = PWM(self.in1)
        self.in1_pwm.freq(1000)
        self.in2_pwm = PWM(self.in2)
        self.in2_pwm.freq(1000)
        
        #min and max duty cycles
        self.min_dty_u16 = 8000
        self.max_dty_u16 = 55000
        self.ignition_dty_u16 = 16000 #a minimum value of pwm to start motor from rest
        self.current_dty_u16 = 0
        
        self.target_rpm = 0
        self.current_rpm = 0
        self.direction = 1 # 1 is forward, -1 is reverse
        self.error = 0
        self.integral = 0
        self.Kp = Kp
        self.Ki = Ki
        #self.Kd = Kd
        
    def pid_control(self):
        self.error = self.target_rpm - self.current_rpm
        self.integral += self.error
        #derivative = error - last_error
        self.current_dty_u16 = self.Kp * self.error + self.Ki * self.integral #+ Kd * derivative
        return max(min(self.current_dty_u16, self.max_dty_u16), self.min_dty_u16)

    def run(self, current_rpm, target_rpm):
        self.target_rpm = abs(target_rpm)
        self.direction = -1 if target_rpm<0 else 1
        self.current_rpm = current_rpm
        
        if(self.target_rpm == 0): #basically idle
            self.current_dty_u16 = 0
        else: #when motor needs to operate at certain rpm
            self.pid_control()
            if(self.direction == -1):
                self.in1_pwm.duty_u16(0)
                if(self.current_rpm == 0): #when starting from rest it needs extra to get started
                    self.in2_pwm.duty_u16(self.ignition_dty_u16)
                    sleep(0.2)
                self.in2_pwm.duty_u16(self.current_dty_u16)
            else:
                self.in2_pwm.duty_u16(0)
                if(self.current_rpm == 0): #when starting from rest it needs extra to get started
                    self.in1_pwm.duty_u16(self.ignition_dty_u16)
                    sleep(0.2)
                self.in1_pwm.duty_u16(self.current_dty_u16)
    
    def deinit(self):
        self.in1_pwm.duty_u16(0)
        self.in2_pwm.duty_u16(0)
        sleep(0.1)
        self.in1_pwm.deinit()
        self.in2_pwm.deinit()