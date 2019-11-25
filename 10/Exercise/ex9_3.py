import math

class Circle:
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def cCircumference(self):
        return math.pi * 2 * self.radius
    
    def cArea(self):
        return (self.radius ** 2) * math.pi


circle = Circle(int(input("radius : ")))
print(circle.cCircumference())
print(circle.cArea())



