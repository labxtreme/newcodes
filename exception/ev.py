class Eve:
    def __init__(self):
        pass
    def __iter__(self):
        self.c=0
        return self
    def __next__(self):
            self.c=self.c+2
            return self.c
p=Eve()
p=iter(p)
while input("press something"):
        n=next(p)
        print(n)


