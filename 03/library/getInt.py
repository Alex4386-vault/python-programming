
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
            