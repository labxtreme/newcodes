n1=list(map(int,input("Enter list 1:").split()))
n2=list(map(int,input("Enter list 2:").split()))
n=zip(n1,n2)
for key,value in n:
    print("{} + {} = {}".format(key,value,key+value))
