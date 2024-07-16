a = int(input("Maths : "))
b = int(input("English : "))
c = int(input("Gujrati : "))
d = int(input("Science : "))
e = int(input("SS : "))

Total = a+b+c+d+e
if Total >80 and Total<100  :
    print("Grad A")
elif Total >70  and Total<80:
    print("Grad B")
elif Total >60 and Total<70  :
    print("Grad C")
elif Total >50 and Total<60  :
    print("Grad D")
else :
    print("FAIL")
per = Total / 5
print("Total  : ",Total)
print("Percentage : ",per)












