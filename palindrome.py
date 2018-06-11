x=int(input("Enter a number : "))
y=x
temp=0
while y:
    temp=temp*10+y%10
    y=y//10
if temp==x:
    print("The number is Palindrome")
else:
    print("The number is not Palindrome")
