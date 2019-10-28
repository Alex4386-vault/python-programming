# Short coding version
[ a for a in [[ int(input("Enter "+("first" if i == 0 else "second")+" number: ")) for i in range(0,2) ]] if print("quotient: "+str(a[0]//a[1])+", remainder: "+str(a[0]%a[1])) ]

first,second = int(input("Enter first number: ")), int(input("Enter second number: "))
print("quotient: "+str(first//second)+", remainder: "+str(first%second))