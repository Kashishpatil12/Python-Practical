list1 = ["apple","banana"]
list2 = ["kerry","graps"]

list3 = list1 + list2
print(list3)
print("--------------------")

for i in list2 : 
    list1.append(i)
print(list1)
print("--------------------")

list1.extend(list2)
print(list1)
print("--------------------")

