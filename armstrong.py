x=int(input("Enter a number : "))
y=x
temp=0
while y:
    temp=temp+(y%10)**3
    y=y//10
if temp==x:
    print("The number is armstrong")
else:
    print("The number is not armstrong")

