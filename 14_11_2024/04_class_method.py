class Employee:
    company = "camel"
    salary = 100
    location = "delhi"
@classmethod
def changeSalary(cls,sal):
    cls.salary = sal
e = Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)
print(Employee.salary)
