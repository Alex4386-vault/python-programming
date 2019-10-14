tu = (12, 54, 37, 'bar')

try: 
    tu.append(50)

except AttributeError:
    print("tuple doesn't have append method")

try: 
    tu.remove(12)

except AttributeError:
    print("tuple doesn't have remove method")
