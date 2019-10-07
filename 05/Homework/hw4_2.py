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
