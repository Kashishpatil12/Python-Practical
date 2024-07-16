thisdict = {
    "brand" : "BMW",
    "Model" : "X5",
    "Price" : "95 lakhs",
    "year" : 2023,
    "colors" : ["Blue","Black","white"]
}
x = thisdict["brand"]
print(x)
x = thisdict.get("Model")
print(x)

car = {
    "brand" : "BMW",
    "Model" : "X5",
    "Price" : "95 lakhs",
    "year" : 2023,
    "colors" : ["Blue","Black","white"]
}
x = car.keys()
print(x)
car["colors"] = "black"
print(x)

x = car.values()
print(x)

x = car.items()
print(x)

if "Model" in car :
    print("yes")