class student :
    def get_student_details(self) : 
        self.__name =input("Enter student name : ")
        self.__no = int(input("Enter Roll No : "))
        print("Enter Subject Marks ")
        self.__java = int(input("Enter Java Marks     : "))
        self.__python = int(input("Enter Python Marks : "))
        self.__html = int(input("Enter html Marks     : "))
    
    def getdata(self):
        print(self.__no,self.__name,(self.__java + self.__python + self.__java)/3)
        
           

Studentarray=[]

while(True):
    s = student()
    s.get_student_details()
    Studentarray.append(s)
    ch =int(input("Are u want to Add : Yes for or NO [0] for other"))
    if ch == 0 :
        break
print("Result : ")    
for i in Studentarray :
    print(i.getdata())
    



    
    


    