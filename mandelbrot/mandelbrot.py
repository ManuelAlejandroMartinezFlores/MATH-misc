import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


def count(c):
    z = 0
    for k in range(100):
        z = z**2 + c
        if abs(z) > 2:
            return k 
    
    return k 

mm = []
aa = []
bb = []
for a in np.linspace(-1.5, 0.5, 1000):
    for b in np.linspace(-1, 1, 1000):
        mm.append(count(a + b*1j))
        aa.append(a)
        bb.append(b)
        
mm = np.array(mm).reshape(1000, 1000)
mm = np.rot90(mm)
sns.heatmap(mm)
plt.savefig("mandelbrot.png")
plt.show()

