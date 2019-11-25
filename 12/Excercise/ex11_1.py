f = open("py_test.txt", "r")

wa = f.readline()
print(wa)

f.seek(0,0)

for i in f.readlines():
    print(i)

f.seek(0,0)

j = f.read(5)
print(j)

j = f.read(10)
print(j)

f.close()
f = open("py_test.txt", "a")
f.write("React")
f.close()
f = open("py_test.txt", "r")
print(f.read())