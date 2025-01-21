class DCmotor:
    def __init__(self, s1, s2, en, min_dty_cyc = 15000, max_dty_cyc = 65000):
        self.s1 = s1
        self.s2 = s2
        self.en = en
        self.min_dty_cyc = min_dty_cyc
        self.max_dty_cyc = max_dty_cyc
    
    def fwd(self, pwm):
        self.pwm = pwm