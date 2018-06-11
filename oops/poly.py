class Poly:
    """HI I AM A POLYGON CLASS"""
    def __init__(self,name,NOS=0):
            self.n=NOS
            self.sides = [0 for var in range(NOS)]

    def set_Sides(self):
        n=self.n
        self.sides=[]
        self.sides=[float(input("Enter Side{} :".format(var))) for var in range (1,n+1)]

    def get_sides(self):
        n=self.n
        for var in range(1,n+1):
            print("Side{} = {}".format(var,self.sides[var-1]))






