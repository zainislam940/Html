class Employee:
    company = "Google"
    def showdetails(self):
        print("thhis is a Employee")
class Programmer:
    language = "python"
    def getlanguage(self):
        print("the language is {self.language}")
    def showdetails(self):
        print("this is a programmer")

e = Employee()
p = Programmer()
p.showdetails()    