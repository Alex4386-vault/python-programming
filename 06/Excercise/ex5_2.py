s = [1, 2, 3]
t = ['begin', s, 'end']

for i in range(len(t)):
    currentList = t[i]
    for j in range(len(currentList)):
        print(t[i][j], end=' ')
    print()

