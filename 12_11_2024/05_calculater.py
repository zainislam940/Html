class Calculator:
   def __init__(self,num):
     self.num = num
     def square(self):
      print(f"the value of {self.num} square is {self.num**2}")
     def squareroot(self):
      print(f"the value of {self.num} square root is {self.num**0.5}")
     def cube(self):
      print(f"the value of {self.num} cube is {self.num**3}")
      @staticmethod
      def greet():
            print("welcome to the he best calculator of the world")
a = Calculator(3)
# a.square()
a.greet()
a.squareroot()
a.cube()
      