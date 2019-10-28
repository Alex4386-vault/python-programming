def calc(choice, arg1, arg2):
    if choice == 1:
        return arg1+arg2
    elif choice == 2:
        return arg1-arg2
    elif choice == 3:
        return arg1*arg2
    elif choice == 4:
        return arg1/arg2
    else:
        return None

getInput = lambda : (int(input("Enter first number: ")), int(input("Enter second number: ")))

choice = int(input("Enter choice(1.add/2.subtract/3.multiply/4.divide): "))
userInput = getInput()
print(calc(choice, userInput[0], userInput[1]))
