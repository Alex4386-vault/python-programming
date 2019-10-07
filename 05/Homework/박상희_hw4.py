###################################
#     APPLICATION PROGRAMMING     #
###################################

###################
#    HOMEWORK 1   #
###################
 #       _       #
 #      / |      #
 #      | |      #
 #      | |      #
 #      |_|      #
 #               #
 #################

num = abs(int(input("Enter number : ")))

digitCount = 0

while num != 0:
    digitCount += 1
    num //= 10

print("The number of digits in the number is: {digitCount}".format(
    digitCount=digitCount
))




###################
#    HOMEWORK 2   #
###################
 #               #
 #     _____     #
 #    |___  \    #
 #      __) |    #
 #     / __/     #
 #    |_____|    #
 #               #
 #################

num = int(input("Enter a number : "))

theStr = ''
a = num
count = 0

while num != 0:
    theStr += str(num % 10)
    num //= 10
    count += 1

revNum = 0
iteration = 1
while a != 0:
    revNum += (a % 10) * (10 ** (count - iteration))
    a //= 10
    iteration += 1

print("Reverse of the number : {revNum}".format(
    revNum = revNum
))




###################
#    HOMEWORK 3   #
###################
 #               #
 #     _____     #
 #    |___ /     #
 #      |_ \     #
 #     ___) |    #
 #    |____/     #
 #               #
 #################

matrixSize = int(input("Enter a number: "))

for y in range(0, matrixSize):
    for x in range(0, matrixSize):
        if x == y:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()



###################
#    HOMEWORK 4   #
###################
 #               #
 #     _  _      #
 #    | || |     #
 #    | || |_    #
 #    |__   _|   #
 #       |_|     #
 #               #
 #################

theNum = int(input("Enter the Number : "))

for i in range(1, theNum+1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()



###################
#    HOMEWORK 5   #
###################
 #               #
 #     ____      #
 #    | ___|     #
 #    |___ \     #
 #     ___) |    #
 #    |____/     #
 #               #
 #################

low = int(input("Enter the Low Value : "))
high = int(input("Enter the High Value : "))

for currentNum in range(low, high):
    # sqrt-ing for less interation
    for divisor in range(2, currentNum+1):
        if currentNum % divisor == 0:
            if currentNum == divisor:
                # This is prime number
                print(currentNum, end=' ')
            else:
                # This is not.
                continue
        
print()
