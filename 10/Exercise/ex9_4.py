class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def move(self):
        print("{} move".format(self.name))



class Dog(Animal):
    def speak(self):
        print("bark!!!")



class Cat(Animal):
    def speak(self):
        # isn't it meow?
        print("myou!!!")

dog = Dog("doggy")
cat = Cat("catty")

dog.speak()
dog.move()
cat.speak()
cat.move()
