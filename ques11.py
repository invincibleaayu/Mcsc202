# Plot the functions y = sin x and y = cos x for −2π ≤ x ≤ 2π on the same plot. Plot
# y = sin x in the color red and y = cos x in the color blue and include a legend to label
# the two curves. Place the legend within the plot, but such that it does not cover either of
# the sine or cosine traces.
import matplotlib.pylab as plt
import numpy as np
x=np.linspace(-2*np.pi,2*np.pi,100)#creating numpy array for value of x
y1=np.sin(x)                    #function
y2=np.cos(x)
plt.plot(x,y1,"r")               # plot graph of red color
plt.plot(x,y2,"b")              #plot graph of blue color
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Plot of sine and cosine function")
plt.show()
