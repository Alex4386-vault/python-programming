matrixSize = int(input("Enter a number: "))

for y in range(0, matrixSize):
    for x in range(0, matrixSize):
        if x == y:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    