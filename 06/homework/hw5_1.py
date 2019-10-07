print("Let's make a shopping list!")
print("Exit is \"quit\"")
print()
currentInput = ""
theShoppingList = []

while currentInput != "quit":
    for index, value in enumerate(theShoppingList):
        print(
            "{humanReadableIndex} {value}".format(
                humanReadableIndex = index+1,
                value = value
            )
        )

    currentInput = input("Please enter what you want : ")

    theShoppingList.append(currentInput)

