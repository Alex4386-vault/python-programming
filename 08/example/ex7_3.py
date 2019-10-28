[ a for a in [[ int(input("Enter "+("first" if i == 0 else "second")+" number: ")) for i in range(0,2) ]] if print("quotient: "+str(a[0]//a[1])+", remainder: "+str(a[0]%a[1])) ]

