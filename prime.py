n=int(input("Starting point : "))
e=int(input("Ending POint : "))
count=0
while n<=e :
    
        c = 2
        import math
        sq=math.sqrt(n)+1
        while c <= sq:
       
            if n % c == 0:
            
                break
        
            elif c == sq  :
        
                print(n, end="\t")
                count=count+1
       
            c=c+1
        n=n+1

print("\n\ncount=",count)        
