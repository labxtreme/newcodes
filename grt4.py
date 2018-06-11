print("Enter 4 numbers")
n1=input("Number 1 : ")
n2=input("Number 2 : ")
n3=input("Number 3 : ")
n4=input("Number 4 : ")
gr8=0
if n1>=n2 and n1>=n3 and n1>=n4:
 gr8=n1
elif n2>=n1 and n2>=n3  and n2>=n4:
 gr8=n2
elif n3>=n1 and n3>=n2 and n3>=n4:
 gr8=n3
else:
 gr8=n4  

print("The Greatest Number is",gr8)

input("Enter any key to exit")



