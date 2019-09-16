## Python I/O

class Employee:
    def __init__(self, employeeName, salary, companyName):
        self.employeeName = employeeName
        self.salary = salary
        self.companyName = companyName

    def getEmployeeDetail(self):
        employeeDetail = "Name: "+self.employeeName+"\n"
        employeeDetail += "Salary: "+str(self.salary)+"\n"
        employeeDetail += "Company Name: "+self.companyName
        return employeeDetail

    @staticmethod
    def getEmployeeDetailHeader():
        return "** Printing Employee Detail Header **"

employee = Employee(input("Type the Name of employee: "), input("Type the Salary of employee: "), input("Type the CompanyName of employee: "))

print(Employee.getEmployeeDetailHeader())

print(employee.getEmployeeDetail())
