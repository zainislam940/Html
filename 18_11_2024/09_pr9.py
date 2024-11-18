# (a+bi)(c+di)=(ac-bd)+(ad+bc)i
class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i
    def __add__(self , c):
        return complex(self.real + c.real , self.imaginary + c.imaginary)
    def __mul__(self , c):
        mulreal =self.real * c.real - self.imaginary * c.imaginary 
        mulImg = self.real + c.imaginary , self.imaginary + c.real
        return complex(mulreal,mulImg)
c1  = complex(3, 2)
c2 = complex(1, 7) 
print(c1+c2)
print(c2+c1)       