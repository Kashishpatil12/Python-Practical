student = {
    
    "st1"  : {
        "name" : "kashish",
        "no"   : 2004
    },
    "st2"  : {
        "name" : "sidhi",
        "no"   :  2005
    },
    "st3" : {
        "name" : "Neha",
        "no"   : 2008
    }
}
print(student)
print("__________________________________________")
for i in student.items() :
    for j in i:
        print(j)

print("____________________________________________________________________________________")

child1 = {
    "name" : "krishna",
    "age" : 19
}
child2 = {
    "name" : "ram",
    "age"  : 25
}
child3 = {
    "name" : "shyam",
    "age" : 35
}

myfamily = {
    "elder" : child1,
    "younger" : child2,
    "older" : child3
}

print(myfamily["older"]["name"])