words = ["seoul", "tokyo", "moskoba", "toronto", "queensland", "beijing", "rome"]

longerthan5 = []
longerthan5len = []

for value in words:
    if len(value) > 5:
        longerthan5.append(value)
        longerthan5len.append(len(value))

print("satisfy name\t:", longerthan5)
print("satisfy length\t:", longerthan5len)
