f = open("test2.txt", "r")

for i, string in enumerate(f.readlines()):
    print(str(i+1)+":"+string.replace("\n",""))