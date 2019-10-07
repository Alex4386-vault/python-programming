# range keyword

# range() output is class <range>
print(type(range(0,10,1)))

# so cast to list
test = list(range(0,10,1))

for mem in test:
    print(mem)
