class Programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"the nameof a Programmer is {self.name} and the product is {self.product}") 
harry = Programmer("harry","github")
alka = Programmer("alka","skpe")
harry.getinfo()
alka.getinfo()
