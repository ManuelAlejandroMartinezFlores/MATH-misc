import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns
import random

N = 10
RANDOM = True
if not RANDOM:
    ROOTS = [np.cos(2 * np.pi * n / N) + np.sin(2 * np.pi * n / N)*1j for n in range(N)]
else:
    ROOTS = [random.random() * 2 - 1 + (random.random() * 2 - 1) * 1j for _ in range(N)]
TOL = 1e-6


def f(x):
    ans = 1 / (N ** 3)
    for r in ROOTS:
        ans *= (x - r)
    return ans 



def color(x):
    for k in range(200):
        if k % 10 == 9:
            for n, root in enumerate(ROOTS):
                if abs(root - x) < TOL:
                    return n 
                
        df = (f(x + TOL) - f(x - TOL)) / (2 * TOL)
        x = x - f(x) / df
        
    return len(ROOTS)


mm = []
n = 0
for a in np.linspace(-2, 2, 1000):
    for b in np.linspace(-2, 2, 1000):
        mm.append(color(a + b*1j))
        n += 1 
        if n / (1000 * 10) % 10 == 0:
            print(n / (1000 * 10))
    

        
mm = np.array(mm).reshape(1000, 1000)
mm = np.rot90(mm)
sns.heatmap(mm)
rand_string = 'rand' if RANDOM else ''
plt.savefig(f"newton-fractal{len(ROOTS)}{rand_string}.png")