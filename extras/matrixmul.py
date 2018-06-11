m1,n1=map(int,input("Enter m and n of the matrix:").split())
m2,n2=map(int,input("Enter m and n of the matrix B:").split())
if(n1==m2):
    A=[list(map(int,input("Enter the whole row of matrix A %d :"%(row+1) ).split())) for row in range(m1)]
    B=[list(map(int,input("Enter the whole row of matrix B %d :"%(row+1) ).split())) for row in range(m2)]
    C=[[0 for col in range(n2)] for row in range(m1)]
    for i in range(m1):
        for j in range(n2):
            z=0
            for k in range(n1):
                  z+=A[i][k]*B[k][j]
            C[i][j]=z
    for var in C:
        print(*var)
else:
    print("Sorry these matrices aren't compatible for multiplication")
