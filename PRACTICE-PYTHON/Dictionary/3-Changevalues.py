car = {
    "brand" : "BMW",
    "Model" : "X5",
    "Price" : "95 lakhs",
    "year" : 2023,
    "colors" : ["Blue","Black","white"]
}

car["year"] =  2024


car.update({"price" : "1 Cr"})
print(car.items())
