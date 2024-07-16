car = {
    "brand" : "BMW",
    "Model" : "X5",
    "Price" : "95 lakhs",
    "year" : 2023,
    "colors" : ["Blue","Black","white"]
}

car["colors"] = "Black"
print(car)

car.update({"colors" : "white"})
print(car)
