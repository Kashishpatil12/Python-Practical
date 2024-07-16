age = "20 {}"
text = "this is age of kashish"
print(age.format(text))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

fn = "talent"
sn = "computer"
ln = "institute"

fullname = "The full name of TCIT is {} {} {}"
print(fullname.format(fn,sn,ln))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


quint = 23
price = 50
itemno = 250
item = "I need a item no {} and quintity around {} , i pay you {} by upi"
print(item.format(itemno,23,price))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

txt = "Computer Acadamy \"TCIT\" from odhav[Vastral]"
print(txt)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#find 
txt = "This is TCIT -- Talent Computer Acadmy"
x = txt.find("TCIT")
print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#count str
txt = "This is TCIT -- Talent Computer Acadmy"
x = txt.count("T")
print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#capital
txt = "This is TCIT -- Talent Computer Acadmy"
print(txt.capitalize())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#lower case
txt = "This is TCIT -- Talent Computer Acadmy"
print(txt.lower())
txt = "This is TCIT -- Talent Computer Acadmy"
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#isfold
txt = "This is TCIT -- Talent Computer Acadmy"
print(txt.casefold())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#join
mytuple = ("kashish","sidhi","priya","kanan")
x = " TCIT-".join(mytuple)
print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#replace
txt = "i like Apple"
print(txt.replace("Apple","banana"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

txt = "apple banana kerry"
print(txt.replace("apple","kerry"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#split
txt = "apple,banana,kerry"
x = txt.split(", ")
print(x)

p = "apple|banana|kerry"
x = txt.split("| ")
print(x)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

txt = ",,,,,Kashish,,,,,,,,,,,,,patil,,,,,,,,,,,,,,,,,"
x = txt.strip(",")
price(x)``





