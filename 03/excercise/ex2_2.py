## Exercise 2

def getIntInput(ah):
    validNumbers = False

    while not validNumbers:
        try:
            No = int(input(ah))
        except ValueError:
            print("Enter Valid Number!!")
        else:
            validNumbers = True
            return No

cubeMe = getIntInput("Enter any number: ")
print("The cube of number {cubeMe} = {cubed}".format(cubeMe = cubeMe, cubed = cubeMe**3))
