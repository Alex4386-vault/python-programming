class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print("Hello, My name is {} and my age is {}".format(self.name, self.age))
    def __del__(self):
        print("Deconstructing Person {}.".format(self.name))

p1 = Person("John", 36)
p1.greeting()

p1.age = 40
p1.greeting()

# WAIT THAT'S ILLEGAL
del p1.age

# FUCK SERIOUSLY? NO DESTRUCTOR?
del p1

try:
    p1.greeting()
except NameError:
    print("No class object called p1 detected.")


