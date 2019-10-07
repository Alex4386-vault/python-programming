theValue = int(input("Enter any integer below 10: "))
incrementalValue = theValue

while incrementalValue <= 10:
    print("Total= "+str(theValue))
    incrementalValue += 1
    theValue += incrementalValue
else:
    print("Your value is greater than 10.")
    # if while statement was terminated
    # via break in the while statement,
    # else statement will not be executed.
    