
a = "Python"

try:
    b = a.copy()
except AttributeError:
    print("Python doesn't support deep copying string. It's immutable")