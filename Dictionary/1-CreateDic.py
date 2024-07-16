dic = {
    "year"   :   2023,
    "month"  :  "August",
    "day"    :  "Monday",
    "Fruit"  :  "Apple",
    "name"   :  "kashish"
}
print(dic)
print(dic["name"])
print(dic.keys())
print(dic.values())

dic["name"] = "khushi"
print(dic.keys())
print(dic.values())

dic.update({"day" : "friday"})
print(dic)

