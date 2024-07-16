import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    password = '120804',
    database = 'ABC_STUDENT'
)

x = db.cursor()

# x.execute("create table login(id int auto_increment,fname varchar(255),lname varchar(255),mail varchar(255),primary key(id))")
# x.execute("insert into login(fname,lname,mail)values('kashish','patil','kash1208@gmail.com')")

# no = int(input("Enter number of record : "))
# for i in range(no):
#    print("--- Enter value ---")
#    fname = input("Plase enter first name- ")
#    lname = input("Plase enter last name - ")
#    mail = input("Plase enter mail id    - ")
#    x.execute("insert into login(fname,lname,mail) values('"+fname+"','"+lname+"','"+mail+"')")
# print("--- value enter successfully ---")
# 

# idno = input("Please enter id no : ")
#  
# fname = input("Plase enter first name- ")
# lname = input("Plase enter last name - ")
# mail = input("Plase enter mail id    - ")
# 
# x.execute("update login set fname = '"+ fname +"',lname = '"+lname+"',mail = '"+mail+"' where id = '"+idno+"'")
# print("--- Record succesfully update... ---") 
x.execute("select * from login")
for i in x :  
    print(i)

idno = input("Please enter id no : ")
x.execute("delete from login where id = '"+idno+"'")
print("--- delete succesfully id no : '"+idno+"'... ---")
db.commit() 
