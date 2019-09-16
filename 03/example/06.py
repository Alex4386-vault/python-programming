## Python I/O

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def getType(self):
        return type(self.age), type(self.name)

me = Person(input("type the age: "), input("type the name: "))

typeOfAge, typeOfName = me.getType()

print(typeOfAge)
print(typeOfName)
