r=int(input("Enter no. of rows :"))
r=r-1
i=0
j=0
while i<r+1:
   for col in range(0,2*r+1):
       if col in range(r-j,r+j+1):
             print("*",end="")
       else :
             print(" ",end="")
   print("\n")
   j=j+1
   i=i+1

