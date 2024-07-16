print("Welcome to Our Bank")
print("___________________________________________________________________")

TotalBalance = 50000
print("Your Total Bank Balance is : ",TotalBalance)
print("___________________________________________________________________")
cont = 1 
Totaldeposite = 0
Totalwithdraw = 0
while cont == 1 :
    choice = int(input("press : \n 1 for deposite \n 2 for withdraw \n 3 for check balance \n"))
    
    if choice == 1 :
        Totaldeposite += 1
        deposite = int(input("Please Enter deposite amount : ")) 
        print("Your Deposite Amount is : ",deposite) 
        TotalBalance +=  deposite
        print("yout total amount is : ",TotalBalance)
        
    elif choice == 2 : 
        Totalwithdraw += 1
        withdraw = int(input("Please enter your withdraw amount : "))
        if withdraw > 20000 : 
            print("Your withdraw Amount is : ",withdraw) 
            TotalBalance -= withdraw 
        else : 
            print("Please Enter amount for withdraw")
        print("yout total amount is : ",TotalBalance)
    
    elif choice == 3 :
        print("Your total balance is : ",TotalBalance)
    else : 
        print("Please try again ")
    
    
    print("___________________________________________________________________")
    cont = int(input("Do you want to countinue press 1 yes or other for exit :"))
   

print("___________________________________________________________________")
print("Your Total deposite : ",Totaldeposite)
print("Your Total Withdrwa is : ",Totalwithdraw)

print("___________________________________________________________________")
print("Your current balance is : ",TotalBalance)
print("___________________________________________________________________")
print("Thank you For visiting our Bank")