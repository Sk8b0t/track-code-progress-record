from matplotlib import pyplot as plt
import numpy as np
x=np.arange(-10,11)
y=x*x
plt.plot(x,y,label="Parabola")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
