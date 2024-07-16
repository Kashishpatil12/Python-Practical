com = {"kashish","krishna","neha","hetvi","kanan"}
sci = {"kanan","sidhhi","neha","hetvi","foram"}
sports = {"khushi","ankita","hetvi","neha","manshi"}
fail = {"khushi","ankita","krishna"}
print("---------students are present in both sci & sports")
c = sci.intersection(com)
print(c) 

print("---------studetns are present in sci but not sports")
a = sci.difference(sports)
print(a)

print("---------students are present in com and sci but not sports")
x = c.difference(sports)
print(x)

print("----common---")
y = c.intersection(sports)
print(y)

print("---")
z = y.difference(fail)
print(z)

