theNum = int(input("Enter the Number : "))

for i in range(1, theNum+1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()
    