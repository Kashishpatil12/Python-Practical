car = {
    "brand" : "BMW",
    "Model" : "X5",
    "Price" : "95 lakhs",
    "year" : 2023,
    "colors" : ["Blue","Black","white"]
}

car.pop("Model")
print(car)

car.popitem()
print(car)

car.clear()
print(car)