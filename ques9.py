# Write a program to find the smallest integer n such that 3
# n ≥ 2000
def calc_n():
    n=0
    while True:
        if (3**n)>= 2000:
            break
        n+=1
    print("The smallest integer is {} such that 3**n>=2000".format(n))

calc_n()