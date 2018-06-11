class Pow:
    def __init__(self,n=2,m=0):
        self.m=m
        self.n=n
    def __iter__(self):
        self.c=1
        return self
    def __next__(self):
        if self.c<=self.m:
            self.c=self.c+1
            r=self.n**self.c
            return r
        else: 
            raise StopIteration("you have used all the powers")
p=Pow(6,10)
p=iter(p)
while input("press something"):
    try:
        n=next(p)
        print(n)
    except StopIteration as e:
        print("error",e)

