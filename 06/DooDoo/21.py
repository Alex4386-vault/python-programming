# cast float list to int

theList = [1.2, 2.4, 3.6, 4.8]

for a in range(len(theList)):
    theList[a] = int(theList[a])

print(theList)