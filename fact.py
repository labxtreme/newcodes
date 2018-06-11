def fact(x):
	if x>0:
		return x*fact(x-1)
	elif x==0:
		return 1
	else: 
		return 'Error! Negative numbers do not have factorial'
op=fact(int(input("Enter the no you wanna find factorial of : ")))
print(op)
