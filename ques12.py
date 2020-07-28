#  Plot the space curve x = 2θcos θ, y = 2θsin θ, z = 1 + 2 θ for 0 ≤ θ ≤ 20π
from mpl_toolkits import mplot3d 
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
ax=plt.axes(projection='3d')   #created x,y,z dimension
#now we create numpy array to store values
theta=np.linspace(0,20*np.pi,1000) #higjer the interval better will be the smoothness of curve
x=2*theta*np.cos(theta)
y=2*theta*np.sin(theta)
z=1+(2*theta)
#now we plot the curve
ax.plot3D(x,y,z,"blue")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Space curve")
plt.show()

