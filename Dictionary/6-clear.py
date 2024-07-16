#clear

dict = {
    "a" : "a1",
    "b" : "b1",
    "c" : "c1"
}
print(dict)
print("-----------------------------")
# dict.clear()
print(dict)
print("-----------------------------")

#copy
dict1 = dict.copy()
print(dict1)

dict1.clear()
# print(dict1)
print("-----------------------------")

#get
print(dict1.get("a"))
print(dict.popitem()) #will display last key value

