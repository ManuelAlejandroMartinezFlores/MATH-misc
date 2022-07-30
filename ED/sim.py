import numpy as np 


class Cont:
    def __init__(self):
        self.gal = 100
        self.lb = 10 
        
    def step(self):
        self.gal += 2
        self.lb += 3 - 4 * self.lb / self.gal 
        return self.lb 
    
    

c = Cont()
for _ in range(30):
    ans = c.step()
    
print(ans)