val = int(input("enter value  : "))
factorial = 1 

for i in range(1,val): 
    factorial = i * factorial
    print(i , "*" ,factorial, end="") 