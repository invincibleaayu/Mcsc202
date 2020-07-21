import numpy as np
#we need to create a numpy array of size 9 with space 2 between 0 and 29
r=np.arange(0,29,2)
print(r) #[ 0  2  4  6  8 10 12 14 16 18 20 22 24 26 28]
#now we need to clculate the square using addition and multiplication
twice_using_multiplication=r*2
print("List of array to calcukate twice using multiplication",twice_using_multiplication)
twice_using_addition=r+r
print("List of array to calculate twice using addition",twice_using_addition)


