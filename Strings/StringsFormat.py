age = "36 {}"
text = "is The age of kashish"
print(age.format(text))
print("---------------------")

firstname = "talent"
middlename = "computer"
lastname = "institute"

fullname = "The full name is of TCIT is {} {} {}"
print(fullname.format(firstname,middlename,lastname))
print("---------------------")

quantity = 3 
itemno = 567
price = 56.98
myorder  = "I want to pay {2} dollers for {0} pieces of item {1}"
print(myorder.format(price,itemno,quantity))
print("---------------------")

#write ""
txt = "Computer Academy \"TCIT\" from Odhav"
print(txt)

str = "Welcome \"Amit\""
print(str)
print("---------------------")

#find tsarting Posi tion
txt = "Hello, Welcome to Talent."
x = txt.find("Welcome")
print(x)
print("---------------------")

#count str
txt = "I love apples , apple are my favorite fruit."
x = txt.count("apple")
print(x)
print("---------------------")

# count specific index
txt = "I love apples , apples are my favorite fruits"
x = txt.count("apples",2,65)
print(x)
print("---------------------")

# capitalized 
txt = "hello , and welcome to my world!"
x = txt.capitalize()
print(x)
print("---------------------")

#lower String
txt = "Hello , and welcome to my world!"
x = txt.casefold()
print(x)
print("---------------------")

#islower
txt = "Talent computer Academy"
x = txt.casefold()
print(x)
print("---------------------")

#join
mytuple = ("vickey","khushbu","Shruti","bhavik")
x = " TCIT".join(mytuple)
print(x)
print("---------------------")

#replace
txt = "I like bananas"
x = txt.replace("banana","apple")
print(x)
print("-------")

txt = "one one was a race horse, two two was one too."
x = txt.replace("one","three")
print(x)
print("-------")

txt = "one one was a race horse, two two was one too."
x = txt.replace("one","three",2)

print("---------------------")

#split
txt = "Apple,Banana,Cherry"
x = txt.split(", ")
print(x)
print("-------")

p = "Bhavesh|manisha|ent"
x = p.split("|")
print(x)
# print("Of all Fruits,x , "is my favorite"")

txt = ",,,,,,,,,,,,,rrttggh.........banana.........rrrrrrrrr"
x = txt.strip(",")
print(x)
