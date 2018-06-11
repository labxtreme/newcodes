i=int(input("Enter the limit to fabbinoci series : "))
a=0
b=1
print(a,end=" ")
print(b,end=" ")
i=i-2
while(i>0):
    c=a+b
    a=b
    b=c
    print(b,end=" ")
    i=i-1
