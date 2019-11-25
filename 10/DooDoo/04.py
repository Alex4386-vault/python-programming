class Car:
    name = ""
    speed = ""

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def printMe(self):
        print("{}'s speed is {}".format(self.getName(), self.getSpeed()))


car1 = Car("Audi", 10)
car2 = Car("BMW", 30)

print("Result:")
car1.printMe()
car2.printMe()

car1.speed += 10
car2.speed += 10
print()

car1.printMe()
car2.printMe()


