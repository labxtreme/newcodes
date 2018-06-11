X=int(input())
from collections import Counter
coun=Counter(map(int,input().split()))
N=int(input())
money=0
for i in range(N):
    k,v=map(int,input().split())
    for key,value in coun.items():
        if key==6 and value!=0:
            coun[k]=value-1
            money+=v
           
print(money)
