num = int(input("Enter the number: "))

if num >= 0:
    currentNum = 0
    total = 0
    while currentNum <= num:
        total += currentNum
        currentNum += 1
    print("total: {total}".format(total=total))
else:
    # All Other Programming Languages:
    #   Throw an exception
    #
    # Python:
    #   Raise an exception
    #
    # Programmer:
    #   FUUUUUUUUUUUCK
    print("Please Enter Positive Number")
    raise ValueError("Expected a Positive Number, but got a negative number: "+str(num))
