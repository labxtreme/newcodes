from poly import Poly
from math import sqrt
class Triangle(Poly):   
    def __init__(self,name):
        Poly.__init__(self,name,3)
        
    def area(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=sqrt(s*(s-a)*(s-b)*(s-c))
        return area
