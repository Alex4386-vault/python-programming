num = abs(int(input("Enter number : ")))

digits = 0

while num != 0:
    digits += 1
    num //= 10

print("The number of digits in the number is: {digits}".format(
    digits=digits
))
