try:
    import pickle
except ModuleNotFoundError:
    print("pickle module is not found!")

datFile = open("f3.dat", "wb")

currentInput = 1

while not currentInput == 0:
    try:
        currentInput = int(input("insert integer number (if 0? end insert) : "))
        pickle.dump(currentInput, datFile)
    except ValueError:
        print("Invalid Input Detected")



datFile.close()

datFile = open("f3.dat", "rb")

while True:
    try:
        print(pickle.load(datFile), end=' ')
    except EOFError:
        print()
        break;

datFile.close()