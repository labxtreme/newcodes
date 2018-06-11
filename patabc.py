i=0
k=1
while i<=5:
    j=0
    while j<=i:
        c=chr(64+k)
        k=k+1
        print(c,end=" ")
        j=j+1
    print("\n")
    i=i+1

