while input("\n\nType something to continue ") :
    n = int(input("Enter a number : "))
    c = 2
    while c <= n//2+1 : 
        if n % c == 0 :
            print("\n\nNot Prime ")
            break 
        elif c == n - 1 :
            print("\n\nPrime")
        c = c + 1


