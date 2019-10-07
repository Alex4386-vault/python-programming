tu = (12, 54, 37, "bar")

try:
    tu.append(50)
except AttributeError:
    print("tuple doesn't have method \"append\"")

try:
    tu.remove(12)
except AttributeError:
    print("tuple doesn't have method \"remove\"")

try:
    tu[0] = 20
except TypeError:
    print("tuple can't be assigned.")