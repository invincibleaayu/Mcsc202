# Write a program to tell the nature of the roots and values of the roots of a quadratic
# equation ax

# ax^2 + bx + c = 0, a ≠ 0.
import math
import  numpy as np
a,b,c=input("Enter the value for a,b,c :").split()
a=float(a)
b=float(b)
c=float(c)

#for solving this problem we need to calculate the discriminant
discriminant=((b*b)-(4*a*c))
print(discriminant)
#now we calculate the root for different value of discriminant
if (discriminant  > 0):
    x1="%.2f"%(((-b + math.sqrt(discriminant)) / (2 * a)))
    x2="%.2f"%((-b - math.sqrt(discriminant)) / (2 * a))
    print("The value of two root are {} and {}".format(x1,x2))
elif (discriminant  < 0):
    x1="%.2f"%(((-b + math.sqrt(-discriminant)) / (2 * a)))
    x2="%.2f"%((-b - math.sqrt(-discriminant)) / (2 * a))
    print("The value of two root are {} and {}".format(x1,x2))
elif (discriminant  == 0):
    x="%.2f"%((-b  / (2 * a)))
    print("The value of  root is {}".format(x))
