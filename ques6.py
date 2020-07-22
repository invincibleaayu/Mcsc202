# Write a program to calculate the factorial of a positive integer input by the user.
# (a) Write the factorial function using a Python while loop.
# (b) Write the factorial function using a Python for loop.
# Check your programs to make sure they work for 0,1, 2, 3, 4,5
value =abs(int(input("Enter the number you want to find the factorial of :")))
count=1
factorial=1
#now we calculate the factorial using while loop
while count <= value:
    factorial*=count
    count+=1

print("The factorial of {} using while loop is {} ".format(value,factorial))

#now we calculate factorial using for loop
value_for =abs(int(input("Enter the number you want to find the factorial of :")))
factorial=1
for i in range(1,(value_for+1)):
    factorial*=i
print("The factorial of {} using for loop is {}".format(value_for,factorial))
