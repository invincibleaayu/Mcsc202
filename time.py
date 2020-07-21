# 1. A ball is thrown vertically up in the air from a height 𝑕0 above the ground at an initial
# velocity v0

# . Its subsequent height 𝑕 and velocity v are given by the equations

# 𝑕 = 𝑕0 + v0
# t −
# 1
# 2
# gt
# 2
# v = v0 − gt
# where g = 9.8 is the acceleration due to gravity in m/s
# 2
# . Write a script that finds the
# height 𝑕 and velocity v at a time t after the ball is thrown. Start the code by setting 𝑕0 = 1.2
# (meters) and v0 = 5.4 (m/s) and have your code print out the values of height and velocity.
# Then use the script to find the height and velocity after 0.5 seconds. Then modify your script
# to find them after 2.0 seconds.

def height_and_velocity(t):
    #we know we have given value as
    g=-9.8                                       #acceleration due to gravity in m/s^2
    ho=1.2                                      #initial height in m
    vo=5.4                                      #initial velocity in m/s
    #now we calculate height and velocity at a given time 
    h=ho+(vo*t)-((1/2)*g*t**2)
    #and the velocity is 
    v=vo-(g*t)
    print(h,v)

height_and_velocity(0.5)
height_and_velocity(2.0)