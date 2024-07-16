maths = float(input("maths : "))
dbms  = float(input("dbms : "))
python  = float(input("python : "))
java  = float(input("java : "))
ds  = float(input("ds : "))

Total = maths + dbms + python + java + ds 
print("Total : ",Total)

percentage = Total / 5
print("Per : " , percentage,"%")

if percentage>80 : 
    print("Grade : A")
elif percentage>70 :
    print("Grade : B")
elif percentage>60 : 
    print("Grade : C")
elif percentage>50 : 
    print("Grade : D")
else :
    print("Fail")