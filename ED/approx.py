import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

x = [2]
y = [-1]
dt = 1e-3

for _ in range(5000):
    x.append(x[-1] + dt)
    y.append(y[-1] + (0.2 * x[-2]**2 + y[-1]) * dt)
    
x2 = [2]
y2 = [-1]

for _ in range(8000):
    x2.append(x2[-1] - dt)
    y2.append(y2[-1] - (0.2 * x2[-2]**2 + y2[-1]) * dt)


plt.plot(x2[::-1] + x, y2[::-1] + y)
x = [0]
y = [0.5]
dt = 1e-3

for _ in range(2000):
    x.append(x[-1] + dt)
    y.append(y[-1] + (0.2 * x[-2]**2 + y[-1]) * dt)
    
x2 = [0]
y2 = [0.5]

for _ in range(6000):
    x2.append(x2[-1] - dt)
    y2.append(y2[-1] - (0.2 * x2[-2]**2 + y2[-1]) * dt)
plt.plot(x2[::-1] + x, y2[::-1] + y)
plt.axis([-7, 7, -4, 4])
plt.show()



