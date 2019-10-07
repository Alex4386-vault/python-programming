lower = int(input("Enter the lower limit for the range:"))
upper = int(input("Enter the upper limit for the range:"))

currentNum = lower if lower % 2 == 1 else lower+1

while currentNum < upper:
    print(currentNum)
    currentNum += 2
