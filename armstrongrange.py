x=int(input("Enter starting point : "))
y=int(input("Enter ending point : "))
count=0
for var in range(x,y+1):
    temp=0
    z=var
    while z:
        temp=temp+(z%10)**3
        z=z//10
    if temp==var:
        print(temp,end="\t")
        count=count+1
print("\n\nThere are {} armstrong numbers between {} and {}".format(count,x,y))
