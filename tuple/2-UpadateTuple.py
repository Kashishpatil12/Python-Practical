tuple1 = (100,200,300,400)
print(tuple1)

for i in tuple1 : 
    print(i,"hello")

list1 = list(tuple1)
print("List  : ",list1)

list1.append('a')
list1=tuple(list1)
print("Tuple : ",tuple1)

x= ("a","b","c")
y= ("x","y","z")

total = x + y
print(total)
