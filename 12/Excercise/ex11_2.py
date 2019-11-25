f = open("f1.txt", "w")

f.write("we\n")
f.write("are\n")
f.write("in\n")
f.write("2019\n")

f.close()

f = open("f1.txt", "r")

print(f.read())

print()

f.seek(0,0)

line = len(f.readlines())

f.seek(0,0)
char = len(f.read())

print("line :", line, "char :", char)

