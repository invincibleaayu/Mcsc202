# Write a program to calculate the sum of natural n natural numbers 1 + 2 + ⋯ + n.
# Calculate the sum when the n = 10
number=int(input("Please enter the number upto which you want find the sum:"))
#now we calculate the sum
def calc_sum(number):
    sum=0
    for num in range(1,number+1):
        sum+=num
    return sum

c=calc_sum(number)
print("the sum upto the number {} is {} ".format(number,c))
