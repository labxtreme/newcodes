m,n=map(int,input("Enter m and n of the matrix:").split())
A=[list(map(int,input("Enter the whole row %d :"%(row+1) ).split())) for row in range(m)]
B=[[A[col][row] for col in range(m)] for row in range(n)]
print("A")
for var in A :
    print(*var)
print("B")
for var in B :
    print(*var)

