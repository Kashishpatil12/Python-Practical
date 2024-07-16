s1 = {"a","b","c"}
if "c" in s1 :
        print("yes c in set")
else : 
        print("c is not in set")

#add
s1.add("d")
print(s1)

#update
s2 = {"e","f","g"}
s1.update(s2)
print(s1)

#upadate() method does not have to be a set , it can  be any iterable object(tuple,lists,diction)
set1 = {"apple","banana","cherry"}
set2 = ["kiwi","orange"]

set1.update(set2)
print(set1)