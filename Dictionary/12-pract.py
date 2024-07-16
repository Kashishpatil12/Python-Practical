sci = {
    'students' : 120,
    'm' : 60,
    'f' : 60
}
com = {
    'students' : 90,
    'm' : 45,
    'n' : 45 
}
arts = {
    'students' : 60,
    'm' : 30,
    'n' : 30
}
all_students = {
    'sci1' : sci,
    'com1' : com,
    'arts1' : arts,
}
print(all_students)

sum = 0
for i in all_students :
    print(i)
    print(all_students[i]['m'])
    sum = sum + all_students[i]['students']
    print("total number of students is : ",sum)

    print(sci.get('students'))