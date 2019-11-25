from caesar import caesarSubstitution

try:
    cipherTextFile = open("cypher.txt", "r")
except FileNotFoundError:
    print("cypher.txt File Not Found!!!")
    exit(1)
except IOError:
    print("cypher.txt File I/O Error detected!")
    exit(1)

shiftCheck = False

while not shiftCheck:
    try:
        shift = int(input("Enter how many characters you want to shift for decryption? : "))
        shiftCheck = True
    except ValueError:
        print("Invalid Input detected")

cipherText = cipherTextFile.read()
decryptedText = caesarSubstitution(cipherText, shift)

try:
    decryptedTextFile = open("decrypted.txt", "w")
    decryptedTextFile.write(decryptedText)
    decryptedTextFile.close()
except IOError:
    print("decrypted.txt File I/O Error Detected!!!")
    exit(1)






samsame = False

try:
    plainTextFile = open("original.txt", "r")
except FileNotFoundError:
    print("original.txt File Not Found!!!")
    exit(1)
except IOError:
    print("original.txt File I/O Error detected!")
    exit(1)

plainText = plainTextFile.read()

if len(plainText) == len(decryptedText):
    for i in range(0, len(plainText)):
        if not plainText[i] == decryptedText[i]:
            samsame = False
            break
        else:
            samsame = True

print("decrypted.txt and original.txt is", "same" if samsame else "different", ".")
