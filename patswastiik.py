for valr in range(1,14):
    for valc in range(1,14): 
        if valr==1:
            if valc==1 or valc in range(7,14):
                print("*",end="  ")                     
            else:
                print(" ",end="  ")
        elif valr in range(2,7):
            if valc==1 or valc==7:
                print("*",end="  ")                     
            else:
                print(" ",end="  ")
        elif valr==7:
            print("*",end="  ")
        elif valr in range (8,13):
            if valc==7 or valc==13:
                print("*",end="  ")                     
            else:
                print(" ",end="  ")
        else: 
            if valc==13 or valc in range(1,8):
                print("*",end="  ")                     
            else:
                print(" ",end="  ")
    print("\n")
