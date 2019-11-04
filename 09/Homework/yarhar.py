import random
import time

dataInput = lambda x:input(x + " data input (seperated by comma(,)) : ").split(",")
shake = lambda x:random.shuffle(x)

member = dataInput("First")
match = dataInput("Second")

if len(member) != len(match):
    print("The data list length is not same!!!")
    exit(1)

print("Shaking for 3 seconds")
shake(member)
shake(match)
shakeResult = zip(member, match)
time.sleep(3)

print()
print("Congratulations~~~")
print()

for x,y in shakeResult:
    print(x, "<=========>", y)





