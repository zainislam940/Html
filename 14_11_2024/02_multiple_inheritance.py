class employee:
    company = "visa"
    ecode = 120
class freelancer:
    company = "Fiverr"
    level = 0
    def upgradelevel(self):
        self.level = self.level + 1
class programmer(employee,freelancer):
       name = "Rohit"
p = programmer()
p.upgradelevel()
print(p.company)        

