# A tuple is a collection with is orderd and unchangeble.

tuple1 = ("a","b","c")
print(tuple1)
print("place [2] : " ,tuple1[2])

print("----------------------")
#Allow Duplicate values
tuple1=("a","b","c","d","a")
print(tuple1)

print("------count------------")

print(tuple1.count("a"))
print("len  :",len(tuple1))
tuple2 = ()
for x in tuple1 :
    print(x)

tuple3 = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(tuple3[1:5])
print(tuple3[:3])
print(tuple3[2::-1])