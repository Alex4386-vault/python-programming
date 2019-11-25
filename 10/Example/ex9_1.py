class Polygon:
    sideNo = 0
    sidesLength = []

    def __init__(self, sideNo):
        self.sideNo = sideNo
        self.sidesLength = [ 0 for i in range(sideNo) ]
    
    def inputSides(self):
        self.sidesLength = [ 
            float(input("Enter side "+str(i+1)+" : "))
            for i in range(self.sideNo)
        ]
    
    def displaySides(self):
        [ print("Side", i+1, "is", self.sidesLength[i]) for i in range(self.sideNo) ]


class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)
    
    def semiPerimeter(self):
        return sum(self.sidesLength) / 2

    def findArea(self):
        p = self.semiPerimeter()
        a,b,c = self.sidesLength
        return ( p * (p - a) * (p - b) * (p - c) ) ** (1/2)

    def printArea(self):
        print("The area of the triangle is %0.2f" % self.findArea())

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)

    def inputSides(self):
        h = float(input("Enter horizontal length : "))
        v = float(input("Enter vertical length : "))

        self.sidesLength = [h, v, h, v]
    
    def findArea(self):
        return h*v

    def printArea(self):
        print("The area of the rectangle is %0.2f" % self.findArea())


triangle = Triangle()
triangle.inputSides()
triangle.displaySides()
triangle.printArea()