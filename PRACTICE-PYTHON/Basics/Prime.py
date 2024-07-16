no = int(input("Enter Number : "))

flag =0 
for i in range(0,no) :
    if no%2==0 :
        flag =1
        break
if flag==0 :
    print("nuber is prime")
else : 
    print("number is not prime")