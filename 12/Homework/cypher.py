from caesar import caesarSubstitution

try:
    plainTextFile = open("original.txt", "r")
except FileNotFoundError:
    print("original.txt File Not Found!!!")
    exit(1)
except IOError:
    print("original.txt File I/O Error detected!")
    exit(1)

shiftCheck = False

while not shiftCheck:
    try:
        shift = int(input("Enter how many characters you want to shift for encryption? : "))
        shiftCheck = True
    except ValueError:
        print("Invalid Input detected")

plainText = plainTextFile.read()

cipherText = caesarSubstitution(plainText, shift)

try:
    cipherTextFile = open("cypher.txt", "w")
    cipherTextFile.write(cipherText)
    cipherTextFile.close()
except IOError:
    print("cypher.txt File I/O Error Detected!!!")
    exit(1)

