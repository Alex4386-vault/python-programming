## HOMEWORK 1

i = 100

# operator module
import operator as op

print("Addition: {}".format(op.add(i,1)))
print("Subtraction: {}".format(op.sub(i,1)))
print("Multiplication: {}".format(op.mul(i,100)))
print("Division: {}".format(op.truediv(i,100)))

print()

# special methods
print("Addition: {}".format(i.__add__(1)))
print("Subtraction: {}".format(i.__sub__(1)))
print("Multiplication: {}".format(i.__mul__(100)))
print("Division: {}".format(i.__truediv__(100)))

print()

# operators
print("Addition: {}".format(i+1))
print("Subtraction: {}".format(i-1))
print("Multiplication: {}".format(i*100))
print("Division: {}".format(i/100))

print()


## HOMEWORK 2

class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    
    def getSalary(self):
        print("{}'s salary is {}".format(self.name, self.salary))
    
    def getCount(self):
        print("Total employee count : {}".format(Employee.count))


kim = Employee("kim", 2000)
kim.getSalary()
kim.getCount()


lee = Employee("lee", 3000)
lee.getSalary()
lee.getCount()
