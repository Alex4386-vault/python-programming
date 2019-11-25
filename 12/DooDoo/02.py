f = open("foo.txt", "w")
f.write("123\n")
f.write("456\n")
f.close()

f1 = open("foo.txt", "r")
print(f1.read())
f1.close()