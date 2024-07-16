no = int(input("enter number for prime : "))

flag=0
for i in range(1,no) : 
    if no%2==0:
        flag=1
        break        
if flag==0:
        print("number is prime")
else:
        print("number is not prime") 
        
        