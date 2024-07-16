namelist = ["kashish","siddhi","priya","kanan"]
namelist.append("riya")
print(namelist)
print("______________")

#Replace item
namelist[1]="neha"
print(namelist)
print("______________")

#insert item
namelist = ["kashish","sidhhi","priya","kanan"]
namelist.insert(1,"Riya")
print(namelist)
print("_________________")


#Extend List 
namelist=["kashish","siddhi","kanan"]
print(namelist)
print("-------")
secondlist = ["riya","neha","nisha"]
namelist.extend(secondlist)
print(namelist)
print("_________________")

namelist = ["kashish","siddhi","kanan"]
thislist = ("maya","kaya")
namelist.extend(thislist)
print(namelist)




