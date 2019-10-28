x = 5

def add(y):
    total = x + y
    return total

print(add(4))

try:
    print(total)
except NameError:
    print("total is only available in add")
