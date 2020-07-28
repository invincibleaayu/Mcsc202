# Plot the function y = 3x
# 2
# for −3 ≤ x ≤ 3. Include enough points (say 100 points) so

# that the curve you plot appears smooth. Label the axes x and y.
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-3,3,100)
y=3*(x**2)
plt.plot(x,y,"r")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph plot of 3x^2")
plt.show()
