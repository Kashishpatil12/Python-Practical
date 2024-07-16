student = {
    'roll' : '1',
    'fname' : '2',
    'lname' : '3',
    'course' : 'ccc',
    'date'   : '2023-06-01'
}
print(student)
for i in student.items() :
    print([i])

print("---nested dict----")
course = {
    'ccc' : {
        'duration' : '2 months',
        'fees' : '3000'
        },
    'python' : {
        'duration' : '6 months',
        'fees' : '10000'
    },
    'java' : {
        'duration'  : '7 months',
        'fees' : '6000'
    }

}
print(course)

# print(course['ccc']['duration'])
for i,j in course.items() : 
    print(j,i)
