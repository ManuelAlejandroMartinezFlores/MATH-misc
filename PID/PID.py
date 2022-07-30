import numpy as np
import matplotlib.pyplot as plt
import random 


class System:
    def __init__(self, S, T0=0, dt=1e-2, Tmax=None):
        if not Tmax: Tmax = S * 1.3
        self.S = S 
        self.T = T0 
        self.Tsys = T0
        self.dt = dt 
        self.Tmax = Tmax 
        self.Tmin = 0
        self.T0 = T0
        self.nstep = 0
        self.noise = 5
        
    def reset_state(self):
        self.T = self.T0 
        self.Tsys = self.T0
        self.nstep = 0
        
    def step(self, adjust):
        self.Tsys += adjust
        self.nstep += 1
        if self.Tsys > self.Tmax: self.Tsys = self.Tmax
        if self.Tsys < self.Tmin: self.Tsys = self.Tmin
        # self.T = self.Tsys + (self.T - self.Tsys) * np.exp(-self.dt) 
        self.T -= (self.T - self.Tsys) * self.dt
        if self.nstep == self.noise:
            self.nstep = 0
            self.T += random.random() * 2 - 1.3
        return self.T, self.S - self.T, self.dt, self.Tsys
    
    
class PID:
    def __init__(self, Kp, Ki, Kd, reset=10, max_adjust=1):
        self.Kp = Kp 
        self.Ki = Ki 
        self.Kd = Kd 
        self.reset = reset
        self.nstep = 0
        self.Ie = 0
        self.laste = 0
        self.max_adjust = max_adjust
        
    def reset_state(self):
        self.nstep = 0
        self.Ie = 0
        self.laste = 0
        
    def step(self, error, dt, train=False):
        self.nstep += 1 
        self.Ie += dt * error
        if self.nstep == self.reset: self.reset = 0
        st = self.Kp * error + self.Ki * self.Ie + self.Kd * (error - self.laste) / dt 
        self.laste = error 
        if st > 1:
            return 1 
        if st < -1: 
            return -1
        return st
    
    
def train(sys:System, pid:PID, epochs=10, iters=100, lr=0.01):
    total_errors = []
    for epoch in range(epochs): 
        errors = []
        sys.reset_state()
        pid.reset_state()
        for _ in range(iters):
            T, error, dt, Tsys = sys.step(adjust) 
            Ts.append(T)
            Tsyss.append(Tsys)
            adjust, (err, Ie, De) = pid.step(error, dt, True)
            
            
        
        
        
if __name__ == '__main__':
    sys = System(30)
    pid = PID(0.7, 0.05, 0.2)
    Ts = []
    Tsyss = []
    Ss = []
    adjust = 0
    errors = []
    for k in range(1000):
        if k == 700:
            sys.S = 20
        T, error, dt, Tsys = sys.step(adjust) 
        errors.append(error)
        Ts.append(T)
        Tsyss.append(Tsys)
        adjust = pid.step(error, dt)
        Ss.append(sys.S)
    plt.subplot(211) 
    plt.plot(Ss, '--')  
    plt.plot(Ts)
    plt.title(f'Sistema {np.abs(errors).mean():.4f}')
    plt.subplot(212)
    plt.plot(Tsyss)
    plt.show()
