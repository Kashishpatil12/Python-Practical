dict = {
    "name" : "kashish",
    "rollno" : "38",
    "add" : "vastral",
    "age" : "19",
    "clg"  : "monark"
}
print("----------------")
print(dict)
print("----------------")
print(dict.keys())
print("----------------")
print(dict.values())
print("----------------")
#will display all key one by one
for i in dict : 
    print(i)

print("----------------------")
#will display all key one by one
for i in dict :
    print(dict[i])
print("----------------")
#print all keys and values 
for x,y in dict.items() :
    print("the key is ",x, "and values is ",y)
