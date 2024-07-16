# Change Tuple Values

x = ("Rose","Lotus","Lily")
y = list(x)
y[1] = "Marigold"
x = tuple(y)
print(x)

# Add Items

thistuple = ("Rose","Lotus","lily","flower")
y = list(thistuple)
y.append("marigold")
print(y)

# Remove Items
y = list(thistuple)
y.remove("lily")
print(y)

#delete
thistuple =  ("Rose","Lotus","lily","flower")
del thistuple

