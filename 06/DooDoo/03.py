# methods in list
whereToGo = [ "Venis", "Rome", "New York" ]

# in python, It is not push. It's append.
whereToGo.append("San Fransico")

# Insert to specific index.
whereToGo.insert(2, "California")

# Gimme the length
len(whereToGo)

# delete by name
whereToGo.remove("Venis")

# delete by index
del whereToGo[1]

# pop the list
sf = whereToGo.pop()
print(sf)

# clear the list
whereToGo.clear()
