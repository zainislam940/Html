class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"


#  def changesalary(self, sal):
#         self.salary= sal 
    @classmethod
    def changesalary(cls, sal):
            cls.salary= sal 
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary
e = Employee()  
print(e.salary)
print(Employee.salary)    