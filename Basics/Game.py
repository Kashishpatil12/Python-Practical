print("*** WELCOME TO OUR GAME ZONE ***")
TotalBalance = 5000
A = 1
while A == 1 :
    print("Your Total Balance is : ",TotalBalance)
    choice =  int(input("Plase Choose One Game and press that's number for play : \n 1 : Shooting Range         - 400/-   \n 2 : Kach Mandir            - 500/-   \n 3 : Scary House            - 900/-  \n 4 : Cricket                - 1000/-  \n 5 : Laser Attack           - 1100/-  \n 6 : Vollyball              - 1100/-  \n 7 : Mystery Room           - 1500/-  \n 8 : Laser Shooter          - 1550/-  \n 9 : Fun Zone               - 6000/- \n Enter your number : "))
    print("________________________________________________________________")

    if TotalBalance > 500 : 
    
        if choice == 1 : 
            price = 400
            print("1 : Shooting Range         400/-")
        elif choice == 2 : 
            price = 500
            print("2 : Kach Mandir             500/-")
        elif choice == 3 : 
            price = 900
            print("3 : Scary House         900/-")
        elif choice == 4 : 
            price = 1000
            print("4 : Cricket         1000/-")
        elif choice == 5 : 
            price = 1100
            print("5 : Laser Attack         1100/-")
        elif choice == 6 : 
            price = 1100
            print("6 : Vollayball         1100/-")
        elif choice == 7 : 
            price = 1500
            print("7 : Mystery Room         1500/-")
        elif choice == 8 : 
            price = 1500
            print("8 : Laser Shooter        1500/-")
        elif choice == 9 : 
            price = 6000
        

        if TotalBalance>price:
              TotalBalance = TotalBalance - price
              print("Your Total balance is : ",TotalBalance)
        else : 
            print("Your Total balance is not enough for play game - Plase topup your balance ")

            print("If you want to topup balance Press 1 and other for exit ")
            topup = int(input())
            if topup == 1 :
                amount = int(input("Enter yout amount : "))
                TotalBalance = TotalBalance + amount 
                print("Success Fully topup your balace")
            
               
            
        print("Do you want ot continue this game [press 1 for countinue] [other for exit]")
        A = int(input())
        A+1


        