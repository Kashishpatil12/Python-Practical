s1 = {1,2,3,4,10}
s2 = {4,56,6,5,1,10}

s3 = s1.intersection(s2) 
print("Intersection : ",s3)

s4 = s1.difference(s2)
print("Difference : ",s4)

s5 = s1.union(s2)
print("union : ",s5)

#father and son
x = {"a","b","c","d","e","a"}
y = {"f","g","h","i","j","k"}
z = x.issubset(y)
print(z)

x1 = {"f","g","h","i","j","k"}
y1 = {"aa","b","e"}
z1 = x1.issuperset(y1)
print(z1)