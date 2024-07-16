fruits =("apple","banana","Strawberry","chikko")
(a,b,c,d) = fruits
print("----------------------")

print(a,b,c,d)

print("----------------------")

(*a,b,c) = fruits
print(a,b,c)
print("c",c)
print("b",b)
print("a  :",a)
# fruits =("apple","banana","Strawberry","chikko")

print("--------")
(x,*y,z) = fruits
print(x)
print("y",y)
print(x)

print("----------------------")
(x,y,*z) = fruits
print(x)
print(y)
print("z  :",z)
