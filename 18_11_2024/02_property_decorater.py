class Employee:
   company = "lesco"
   salary = 5500
   salarybonus = 500
#    totalsalary= 6100
@property
def totalsalary(self):
    return self.salary + self.salarybonus
e = Employee()
print(e.totalsalary)
e.salary = 5500    
