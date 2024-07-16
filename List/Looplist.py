namelist = ["apple","banana","graps"]
for i in namelist : 
  print(i)
print(len(namelist))

for i in range(len(namelist)) : 
    print(i,namelist[i])
print("-------------------------------------")
#while 
i=0
while i < len(namelist) : 
    print(i,namelist)
    i = i+1
print("-------------------------------------")


#List Comprehension
[print(x) for x in namelist]

fruits = ["apple","banana","mango","pineapple","cherry","kiwi","orange"]
newlist = []

for x in fruits : 
    if "a" in x : 
        newlist.append(x)   

print("fruits : ",fruits)
print("newlist [i]:",newlist)
print("-------------------------------------")


#above code with list compreliension with in just one line
fruits = ["banana","mango","pineapple","cherry","kiwi","orange"]
newlist = [x for x in fruits if "c" in x]
print("New comprehension list")
print(newlist)

updatedlist = []
updatedlist = [x for x in fruits if x != "apple"]
print("updatedlist : ",updatedlist)
print("-------------------------------------")


#reutrn "orange" instead of "banana"
fruits = ["apple","banana","mango","pineapple","cherry","kiwi","orange"]
newlist = [x if x != "banana" else "orange" for x in fruits ]

print(newlist)

