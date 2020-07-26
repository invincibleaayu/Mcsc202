# Write a program to calculate the sum of squares of natural n natural numbers 1
# 2 + 2
# 2 +

# ⋯ + n
# 2
# . Calculate the sum when n = 5.

number=int(input("Please enter the number of the series you want to find the sum of:"))

def calc_squareSum(number):
    sum=0
    for num in range(1,number+1):
        sum+=(num**2)
    return sum

s="%.2f"%(calc_squareSum(number))
print("The  square sum up to the number  {} is {}".format(number,s))