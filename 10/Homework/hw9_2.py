class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    
    def getSalary(self):
        return self.salary
    
    def getCount(self):
        return Employee.count


kim = Employee("kim", 2000)
print("{}'s salary is {}".format(kim.name, kim.getSalary()))
print("Total employee count : {}".format(Employee.count))

lee = Employee("lee", 3000)
print("{}'s salary is {}".format(lee.name, lee.getSalary()))
print("Total employee count : {}".format(Employee.count))
