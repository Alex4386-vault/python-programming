## Excercise 1

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
            

n1 = getIntInput("type n1:")
n2 = getIntInput("type n2:")
n3 = getIntInput("type n3:")

if n1 > n2 and n1 > n3:
    print("n1 is the biggest")
else:
    print("n1 is not the biggest number")