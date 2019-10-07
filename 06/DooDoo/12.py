# Object Pointers in Python

a = 1

# shallow copy a
b = a

# Compare by value
print(a == b)

# Compare by pointer
print(a is b)

# Return pointer
print(hex(id(a)))
print(hex(id(b)))
