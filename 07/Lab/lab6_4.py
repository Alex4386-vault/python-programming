aset = set()
bset = set()

a = int(input("1.Please enter a number : "))
b = int(input("2.Please enter a number : "))

aset = { i for i in range(1,a+1) if a % i == 0 }
print(aset)

bset = { i for i in range(1,b+1) if b % i == 0 }
print(bset)

print("Common factor :", aset & bset)

