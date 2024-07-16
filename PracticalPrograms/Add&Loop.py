com_st = ["kashish","siddhi","riddhi","Paridhi","nidhi"]
sci_st = ["ankita","anita","nikita","amrita","susita"]

print("Commerce students : ")
for x in com_st : 
    print(x)
print("-------------------------------------")
print("Scince students : ")
for y in sci_st : 
    print(y)
print("-------------------------------------")

print("Total Students : ")
com_st.extend(sci_st)
for total in com_st :
    print(total)

print("-------------------------------------")
students = []
for i in com_st :
    if "dhi" in i :
        students.append(i)
for a in students : 
    print(a)

print("--------------------------------------")
print("Replace name Khushi on 1: ")
students[1] = "Khushi"
for a in students : 
    print(a)

print("--------------------------------------")
students.insert(2,"kashish")
for a in students : 
    print(a)




















