""" 
low = int(input("Enter the Low Value : "))
high = int(input("Enter the High Value : "))

for currentNum in range(low, high):
    for divisor in range(2, int(currentNum**(1/2))+2):
        if currentNum % divisor == 0:
            break
    else:
        print(currentNum, end=' ')
print()
 """

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
