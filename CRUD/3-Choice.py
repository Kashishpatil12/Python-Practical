import mysql.connector

a = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '120804',
    database = 'ABC_STUDENT'
)
b = a.cursor()
b.execute("select * from st_detail")
for i in b :
    print(i)
a.commit()

# b.execute("create table st_detail(id int auto_increment,fname varchar(50),lname varchar(50),address varchar(255),primary key(id))")
choice = int(input("--- Select Choice : \n 1 :- Add values \n 2 :- Update values \n 3 :- Delete Values \n"))

if choice == 1:
    no = int(input("Enter number of List : "))
    for i in range(no) :
        print("*** Enter value ***")
        fname = input("Enter fname  :")
        lname = input("Enter lame   :")
        address = input("Enter Address  :")
        b.execute("insert into st_detail(fname,lname,address)values('"+fname+"','"+lname+"','"+address+"')")
    print("--- Successfully Add Values ---")

elif choice==2 :
    no_id = int(input("Enter id number for update value : "))
    fname = input("Enter fname : ")
    lname = input("Enter lname : ")
    address = input("Enter Address : ")
    b.execute("update st_detail set fname = '"+fname+"',lname ='"+lname+"',address = '"+address+"' where id = '"+no_id+"'")
    print("--- Value successfully uapdate ---")

elif choice== 3 :
    no_id = int(input("Enter id number for delete value : "))
    b.execute("delete from st_detail where id = '"+no_id+"'") 
    print("--- value delete succesfully ---")



