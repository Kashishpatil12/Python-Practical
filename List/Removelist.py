
#remove
namelist = ["apple","banana","graps"]
namelist.remove("banana")
print(namelist)

print("_______________________________________________")

#Remove Specified Index
namelist = ["apple","banana","graps"]
namelist.pop(1)
print(namelist)

print("_______________________________________________")

#Remove last item
namelist = ["apple","banana","graps"]
namelist.pop()
print(namelist)

print("_______________________________________________")

#del will remove first item
namelist =["apple","banana","graps"]
del namelist[0]     
print(namelist)

print("_______________________________________________")

#Delete the entire list
namelist =["apple","banana","graps"]
del namelist

print("_______________________________________________")

#Clear the list 
#the clear() Method empties the list , the list still remains

namelist = ["apple","banana","graps"]
namelist.clear()
print(namelist)