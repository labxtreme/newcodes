import sqlite3 as sql
db=sql.connect("st_data.db")
c=db.cursor()
while input("press something to add values in database in tables"):
    cmd="insert into student values('{0}',{1},'{2}',{3},'{4}','{5}')"
    name=input("Enter name : ")
    sid=int(input("Enter Id "))
    crs=input("course : ")
    fees=float(input("Fees : "))
    ph=input("Enter phone number : ")
    email=input("Email : ")
    cmd=cmd.format(name,sid,crs,fees,ph,email)
    c.execute(cmd)
    db.commit()
c.close()
db.close()
