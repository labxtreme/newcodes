import sqlite3 as sql
def query():
    try:
        db=sql.connect('st_data.db')
        c=db.cursor()
    except Exception as error:
        print("Error : ",error)
        exit(0)

    print("\t1. Show All Data\n\t2.Query with Id\n\t3.Query with fees")
    ch=int(input("Choice :"))
    if ch==1:
        cmd="select * from student"
        c.execute(cmd)
        data=c.fetchall()
        print("{:>10}{:>8}{:>20}{:>15}{:>20}{:>40}".format("Name","ID","Course","fees","ph_no","Email"))
        for d in data:
            print("{:>10}{:>8}{:>20}{:>15}{:>20}{:>40}".format(*d))
    elif ch==2:
        sid=int(input("Enter Id : "))
        c.execute("select * from student where id={}".format(sid))
        data=c.fetchone()
        print("{:>10}{:>8}{:>20}{:>15}{:>20}{:>40}".format("Name","ID","Course","fees","ph_no","Email"))
        print("{:>10}{:>8}{:>20}{:>15}{:>20}{:>40}".format(*data))
    elif ch==3:
        fee=float(input("Enter fees : "))
        c.execute("select * from student where fees={}".format(fee))
        data=c.fetchall()
        print("{:>10}{:>8}{:>20}{:>15}{:>20}{:>40}".format("Name","ID","Course","fees","ph_no","Email"))
        for d in data:
            print("{:>10}{:>8}{:>20}{:>15}{:>20}{:>40}".format(*d))
    else:
        print("wrong choice")
        exit(0)
query() 
