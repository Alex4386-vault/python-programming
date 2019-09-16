## Python I/O

validNumbers = False

while not validNumbers:
    try:
        firstNum = int(input("Enter the first No.: "))
    except ValueError:
        print("Enter Valid Number!!")
    else:
        validNumbers = True

validNumbers = False

while not validNumbers:
    try:
        secondNum = int(input("Enter the second No.: "))
    except ValueError:
        print("Enter Valid Number!!")
    else:
        validNumbers = True

total = firstNum + secondNum

print("Sum of two numbers:", total)
