thislist = ["apple","Banana","cherry","graps","Orange","watermalon","mango"]
print("Thislist : ",thislist)
print("Access Items         :",thislist[1])
print("Negative Indexing    :",thislist[-1])
print("Range of Indexes     :",thislist[2:5])
print("Range of Indexes     :",thislist[:2])
print("Range of Indexes     :",thislist[2:])
print("Range of Negative Indexes :",thislist[-4:-1])
if "apple" in thislist :
    print("Check if Item Exists : ""Yes, 'apple' is in the fruits list")