set1 = {"a","b","c","d"}
set2 = {"e","f","g","i"}

set3 = set1.union(set2)
print(set3)

# update

set1.update(set2)
print(set1)

print("________________________________________")
# Keep ONLY the Duplicates

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

x.intersection_update(y)
print(x)
print("________________________________________")

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

z = x.intersection(y)
print(z)
print("________________________________________")

# Keep All, But NOT the Duplicates
# Keep the items that are not present in both sets:

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

x.symmetric_difference_update(y)
print(x)

x = {"apple","banana","cherry"}
y = {"google","microsoft","apple"}

x.symmetric_difference(y)
print(x)

print("________________________________________")
