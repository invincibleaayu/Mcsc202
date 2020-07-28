# Write the program for (i) surface plot (ii) contour plot on xy −plane of the function
# f(x, y) =1−x2+x5+y 5 e−x 2−y 2 on the domain -−3 ≤ x ≤ 3 and − 3 ≤ y ≤ 3
from mpl_toolkits import mplot3d 
import matplotlib.pyplot as plt
import numpy as np

#now we create numpy array to store values
def f(x,y):
    return ((1-(x/2)+(x**5)+(y**5))/(np.exp((-x**2)-(y**2))))
x=np.linspace(-3,3,1000)
y=np.linspace(-3,3,1000)
X, Y = np.meshgrid(x,y)
Z=f(X,Y)

def surface(X,Y,Z):
    #now we plot for surface curve
    fig=plt.figure()
    ax=plt.axes(projection='3d')   #created x,y,z dimension
    ax.plot_surface(X,Y,Z,cmap="plasma")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("Surface curve")
    plt.show()

    
def contour(X,Y,Z):
    #now we plot contour curve
    fig=plt.figure()
    ax=plt.axes(projection='3d')   #created x,y,z dimension
    ax.view_init(20,100) # View angle
    plt.contourf(X,Y,Z,100,cmap='jet')    
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.set_title("Contour curve")
    plt.show()

c=contour(X,Y,Z)
s=surface(X,Y,Z)








