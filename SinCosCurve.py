import matplotlib.pyplot as plt
import numpy as np

#set a x value from zero to 4π in increment of 0.1 radians
x=np.arrange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,x,z)
plt.show()
