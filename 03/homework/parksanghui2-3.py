try:
    side1 = float(input("Enter the First side of a Triangle"))
    side2 = float(input("Enter the Second side of a Triangle"))
    side3 = float(input("Enter the Third side of a Triangle"))
except ValueError:
    print("Improper input detected")
    exit(1)

print()

perimeter = side1+side2+side3
print("The Perimeter of Triangle = {perimeter}".format(perimeter = perimeter))

semiperimeter = perimeter / 2
print("The Semi Permieter of Triangle = {semiperimeter}".format(semiperimeter = semiperimeter))

area = (semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)) ** (1/2)
print("The Area of Triangle is {area}".format(area = area))
