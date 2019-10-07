# factorial

num = int(input("Enter a number: "))

fac = 1
for i in range(num, 0, -1):
    fac *= i

print("The factorial of {num} is {factorial}".format(
    num=num, factorial=fac
))
