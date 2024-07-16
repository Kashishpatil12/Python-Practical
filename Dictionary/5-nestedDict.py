course = {
    "java" : { 
        "duration" : "2 month",
        "fees" : 10000
    },
    "html" : {
        "duration"  : "1 month",
        "fees"  : 3000
    },
    "math"  : { 
        "duration"  : "1 month",
        "fees"  : 4000
    },
}
s = {1,2,23,44,55,5}

d = {
    'username' : 'talant1201',
    'password' : 'tcit1201' 
}
print("-----------------------------")
print(d['username'])
print("-----------------------------")
d['username'] = 'talantcomputer'
print(d['username'])
print("-----------------------------")
d.update({'username' : '12082004'})
print(d['username'])
print("-----------------------------")
print(d.values())
print("-----------------------------")
print(d)

for i,j in d.items():
    print(i,j)
