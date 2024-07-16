import mysql.connector

a = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '120804',
    database = 'ABC_STUDENT'
)

b = a.cursor()

# b.execute("CREATE DATABASE ABC_STUDENT")
# b.execute("create table Login(fname varchar(20),lname varchar(20));")
# b.execute("insert into login(fname,lname)values('priya','sharma')")
# b.execute("delete from login where fname ='priya'")
# b.execute("update login set lname='patel' where fname ='sikha' ")
# a.commit()
b.execute("select * from login")

for i in b :
    print(i)



