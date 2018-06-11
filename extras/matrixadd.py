m,n=map(int,input("Enter m and n of the matrix:").split())
A=[list(map(int,input("Enter the whole row of matrix A %d :"%(row+1) ).split())) for row in range(m)]
B=[list(map(int,input("Enter the whole row of matrix B %d :"%(row+1) ).split())) for row in range(m)]
C=[[A[row][col]+B[row][col] for col in range(n)]for row in range(m)]
for var in C:
    print(*C)
