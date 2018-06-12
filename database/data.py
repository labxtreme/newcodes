import sqlite3 as sql
db=sql.connect('st_data.db')
c=db.cursor()
cmd ="Create Table student(name varchar(30) not null,id int(6) primary key,course varchar(500) not null,fees float not null,\
        ph_no varchar(20) not null, email varchar(100))" 

c.execute(cmd)
db.commit()
c.close()
db.close()
