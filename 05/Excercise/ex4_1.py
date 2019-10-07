number = int(input("Enter a number: "))

lastPwr = 1

#total = int(number % 10)
#
#while number >= (10**lastPwr):
#    total += (number % (10**(lastPwr+1))) // (10**lastPwr)
#    lastPwr += 1

total = 0

while number > 0:
    total += int(number % 10)
    number = number // 10


print("The sum of the digits is:", total)

