import numpy as np
import math
#we have
g=9.8#acceleration due to gravity
ho=10#height
np_height=np.arange(10,0,-0.5)
print(np_height)
#we need to calculate the sequence of time at a 
# given height which is stored in numpy array
time=[]
for y in np_height:
    t="%.2f"%((math.sqrt(2*(ho-y)))/g)
    time.append(t)

print("The sequence of time in a givin height is",time)
#now we calcaulate the average velocity
del_y=-0.5 #for each interval according to ques
average_velocity=[]
for t in range(0,(len(time)-1)):
    average_velocity.append("%.2f"%(del_y/(float(time[t+1])-float(time[t]))))
print("The average velocity is ",average_velocity)
