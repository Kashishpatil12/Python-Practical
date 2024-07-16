

comst = ["kashish patil","kanan patel","siddhi patel","neha patil","nisha patel"]
scist = ["ayushi patel","ridhhi patel","nikita patil","khushi patel","arpita patel"]

print("Total Studets : ")

print("_____________")
totalst = comst + scist

for i in totalst  :
    print(i)

newlist = []
for x in totalst : 
    if "patel" in x : 
        newlist.append(x)

print("_________________________________________")
for y in newlist :
    print(y)

namelist = []

print("total studets are : ")
namelist.copy(totalst)

