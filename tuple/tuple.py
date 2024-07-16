x = ("apple","banana","cherry","apple","apple","banana")
print(x)
cont =0 
for i in x : 
    print(cont,i)
    cont+=1
print("________________")
print("Len   : ",len(x))

count = x.count("apple")
print("Apple : ",count)

#casting

l = list(x)
l.append("graps")
print("List  : ",l)

x = tuple(l)
print("tuple : ",x)





