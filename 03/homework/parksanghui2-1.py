'''
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
