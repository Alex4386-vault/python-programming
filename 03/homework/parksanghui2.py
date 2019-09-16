##########################
#       HOMEWORK 1       #
##########################

'''
# Try to import math library

try:
    import math
except ImportError:
    print("math is not available")
    PI = 3.1415926535897932384
else:
    PI = math.pi
'''

# Override:
PI = 3.14

try:
    radius = float(input("Please Enter the Radius of a Cylinder: "))
    height = float(input("Please Enter the Height of a Cylinder: "))
except ValueError:
    print("Improper Input detected")
    exit(1)

print(" The Surface Area of a Cylinder = "+str( (2*PI*(radius**2)) + (2*PI*radius*height)))
print(" The Volume of a Cylinder = "+str( PI*(radius**2)*height ))




##########################
#       HOMEWORK 2       #
##########################

try:
    mrFahrenheit = float(input("Please enter a temperature in ℉ : "))
except ValueError:
    print("Improper input detected")
    exit(1)

print("{mrFahrenheit} ℉ = {superSonicManOuttaYou} ℃".format(mrFahrenheit = mrFahrenheit, superSonicManOuttaYou = (5/9) * (mrFahrenheit - 32)))




##########################
#       HOMEWORK 3       #
##########################

try:
    side1 = float(input("Enter the First side of a Triangle: "))
    side2 = float(input("Enter the Second side of a Triangle: "))
    side3 = float(input("Enter the Third side of a Triangle: "))
except ValueError:
    print("Improper input detected")
    exit(1)

print()

perimeter = side1+side2+side3
print("The Perimeter of Triangle = {perimeter}".format(perimeter = perimeter))

semiperimeter = perimeter / 2
print("The Semi Permieter of Triangle = {semiperimeter}".format(semiperimeter = semiperimeter))

area = (semiperimeter * (semiperimeter - side1) * (semiperimeter - side2) * (semiperimeter - side3)) ** (1/2)
print("The Area of Triangle is %.2f" % area)
