all_students = {
    "sci" : {
        "m" : 40,
        "f" : 60
    },
    "com" : {
        "m" : 30,
        "f" : 80
    },
    "arts" : {
        "m" : 45,
        "f" : 90
    } 
}

print(all_students)
sum = 0
add = 0 
for i in all_students :
    print(i)
    print(all_students[i])
    if all_students[i]["m"]<=50 :
        sum +=  all_students[i]["m"]
        print(sum)
    if all_students[i]["f"]>=50 : 
       add += all_students[i]["f"]
       print(add)