thislist = ["apple","banana","cherry","mango"]

for i in thislist :
    print(i)
print("_______________________________________________________")


for i in range(len(thislist)) :
    print(thislist[i])
print("_______________________________________________________")

i = 0 
while  i < len(thislist) :
    print(thislist[i])
    i= i + 1
print("_______________________________________________________")

[print (x) for x in thislist]
print("_______________________________________________________")

