def hello():
    try:
        x=int(input("Enter an integer :"))
        f=open(input("Enter file name :"))
        print(f.read())
        f.close()
    except ValueError as arg :
        print("Error!! please input only integer")
        hello()
    except FileNotFoundError as a:
        print("Erroe!! No such file exists make sure path is correct")
        hello()
hello()
