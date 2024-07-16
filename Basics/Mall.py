print(" *** Welcome to our mall *** ")
print("_______________________________________________________")
print("If you are buying products from this amount , you getting discount of \n 40,000 for 20% , \n 50,000 for 30% , \n 70,000 for 50%") 
Total_amt = 0
cont = 1

while cont == 1 :
    amt =  int(input("Enter product amount : "))
    Total_amt = Total_amt + amt
    cont = int(input("Do you want to buying other product ? *Press for 1 yes or other for exit"))
    print("_______________________________________________________")
print("your total amount is : ",Total_amt)
print("*** Thanks for shopping with us ***")


if  Total_amt > 40000 : 
    discount = ((Total_amt * 20)/ 100)
    Total_amt =  Total_amt - discount

elif Total_amt > 50000 : 
    discount = Total_amt * 30 / 100
    Total_amt =  Total_amt - discount

elif Total_amt > 70000  :
    discount= Total_amt *  50 / 100
    Total_amt =  Total_amt - discount
else : 
    print("you can't get any discount") 


print("_________________________________________________________________")
print("you get discount : ",discount)
print("final amount is ",Total_amt)
print("_________________________________________________________________")