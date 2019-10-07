first = int(input("Enter the First Value: "))
second = int(input("Enter the Second Value: "))

i = 0

# get which is bigger: minimize iteration
big = first if first >= second else second

theLCM = big
while True:
    if theLCM % first == 0 and theLCM % second == 0:
        break
    theLCM += 1

print("LCM of {first} and {second} = {theLCM}".format(
    first=first,
    second=second,
    theLCM=theLCM
))
