print("Enter 3 numbers")
n1=input("Number 1 : ")
n2=input("Number 2 : ")
n3=input("Number 3 : ")
gr8=0
if n1>=n2 and n1>=n3:
 gr8=n1
elif n2>=n1 and n2>=n3:
 gr8=n2
else: 
 gr8=n3

print("The Greatest Number is",gr8)

input("Enter any key to exit")


