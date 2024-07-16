dics1 = {
    "roll" : "1",
    "name" : "ankit",    
    "surname" : "patel",
    "std" : 5
}
print(dics1)

dics1.update({"name" : "anil"}) #remove name element from
print(dics1)

dics1.pop("name") #remove last key and values
print(dics1)

dics1.popitem() # clear all key value from dictinory
print(dics1)


